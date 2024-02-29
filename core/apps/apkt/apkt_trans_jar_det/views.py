from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import APKTTransJARDet, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import SearchFilter, APKTTransJARDetFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


class APKTTransJARDetViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = APKTTransJARDet.objects.all()
    serializer_class = serializers.APKTTransJARDetSerializers
    update_serializer_class = serializers.UDAPKTTransJARDetSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = APKTTransJARDetFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['id_apkt_trans_jar_det', 'tgl_padam', 'tgl_nyala', 'tgl_apkt_kirim_padam', 'tgl_padam_scada', 'status_apkt_kirim_padam', 'status_data', 'tgl_user_update_padam', 'server_apkt', 'gardu_mjd', 'id_feeder', 'id_gi', 'tgl_apkt_kirim_nyala', 'status_apkt_kirim_nyala', 'res_apkt_kirim_nyala', 'tgl_apkt_kirim', 'res_apkt_kirim', 'tgl_user_update_nyala', 'tgl_mulai_apkt_kirim_padam', 'tgl_selesai_apkt_kirim_padam', 'tgl_mulai_apkt_kirim_nyala', 'tgl_selesai_apkt_kirim_nyala', 'kode_aset', 'parent_aset', 'kode_ref_aset_jenis', 'kode_feeder', 'jenis_aset', 'tgl_user_update', 'res_apkt_kirim_padam']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_apkt_trans_jar_det']

    @extend_schema(
        methods=["POST"],
        summary="Create APKT - APKT TRANS JAR Det.",
        description="Create APKT - APKT TRANS JAR Det.",
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'apkt_trans_jar_det.create')

    @extend_schema(
        methods=["GET"],
        summary="Get APKT - APKT TRANS JAR Det.",
        description="Get APKT - APKT TRANS JAR Det.",
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
        title = 'APKT TRANS JAR DET'

        queryset = self.filter_queryset(self.get_queryset())
        return get_response(self, request, queryset, 'apkt_trans_jar_det.view',headers=header, relation=relation, fields=fields,title=title)

    @extend_schema(
        methods=["GET"],
        summary="Get APKT - APKT TRANS JAR Det (Specified).",
        description="Get APKT - APKT TRANS JAR Det (Specified).",
        tags=['apkt']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        apkt_trans_jar_det = self.queryset.filter(pk=pk)
        if not apkt_trans_jar_det :
            return not_found('apkt_trans_jar_det.not_found')

        serializer = self.serializer_class(apkt_trans_jar_det, many=True)
        return response__(request, serializer, 'apkt_trans_jar_det.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update APKT - APKT TRANS JAR Det.",
        description="Update APKT - APKT TRANS JAR Det.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['apkt']
    )
    def update(self, request, pk):
        apkt_trans_jar_det = get_object_or_404(APKTTransJARDet, pk=pk)
        serializer = self.update_serializer_class(instance=apkt_trans_jar_det, data=request.data)

        return post_update_response(serializer, 'apkt_trans_jar_det.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete APKT - APKT TRANS JAR Det.",
        description="Delete APKT - APKT TRANS JAR Det.",
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def destroy(self, request, pk):
        apkt_trans_jar_det = get_object_or_404(APKTTransJARDet, pk=pk)
        self.perform_destroy(apkt_trans_jar_det)
        return response__(request, apkt_trans_jar_det, 'apkt_trans_jar_det.delete')

    def perform_destroy(self, instance):
        instance.delete()