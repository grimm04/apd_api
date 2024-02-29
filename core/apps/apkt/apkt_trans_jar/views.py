from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import APKTTransJAR, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import SearchFilter, APKTTransJARFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


class APKTTransJARViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = APKTTransJAR.objects.all()
    serializer_class = serializers.APKTTransJARSerializers
    update_serializer_class = serializers.UDAPKTTransJARSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = APKTTransJARFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['id_apkt_trans_jar', 'no_laporan', 'nama_laporan', 'tgl_laporan', 'no_apkt', 'status_laporan', 'jenis_laporan', 'jlh_gardu_nyala', 'jlh_gardu_padam', 'tgl_nyala_terakhir', 'tgl_close_laporan', 'status_apkt_kirim_padam', 'tgl_padam', 'server_apkt', 'res_apkt_kirim_padam', 'id_feeder', 'feeder', 'status_data', 'tgl_nyala_awal', 'tgl_mulai_apkt_kirim_padam', 'tgl_selesai_apkt_kirim_padam', 'status_apkt_kirim_nyala', 'tgl_mulai_apkt_kirim_nyala', 'tgl_selesai_apkt_kirim_nyala', 'nama_switch', 'point_number_switch', 'kode_aset', 'jenis_Aset', 'parent_aset', 'res_apkt_kirim_nyala', 'tgl_apkt_kirim_nyala']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_apkt_trans_jar']

    @extend_schema(
        methods=["POST"],
        summary="Create APKT - APKT TRANS JAR.",
        description="Create APKT - APKT TRANS JAR.",
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'apkt_trans_jar.create')

    @extend_schema(
        methods=["GET"],
        summary="Get APKT - APKT TRANS JAR.",
        description="Get APKT - APKT TRANS JAR.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def list(self, request):
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        fields = EXPORT_FIELDS
        title = 'APKT TRANS JAR'

        queryset = self.filter_queryset(self.get_queryset())
        return get_response(self, request, queryset, 'apkt_trans_jar.view',headers=header, relation=relation, fields=fields,title=title)

    @extend_schema(
        methods=["GET"],
        summary="Get APKT - APKT TRANS JAR (Specified).",
        description="Get APKT - APKT TRANS JAR (Specified).",
        tags=['apkt']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        apkt_trans_jar = self.queryset.filter(pk=pk)
        if not apkt_trans_jar :
            return not_found('apkt_trans_jar.not_found')

        serializer = self.serializer_class(apkt_trans_jar, many=True)
        return response__(request, serializer, 'apkt_trans_jar.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update APKT - APKT TRANS JAR.",
        description="Update APKT - APKT TRANS JAR.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['apkt']
    )
    def update(self, request, pk):
        apkt_trans_jar = get_object_or_404(APKTTransJAR, pk=pk)
        serializer = self.update_serializer_class(instance=apkt_trans_jar, data=request.data)

        return post_update_response(serializer, 'apkt_trans_jar.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete APKT - APKT TRANS JAR.",
        description="Delete APKT - APKT TRANS JAR.",
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def destroy(self, request, pk):
        apkt_trans_jar = get_object_or_404(APKTTransJAR, pk=pk)
        self.perform_destroy(apkt_trans_jar)
        return response__(request, apkt_trans_jar, 'apkt_trans_jar.delete')

    def perform_destroy(self, instance):
        instance.delete()