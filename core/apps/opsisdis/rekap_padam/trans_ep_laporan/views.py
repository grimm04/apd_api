from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransEpLaporan
from .filters import TransEpLaporanFilter, SearchFilter, TransEpLaporan

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransEpLaporanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransEpLaporan.objects.all()
    serializer_class = serializers.TransEpLaporanSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransEpLaporanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['tegangan','status_s','status_g']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_ep_laporan']

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Laporan",
        description="Get Opsisdis - Rekap Padam - Trans Ep Laporan",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_ep_laporan.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Rekap Padam - Trans Ep Laporan",
        description="Create Opsisdis - Rekap Padam - Trans Ep Laporan",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_ep_laporan.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Laporan (Specified).",
        description="Get Opsisdis - Rekap Padam - Trans Ep Laporan (Specified).",
        tags=['opsisdis_rekap_padam']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_ep_laporan = self.queryset.filter(id_trans_ep_laporan=pk)
        if not trans_ep_laporan:
            return not_found('trans_ep_laporan.not_found')

        serializer = self.serializer_class(trans_ep_laporan, many=True)
        return response__(request, serializer, 'trans_ep_laporan.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Opsisdis -  Trans Ep Laporan",
        description="Update Opsisdis - Opsisdis -  Trans Ep Laporan",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def update(self, request, pk):
        trans_ep_laporan = get_object_or_404(TransEpLaporan, pk=pk)
        serializer = self.serializer_class(instance=trans_ep_laporan, data=request.data)

        return post_update_response(serializer, 'trans_ep_laporan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Rekap Padam - Trans Ep Laporan",
        description="Delete Opsisdis - Rekap Padam - Trans Ep Laporan",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def destroy(self, request, pk):
        trans_ep_laporan = get_object_or_404(TransEpLaporan, pk=pk)
        self.perform_destroy(trans_ep_laporan)
        return response__(request, trans_ep_laporan, 'trans_ep_laporan.delete')

    def perform_destroy(self, instance):
        instance.delete()