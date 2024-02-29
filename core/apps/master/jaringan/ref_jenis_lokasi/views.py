from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefJenisLokasi
from .filters import SearchFilter, RefJenisLokasiFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


class RefJenisLokasiViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefJenisLokasi.objects.all()
    serializer_class = serializers.CRRefJenisLokasiSerializers
    update_serializer_class = serializers.UDRefJenisLokasiSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefJenisLokasiFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_jenis_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_jenis_lokasi']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Jaringan - Ref Jenis Lokasi.",
        description="Create Master Data - Jaringan - Ref Jenis Lokasi.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_jenis_lokasi.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Lokasi.",
        description="Get Master Data - Jaringan - Ref Jenis Lokasi.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_jenis_lokasi.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Lokasi (Specified).",
        description="Get Master Data - Jaringan - Ref Jenis Lokasi (Specified).",
        tags=['master_jaringan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_jenis_lokasi = self.queryset.filter(pk=pk)
        if not ref_jenis_lokasi :
            return not_found('ref_jenis_lokasi.not_found')

        serializer = self.serializer_class(ref_jenis_lokasi, many=True)
        return response__(request, serializer, 'ref_jenis_lokasi.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Jaringan - Ref Jenis Lokasi.",
        description="Update Master Data - Jaringan - Ref Jenis Lokasi.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_jaringan']
    )
    def update(self, request, pk):
        ref_jenis_lokasi = get_object_or_404(RefJenisLokasi, pk=pk)
        serializer = self.update_serializer_class(instance=ref_jenis_lokasi, data=request.data)

        return post_update_response(serializer, 'ref_jenis_lokasi.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Jaringan - Ref Jenis Lokasi.",
        description="Delete Master Data - Jaringan - Ref Jenis Lokasi.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def destroy(self, request, pk):
        ref_jenis_lokasi = get_object_or_404(RefJenisLokasi, pk=pk)
        self.perform_destroy(ref_jenis_lokasi)
        return response__(request, ref_jenis_lokasi, 'ref_jenis_lokasi.delete')

    def perform_destroy(self, instance):
        instance.delete()
