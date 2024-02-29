from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import action

from . import serializers
from .models import TransJadwalHar ,EXPORT_HEADERS,EXPORT_HEADERS_CAPTION,EXPORT_FIELDS,EXPORT_RELATION_FIELD 
from .filters import TransJadwalHarFilter, SearchFilter, TransJadwalHar

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 
from base.negotiation import CustomContentNegotiation


class TransJadwalHarViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransJadwalHar.objects.all()
    serializer_class = serializers.TransJadwalHarSerializers
    create_serializer_class = serializers.CRTransJadwalHarSerializers
    update_serializer_class = serializers.UDTransJadwalHarSerializers
    update_status_serializer_class = serializers.UDStatusTransJadwalHarSerializers
    content_negotiation_class = CustomContentNegotiation

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransJadwalHarFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nomor','pelaksana','pelaksana_pek','pengawas','status_pekerjaan','id_gardu_induk_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_jadwal_har']

    @extend_schema( 
        methods=["GET"],
        summary="Get Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        description="Get Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def list(self, request):
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        header_caption = EXPORT_HEADERS_CAPTION

        fields = EXPORT_FIELDS
        title = 'Laporan Jadwal Pemeliharaan - Input Jadwal'
        queryset = self.filter_queryset(self.get_queryset())   
 
        return get_response(self, request, queryset, 'trans_jadwal_har.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption)  


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        description="Create Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_jadwal_har.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan (Specified).",
        description="Get Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_jadwal_har = self.queryset.filter(id_trans_jadwal_har=pk)
        if not trans_jadwal_har:
            return not_found('trans_jadwal_har.not_found')

        serializer = self.serializer_class(trans_jadwal_har, many=True)
        return response__(request, serializer, 'trans_jadwal_har.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        description="Update Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_jadwal_har = get_object_or_404(TransJadwalHar, pk=pk)
        serializer = self.update_serializer_class(instance=trans_jadwal_har, data=request.data)

        return post_update_response(serializer, 'trans_jadwal_har.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        description="Delete Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_jadwal_har = get_object_or_404(TransJadwalHar, pk=pk)
        self.perform_destroy(trans_jadwal_har)
        return response__(request, trans_jadwal_har, 'trans_jadwal_har.delete')

    def perform_destroy(self, instance):
        instance.delete()
 
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan Status Update",
        description="Update Opsisdis - Jadwal Pemeliharaan - Usulan Pemeliharaan Status Update",
        request=update_status_serializer_class,
        responses=update_status_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    @action(detail=False, methods=['PUT'], url_path='status/(?P<id_trans_jadwal_har>\d+)', url_name='update-status')
    def update_status(self, request, id_trans_jadwal_har):
        trans_jadwal_har = get_object_or_404(TransJadwalHar, pk=id_trans_jadwal_har)
        serializer = self.update_status_serializer_class(instance=trans_jadwal_har, data=request.data)
        return post_update_response(serializer, 'trans_jadwal_har.update') 
