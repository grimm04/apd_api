from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TelemetringAMRCustomer, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import TelemetringAMRCustomerFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination

class TelemetringAMRCustomerViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringAMRCustomer.objects.all()
    serializer_class = serializers.TelemetringAMRCustomerSerializers
    update_serializer_class = serializers.UDTelemetringAMRCustomerSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringAMRCustomerFilter
    filterset_fields = ['keyword']
    search_fields = ['id', 'customer_rid', 'meter_id', 'meter_type', 'rate', 'modem_adr', 'nama', 'alamat', 'lok', 'daya', 'bapm', 'faktor_kali', 'nofa', 'goltarif', 'kodegardu']
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - AMR Customer",
        description="Get OPSISDIS - Telemetring - AMR Customer",
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
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        fields = EXPORT_FIELDS
        title = 'Laporan Telemetring Customer'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_amr_customer.view', headers=header, relation=relation,
                        fields=fields, title=title)

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - AMR Customer - Specified.",
        description="Get OPSISDIS - Telemetring - AMR Customer - Specified.",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_amr_customer = self.queryset.filter(pk=pk)
        if not telemetring_amr_customer:
            return not_found('telemetring_amr_customer.not_found')

        serializer = self.serializer_class(telemetring_amr_customer, many=True)
        return response__(request, serializer, 'telemetring_amr_customer.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - AMR Customer - Specified",
        description="Update OPSISDIS - Telemetring - AMR Customer - Specified",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        telemetring_amr_customer = get_object_or_404(TelemetringAMRCustomer, pk=pk)
        serializer = self.update_serializer_class(instance=telemetring_amr_customer, data=request.data)

        return post_update_response(serializer, 'telemetring_amr_customer.update')