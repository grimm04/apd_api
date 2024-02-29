 
from django.contrib.auth.hashers import check_password 
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from .serializers import CustomUserSerializer, UpdateUserSerializer, UpdatePasswordUser, ResetPasswordUser, UserListSerializer, UpdateReguPetugasSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
# swagger
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Users
from .filters import SearchFilter, UserFilter

# base response 
from base.response import response__, get_response, post_update_response, not_found, response_basic
from base.negotiation import CustomContentNegotiation
# custom pagination
from base.custom_pagination import CustomPagination


class UsersView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = UserListSerializer
    serializer_create_class = CustomUserSerializer
    serializer_update_class = UpdateUserSerializer
    serializer_update_password_class = UpdatePasswordUser
    serializer_reset_password_class = ResetPasswordUser
    serializer_update_regu_class = UpdateReguPetugasSerializer
    queryset = Users.objects.all()
    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = UserFilter
    filterset_fields = ['fullname', 'username']
    search_fields = ['fullname', 'username', 'email','nip','sap','status']
    ordering_fields = '__all__'
    # sorting by field, tambah "-" untuk descending, ecample: -id_user
    ordering = ['id_user']

    @extend_schema(
        methods=["GET"],
        summary="List all the users.",
        description="Return a list of all usernames in the system.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='show per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        # format=(xmlreader,JsonResponse)
        tags=['admin']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'users.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Data User.",
        description="Create Data User.",
        request=serializer_create_class,
        responses=serializer_create_class,
        tags=['admin']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_create_class(data=data)

        return post_update_response(serializer, 'users.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied User",
        description="Get Details User",
        tags=['admin']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        users = self.queryset.filter(pk=pk)
        if users is None:
            return not_found('users.not_found')

        serializer = self.serializer_class(users, many=True)
        return response__(request, serializer, 'users.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Spesific User",
        description="Update User",
        request=serializer_update_class,
        responses=serializer_update_class,
        tags=['admin']
    )
    def update(self, request, pk):
        users = get_object_or_404(Users, pk=pk)
        serializer = self.serializer_update_class(instance=users, data=request.data)

        return post_update_response(serializer, 'users.update')
    
    @extend_schema(
        methods=["PUT"],
        summary="Users - Update Regu",
        description="Users - Update Regu",
        request=serializer_update_regu_class,
        responses=serializer_update_regu_class,
        tags=['admin']
    )
    @action(detail=False, methods=['PUT'], url_path='regu/(?P<id_user>\d+)', url_name='regu-user') 
    def update_user(self, request, id_user):
        user = get_object_or_404(Users, pk=id_user)
        serializer = self.serializer_update_regu_class(instance=user, data=request.data) 
        return post_update_response(serializer, 'users.update_regu')
    

    @extend_schema(
        methods=["PUT"],
        summary="Users - Delete Regu",
        description="Users - Delete Regu",
        request=None,
        responses=None,
        tags=['admin']
    )
    @action(detail=False, methods=['PUT'], url_path='delete-regu/(?P<id_user>\d+)', url_name='delete-regu-user') 
    def delete_regu(self, request, id_user):
        user = get_object_or_404(Users, pk=id_user)
        data = {
            'id_ref_regu_petugas':None
        }
        serializer = self.serializer_update_regu_class(instance=user, data=data) 
        return post_update_response(serializer, 'users.delete_regu')

    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Password Specific User.",
    #     description="Update Password Specific User.",
    #     request=serializer_update_password_class,
    #     responses=serializer_update_class,
    #     tags=['admin']
    # )
    # @action(detail=True, methods=['PUT'], url_path='update-user-password', url_name='update-user-password')
    # def update_user_password(self, request, pk):
    #     old_password = request.data['old_password']
    #     new_password = request.data['new_password']
    #     retype_new_password = request.data['retype_new_password']
    #
    #     if not old_password or not new_password or not retype_new_password:
    #         return response_basic(_status=False, msg='users.update_password_field')
    #
    #     users = get_object_or_404(Users, pk=pk)
    #     if not users.check_password(old_password):
    #         return response_basic(_status=False, msg='users.update_password_old_notmatch')
    #
    #     if new_password != retype_new_password:
    #         return response_basic(_status=False, msg='users.update_password_notmatch')
    #
    #     users.set_password(new_password)
    #     users.save()
    #
    #     serializer = self.serializer_update_class(instance=users)
    #
    #     return response_basic(_status=True, msg='users.update_password', results=serializer.data)

    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Reset Password User.",
    #     description="Reset Password User.",
    #     request=serializer_reset_password_class,
    #     responses=serializer_update_class,
    #     tags=['admin']
    # )
    # @action(detail=True, methods=['PUT'], url_path=r'reset-user-password', url_name='reset-user-password')
    # def reset_user_password(self, request, pk):
    #     new_password = request.data['new_password']
    #
    #     if not new_password:
    #         return response_basic(_status=False, msg='users.reset_password_field')
    #
    #     users = get_object_or_404(Users, pk=pk)
    #     users.set_password(new_password)
    #     users.save()
    #
    #     serializer = self.serializer_update_class(instance=users)
    #
    #     return response_basic(_status=True, msg='users.update_password', results=serializer.data)

    @extend_schema(
        methods=["DELETE"],
        summary="Remove Spesific User",
        description="Delete User",
        tags=['admin']
    )
    def destroy(self, request, pk):
        users = get_object_or_404(Users, pk=pk)
        self.perform_destroy(users)
        return response__(request, users, 'users.delete')

    def perform_destroy(self, instance):
        instance.delete()


class UsersResetPasswordView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = CustomUserSerializer 
    serializer_reset_password_class = ResetPasswordUser
    serializer_update_class = UpdateUserSerializer 
    queryset = Users.objects.all() 

    @extend_schema(
        methods=["PUT"],
        summary="Reset Password User.",
        description="Reset Password User.",
        request=serializer_reset_password_class,
        responses=serializer_class,
        tags=['admin']
    )
    def update(self, request, pk):
        new_password = request.data['new_password']

        if not new_password:
            return response_basic(_status=False, msg='users.reset_password_field')

        users = get_object_or_404(Users, pk=pk)
        users.set_password(new_password)
        users.save()

        serializer = self.serializer_update_class(instance=users)

        return response_basic(_status=True, msg='users.update_password', results=serializer.data)
