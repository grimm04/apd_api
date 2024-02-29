import imp
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
# serializers
from .serializers import AuthSerializer, ChangePasswordSerializer, AuthDetailSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404

from apps.users.models import Users
# swagger
from drf_spectacular.utils import extend_schema, OpenApiParameter

# jwt serializer 
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from django.contrib.auth import get_user_model

# custom user login
from .custom_serializers import CustomTokenObtainPairSerializer, InActiveUser, UserNotFound, PasswordNotMatch
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenViewBase

from apps.histori.users_his_password.models import USER_HIS_PASSWORD
from django.contrib.auth.hashers import check_password,make_password
User = get_user_model()

from rest_framework import serializers

class CustomTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.

    Returns HTTP 406 when user is inactive and HTTP 401 when login credentials are invalid.
    """
    serializer_class = CustomTokenObtainPairSerializer
 
    def validate_user(self, request):
        user = Users.objects.filter(username=request.data.get('username')).first()  
        if not user:
            raise UserNotFound  
        if not check_password(request.data.get('password'), user.password):
            raise PasswordNotMatch 

    def post(self, request, *args, **kwargs):   
        self.validate_user(request) 
        serializer = self.get_serializer(data=request.data) 
        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed:
            raise InActiveUser()
        except TokenError:
            raise InvalidToken()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class AuthDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        methods=["POST"],
        summary="Detail user login.",
        description="Detail user login.",
        request=None,
        responses=None,
        # more customizations
    )
    def post(self, request):
        user = self.get_object(request.user.id)
        serializer = AuthDetailSerializer(user)
        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Detail User',
            "data": serializer.data
        })


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    @extend_schema(
        methods=["POST"],
        summary="Register user baru",
        description="Register user baru",
        request=AuthSerializer,
        responses=AuthSerializer,
        # more customizations
    )
    def post(self, request, format='json'):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = ChangePasswordSerializer

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # make sure to catch 404's below
    #     obj = queryset.get(pk=self.request.user.id)
    #     self.check_object_permissions(self.request, obj) 
    #     return obj

        # def get_object(self, queryset=None):
    #     obj = self.request.user
    #     return obj

    # def put(self,request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(context = {'request':request}, data=request.data)

    #     print(serializer)
    #     serializer = ChangePasswordSerializer(instance=self.request.user, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #          serializer.save()
    #          return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if serializer.is_valid():
    #     # Check old password
    #     if not self.object.check_password(serializer.data.get("old_password")):
    #         return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
    #         # set_password also hashes the password that the user will get
    #         self.object.set_password(serializer.data.get("new_password"))
    #         self.object.save()
    #         response = {
    #             'status': 'success',
    #             'code': status.HTTP_200_OK,
    #             'message': 'Password updated successfully',
    #             'data': []
    #         }

    #         return Response(response)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user_id = self.request.user.id 
            # print('tes', password)
            if user_id != self.object.id_user: 
                raise serializers.ValidationError({"authorize": "Tidak Mempunyai Akses merubah user ini."}) 
            password = request.data.get('password')  
            self.object.set_password(password)
            self.object.save()
            if self.object :
                user = get_object_or_404(Users, pk=user_id)   
                his = USER_HIS_PASSWORD(id_user=user,password=make_password(password))
                his.save()  
            # return self.object
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password Berhasil Diubah'
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    @extend_schema(
        methods=["POST"],
        summary="Logout",
        description="User logout",
    )
    def post(self, request):
        try:
            tokens = OutstandingToken.objects.filter(id_user=request.user.id)
            for token in tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=token)

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
