from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import USER_HIS_PASSWORD 
from . import serializers
from .filters import SearchFilter, USER_HIS_PASSWORDFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


class UsersHisPasswordViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = USER_HIS_PASSWORD.objects.all()
    serializer_class = serializers.USER_HIS_PASSWORDSerializers
    create_serializer_class = serializers.CRUSER_HIS_PASSWORDCSerializers
    update_serializer_class = serializers.UDUSER_HIS_PASSWORDSerializers

    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = USER_HIS_PASSWORDFilter
    # filterset_fields = ['keyword']
    # search_fields = ['p','path2','path3']
    ordering_fields = '__all__'
    ordering = ['id_user_his_password']

    @extend_schema(
        methods=["GET"],
        summary="Get His Users Password",
        description="Get His Users Password",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=15), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['histori']
    )
    def list(self, request): 

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'user_his_password.view')  

    @extend_schema(
        methods=["POST"],
        summary="Create His Users Password",
        description="Create His Users Password",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['histori']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'user_his_password.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Histori Users Password",
        description="Get Details Histori Users Password",
        tags=['histori']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        user_his_password = self.queryset.filter(pk=pk)
        if not user_his_password:
            return not_found('user_his_password.not_found')

        serializer = self.serializer_class(user_his_password, many=True)
        return response__(request, serializer, 'user_his_password.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update His Users Password",
        description="Update His Users Password",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['histori']
    )
    def update(self, request, pk):
        user_his_password = get_object_or_404(USER_HIS_PASSWORD, pk=pk)
        serializer = self.update_serializer_class(instance=user_his_password, data=request.data)
        return post_update_response(serializer, 'user_his_password.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delett His Users Password",
        description="Delett His Users Password",
        request=serializer_class,
        responses=serializer_class,
        tags=['histori']
    )
    def destroy(self, request, pk):
        user_his_password = get_object_or_404(USER_HIS_PASSWORD, pk=pk)
        self.perform_destroy(user_his_password)
        return response__(request, user_his_password, 'user_his_password.delete')

    def perform_destroy(self, instance):
        instance.delete()
