from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransJadwalHarDok
from .filters import TransJadwalHarDokFilter, SearchFilter, TransJadwalHarDok

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransJadwalHarDokViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransJadwalHarDok.objects.all()
    serializer_class = serializers.TransJadwalHarDokSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransJadwalHarDokFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_dok']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_jadwal_har_dok']

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Jadwal Pemeliharaan - Jadwal Har Dok",
        description="Get Opsisdis - Jadwal Pemeliharaan - Jadwal Har Dok",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_jadwal_har_dok.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Jadwal Pemeliharaan - Jadwal Har Dok",
        description="Create Opsisdis - Jadwal Pemeliharaan - Jadwal Har Dok",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_jadwal_har_dok.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Jadwal Pemeliharaan - Ref Jenis Pekerjaan (Specified).",
        description="Get Opsisdis - Jadwal Pemeliharaan - Ref Jenis Pekerjaan (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_jadwal_har_dok = self.queryset.filter(id_trans_jadwal_har_dok=pk)
        if not trans_jadwal_har_dok:
            return not_found('trans_jadwal_har_dok.not_found')

        serializer = self.serializer_class(trans_jadwal_har_dok, many=True)
        return response__(request, serializer, 'trans_jadwal_har_dok.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Opsisdis -  Jadwal Har Dok",
        description="Update Opsisdis - Opsisdis -  Jadwal Har Dok",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_jadwal_har_dok = get_object_or_404(TransJadwalHarDok, pk=pk)
        serializer = self.serializer_class(instance=trans_jadwal_har_dok, data=request.data)

        return post_update_response(serializer, 'trans_jadwal_har_dok.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Jadwal Pemeliharaan - Jadwal Har Dok",
        description="Delete Opsisdis - Jadwal Pemeliharaan - Jadwal Har Dok",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_jadwal_har_dok = get_object_or_404(TransJadwalHarDok, pk=pk)
        self.perform_destroy(trans_jadwal_har_dok)
        return response__(request, trans_jadwal_har_dok, 'trans_jadwal_har_dok.delete')

    def perform_destroy(self, instance):
        instance.delete()