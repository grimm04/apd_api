from imp import PKG_DIRECTORY
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TelemetringAMREnergi, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS, EXPORT_HEADERS_CUSTOM_XLSX
from .filters import TelemetringAMREnergiFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found, response_basic
from base.custom_pagination import CustomPagination

class TelemetringAMREnergiViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringAMREnergi.objects.all()
    serializer_class = serializers.TelemetringAMREnergiSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringAMREnergiFilter
    filterset_fields = ['keyword']
    search_fields = ['id', 'tgl', 'kwh', 'kvarh', 'kvah', 'tgl_maxdem', 'maxdem', 'rate1', 'rate2', 'rate3', 'rate1_prev', 'rate2_prev', 'rate3_prev', 'kwh_prev', 'fk', 'kvarh_prev', 'tgl_capture', 'tgl_prev', 'kvah_prev']
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - AMR Energi",
        description="Get OPSISDIS - Telemetring - AMR Energi",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def list(self, request):
        header = EXPORT_HEADERS
        header_custom = EXPORT_HEADERS_CUSTOM_XLSX
        relation = EXPORT_RELATION_FIELD
        fields = EXPORT_FIELDS
        title = 'Laporan Telemetring AMR Energi'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_amr_energi.view', headers=header, relation=relation,
                        fields=fields, title=title, header_custom=header_custom)

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - AMR Energi - Specified.",
        description="Get OPSISDIS - Telemetring - AMR Energi - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_amr_energi = self.queryset.filter(pk=pk)
        if not telemetring_amr_energi:
            return not_found('telemetring_amr_energi.not_found')

        serializer = self.serializer_class(telemetring_amr_energi, many=True)
        return response__(request, serializer, 'telemetring_amr_energi.view')