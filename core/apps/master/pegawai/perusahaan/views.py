from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Perusahaan , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, PerusahaanFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class PerusahaanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = Perusahaan.objects.all()
    serializer_class = serializers.CRPerusahaanSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PerusahaanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama','nama_direktur','alamat_kantor','email','no_hp']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_perusahaan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Perusahaan.",
        description="Get Data Perusahaan.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Perusahaan'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'perusahaan.view',headers=header, relation=relation, fields=fields,title=title)   

    @extend_schema(
        methods=["POST"],
        summary="Create Data Perusahaan.",
        description="Create Data Perusahaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'perusahaan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Perusahaan",
        description="Get Details Perusahaan",
        tags=['master_pegawai']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        perusahaan = self.queryset.filter(id_perusahaan=pk)
        if perusahaan is None:
            return not_found('perusahaan.not_found')

        serializer = self.serializer_class(perusahaan, many=True)
        return response__(request, serializer, 'perusahaan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Perusahaan.",
        description="Update Data Perusahaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def update(self, request, pk):
        perusahaan = get_object_or_404(Perusahaan, pk=pk)
        serializer = self.serializer_class(instance=perusahaan, data=request.data)

        return post_update_response(serializer, 'perusahaan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Perusahaan.",
        description="Delete Data Perusahaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def destroy(self, request, pk):
        perusahaan = get_object_or_404(Perusahaan, pk=pk)
        self.perform_destroy(perusahaan)
        return response__(request, perusahaan, 'perusahaan.delete')

    def perform_destroy(self, instance):
        instance.delete()
