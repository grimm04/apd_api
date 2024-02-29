from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Frekuensi , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, FrekuensiFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class FrekuensiViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = Frekuensi.objects.all()
    serializer_class = serializers.FrekuensiSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = FrekuensiFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama', 'lokasi', 'status']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_meter']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - OPSIDIS - Frekuensi.",
        description="Get Data Master - OPSIDIS - Frekuensi.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Frekuensi'

        queryset = self.filter_queryset(self.get_queryset())
        return get_response(self, request, queryset, 'opsisdis_frekuensi.view', headers=header, relation=relation, fields=fields, title=title)

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - OPSIDIS - Frekuensi.",
        description="Create Data Master - OPSIDIS - Frekuensi.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'opsisdis_frekuensi.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - OPSIDIS - Frekuensi.",
        description="Get Details Master - OPSIDIS - Frekuensi.",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        master = self.queryset.filter(pk=pk)
        if master is None:
            return not_found('fasop_point_type.not_found')

        serializer = self.serializer_class(master, many=True)
        return response__(request, serializer, 'opsisdis_frekuensi.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - OPSIDIS - Frekuensi.",
        description="Update Data Master - OPSIDIS - Frekuensi.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        master = get_object_or_404(Frekuensi, pk=pk)
        serializer = self.serializer_class(instance=master, data=request.data)

        return post_update_response(serializer, 'opsisdis_frekuensi.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - OPSIDIS - Frekuensi.",
        description="Delete Data Master - OPSIDIS - Frekuensi.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        master = get_object_or_404(Frekuensi, pk=pk)
        self.perform_destroy(master)
        return response__(request, master, 'opsisdis_frekuensi.delete')

    def perform_destroy(self, instance):
        instance.delete()