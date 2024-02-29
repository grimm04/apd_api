from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransAsetMutasi
from .filters import TransAsetMutasiFilter, SearchFilter, TransAsetMutasi

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransAsetMutasiViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransAsetMutasi.objects.all()
    serializer_class = serializers.GetTransAsetMutasiSerializers
    create_serializer_class = serializers.CRTransAsetMutasiSerializers
    update_serializer_class = serializers.UDTransAsetMutasiSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransAsetMutasiFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['bobot_total_standar','bobot_total_hasil','level_pm','kesimpulan','status']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_aset_mutasi']

    @extend_schema(
        methods=["GET"],
        summary="Get Trans Aset Mutasi",
        description="Get Trans Aset Mutasi",
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

        return get_response(self, request, queryset, 'trans_aset_mutasi.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Trans Aset Mutasi.",
        description="Create Trans Aset Mutasi.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'trans_aset_mutasi.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Trans Aset Mutasi (Specified).",
        description="Get Trans Aset Mutasi (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_aset_mutasi = self.queryset.filter(id_wo=pk)
        if not trans_aset_mutasi:
            return not_found('trans_aset_mutasi.not_found')

        serializer = self.serializer_class(trans_aset_mutasi, many=True)
        return response__(request, serializer, 'trans_aset_mutasi.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Trans Aset Mutasi",
        description="Update Trans Aset Mutasi",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_aset_mutasi = get_object_or_404(TransAsetMutasi, pk=pk)
        serializer = self.update_serializer_class(instance=trans_aset_mutasi, data=request.data)

        return post_update_response(serializer, 'trans_aset_mutasi.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete trans.",
        description="Delete trans.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_aset_mutasi = get_object_or_404(TransAsetMutasi, pk=pk)
        self.perform_destroy(trans_aset_mutasi)
        return response__(request, trans_aset_mutasi, 'trans_aset_mutasi.delete')

    def perform_destroy(self, instance):
        instance.delete()
 