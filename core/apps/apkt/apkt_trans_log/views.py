from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import APKTTransLog, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import SearchFilter, APKTTransLogFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


class APKTTransLogViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = APKTTransLog.objects.all()
    serializer_class = serializers.APKTTransLogSerializers
    update_serializer_class = serializers.UDAPKTTransLogSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = APKTTransLogFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['id_apkt_trans_log', 'tgl_mulai', 'tgl_selesai', 'input_apkt', 'output_apkt', 'tgl_buat', 'server_apkt', 'webservice']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_apkt_trans_log']

    @extend_schema(
        methods=["POST"],
        summary="Create APKT - APKT Trans Log.",
        description="Create APKT - APKT Trans Log.",
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'apkt_trans_log.create')

    @extend_schema(
        methods=["GET"],
        summary="Get APKT - APKT Trans Log.",
        description="Get APKT - APKT Trans Log.",
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
        title = 'APKT TRANS LOG'

        queryset = self.filter_queryset(self.get_queryset())
        return get_response(self, request, queryset, 'apkt_trans_log.view',headers=header, relation=relation, fields=fields,title=title)

    @extend_schema(
        methods=["GET"],
        summary="Get APKT - APKT Trans Log (Specified).",
        description="Get APKT - APKT Trans Log (Specified).",
        tags=['apkt']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        apkt_trans_log = self.queryset.filter(pk=pk)
        if not apkt_trans_log :
            return not_found('apkt_trans_log.not_found')

        serializer = self.serializer_class(apkt_trans_log, many=True)
        return response__(request, serializer, 'apkt_trans_log.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update APKT - APKT Trans Log.",
        description="Update APKT - APKT Trans Log.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['apkt']
    )
    def update(self, request, pk):
        apkt_trans_log = get_object_or_404(APKTTransLog, pk=pk)
        serializer = self.update_serializer_class(instance=apkt_trans_log, data=request.data)

        return post_update_response(serializer, 'apkt_trans_log.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete APKT - APKT Trans Log.",
        description="Delete APKT - APKT Trans Log.",
        request=serializer_class,
        responses=serializer_class,
        tags=['apkt']
    )
    def destroy(self, request, pk):
        apkt_trans_log = get_object_or_404(APKTTransLog, pk=pk)
        self.perform_destroy(apkt_trans_log)
        return response__(request, apkt_trans_log, 'apkt_trans_log.delete')

    def perform_destroy(self, instance):
        instance.delete()