from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import LaranganTanggungJawabMitra,EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, LaranganTanggungJawabMitraFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination

class LaranganTanggungJawabMitraView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = LaranganTanggungJawabMitra.objects.all()
    serializer_class = serializers.LaranganTanggungJawabMitraSerializers
    create_serializer_class = serializers.CRLaranganTanggungJawabMitraCSerializers
    update_serializer_class = serializers.UDLaranganTanggungJawabMitraSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaranganTanggungJawabMitraFilter
    filterset_fields = ['keyword']
    search_fields = ['uraian']
    ordering_fields = '__all__'
    ordering = ['id_larangan_tanggung_jawab_mitra']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Larangan & Tanggung Jawab Mitra.",
        description="Get Data Larangan & Tanggung Jawab Mitra.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Larangan & Tanggung Jawab QRC'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'larangan_tanggung_jawab_mitra.view',headers=header, relation=relation, fields=fields,title=title) 
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Larangan & Tanggung Jawab Mitra.",
        description="Create Data Larangan & Tanggung Jawab Mitra.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_working_permit']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'larangan_tanggung_jawab_mitra.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Larangan & Tanggung Jawab Mitra",
        description="Get Details Larangan & Tanggung Jawab Mitra",
        tags=['master_working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        larangan_tanggung_jawab_mitra = self.queryset.filter(pk=pk)
        if not larangan_tanggung_jawab_mitra:
            return not_found('larangan_tanggung_jawab_mitra.not_found')

        serializer = self.serializer_class(larangan_tanggung_jawab_mitra, many=True)
        return response__(request, serializer, 'larangan_tanggung_jawab_mitra.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Larangan & Tanggung Jawab Mitra.",
        description="Update Data Larangan & Tanggung Jawab Mitra.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_working_permit']
    )
    def update(self, request, pk):
        larangan_tanggung_jawab_mitra = get_object_or_404(LaranganTanggungJawabMitra, pk=pk)
        serializer = self.update_serializer_class(instance=larangan_tanggung_jawab_mitra, data=request.data)
        return post_update_response(serializer, 'larangan_tanggung_jawab_mitra.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Larangan & Tanggung Jawab Mitra.",
        description="Delete Data Larangan & Tanggung Jawab Mitra.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def destroy(self, request, pk):
        larangan_tanggung_jawab_mitra = get_object_or_404(LaranganTanggungJawabMitra, pk=pk)
        self.perform_destroy(larangan_tanggung_jawab_mitra)
        return response__(request, larangan_tanggung_jawab_mitra, 'larangan_tanggung_jawab_mitra.delete')

    def perform_destroy(self, instance):
        instance.delete()
