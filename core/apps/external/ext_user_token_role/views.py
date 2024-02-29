from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import ExtUserTokenRole
from . import serializers
from .filters import SearchFilter, ExtUserTokenRoleFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class ExtUserTokenRoleViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = ExtUserTokenRole.objects.all()
    serializer_class = serializers.ExtUserTokenRoleSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ExtUserTokenRoleFilter
    filterset_fields = []  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_token_role']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - External - Ext User Token Role.",
        description="Get Data Master - External - Ext User Token Role.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ext_user_token_role.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - External - Ext User Token Role.",
        description="Create Data Master - External - Ext User Token Role.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ext_user_token_role.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - External - Ext User Token Role.",
        description="Get Details Master - External - Ext User Token Role.",
        tags=['external']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ext_token_role = self.queryset.filter(id_token_role=pk)
        if ext_token_role is None:
            return not_found('ext_user_token_role.not_found')

        serializer = self.serializer_class(ext_token_role, many=True)
        return response__(request, serializer, 'ext_user_token_role.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - External - Ext User Token Role.",
        description="Update Data Master - External - Ext User Token Role.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def update(self, request, pk):
        ext_token_role = get_object_or_404(ExtUserTokenRole, pk=pk)
        serializer = self.serializer_class(instance=ext_token_role, data=request.data)

        return post_update_response(serializer, 'ext_user_token_role.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - External - Ext User Token Role.",
        description="Delete Data Master - External - Ext User Token Role.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def destroy(self, request, pk):
        ext_token_role = get_object_or_404(ExtUserTokenRole, pk=pk)
        self.perform_destroy(ext_token_role)
        return response__(request, ext_token_role, 'ext_user_token_role.delete')

    def perform_destroy(self, instance):
        instance.delete()
