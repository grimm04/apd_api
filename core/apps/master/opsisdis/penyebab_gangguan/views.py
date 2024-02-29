from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import PenyebabGangguan , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, PenyebabGangguanFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


# Create your views here.
class PenyebabGangguanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PenyebabGangguan.objects.all()
    serializer_class = serializers.CRPenyebabGangguanSerializers
    ru_serializer_class = serializers.RUPenyebabGangguanSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PenyebabGangguanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_penyebab_gangguan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Penyebab Gangguan.",
        description="Get Data Penyebab Gangguan.",
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
        title        = 'opsisdis_penyebab_gangguan'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'opsisdis_penyebab_gangguan.view',headers=header, relation=relation, fields=fields,title=title)  
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Penyebab Gangguan.",
        description="Create Data Penyebab Gangguan.",
        request=ru_serializer_class,
        responses=ru_serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.ru_serializer_class(data=data)

        return post_update_response(serializer, 'opsisdis_penyebab_gangguan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Penyebab Gangguan",
        description="Get Details Penyebab Gangguan",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        departemen = self.queryset.filter(id_penyebab_gangguan=pk)
        if departemen is None:
            return not_found('opsisdis_penyebab_gangguan.not_found')

        serializer = self.serializer_class(departemen, many=True)
        return response__(request, serializer, 'opsisdis_penyebab_gangguan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Penyebab Gangguan.",
        description="Update Data Penyebab Gangguan.",
        request=ru_serializer_class,
        responses=ru_serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        departemen = get_object_or_404(PenyebabGangguan, pk=pk)
        serializer = self.ru_serializer_class(instance=departemen, data=request.data)

        return post_update_response(serializer, 'opsisdis_penyebab_gangguan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Penyebab Gangguan.",
        description="Delete Data Penyebab Gangguan.",
        request=ru_serializer_class,
        responses=ru_serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        departemen = get_object_or_404(PenyebabGangguan, pk=pk)
        self.perform_destroy(departemen)
        return response__(request, departemen, 'opsisdis_penyebab_gangguan.delete')

    def perform_destroy(self, instance):
        instance.delete()
