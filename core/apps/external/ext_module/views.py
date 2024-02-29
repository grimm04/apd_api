from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import ExtModule
from . import serializers
from .filters import SearchFilter, ExtModuleFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class ExtModuleViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = ExtModule.objects.all()
    serializer_class = serializers.ExtModuleSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ExtModuleFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_module']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - External - Ext Module.",
        description="Get Data Master - External - Ext Module.",
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

        return get_response(self, request, queryset, 'ext_module.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - External - Ext Module.",
        description="Create Data Master - External - Ext Module.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ext_module.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - External - Ext Module.",
        description="Get Details Master - External - Ext Module.",
        tags=['external']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ext_module = self.queryset.filter(id_module=pk)
        if ext_module is None:
            return not_found('ext_module.not_found')

        serializer = self.serializer_class(ext_module, many=True)
        return response__(request, serializer, 'ext_module.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - External - Ext Module.",
        description="Update Data Master - External - Ext Module.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def update(self, request, pk):
        ext_module = get_object_or_404(ExtModule, pk=pk)
        serializer = self.serializer_class(instance=ext_module, data=request.data)

        return post_update_response(serializer, 'ext_module.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - External - Ext Module.",
        description="Delete Data Master - External - Ext Module.",
        request=serializer_class,
        responses=serializer_class,
        tags=['external']
    )
    def destroy(self, request, pk):
        ext_module = get_object_or_404(ExtModule, pk=pk)
        self.perform_destroy(ext_module)
        return response__(request, ext_module, 'ext_module.delete')

    def perform_destroy(self, instance):
        instance.delete()
