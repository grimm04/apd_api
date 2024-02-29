from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefLokasiGD
from .filters import SearchFilter, RefLokasiGDFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination

class RefLokasiGDViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasiGD.objects.all()
    serializer_class = serializers.RefLokasiGDSerializer 
    create_serializer_class = serializers.CRRefLokasiGDSerializers
    update_serializer_class = serializers.UDRefLokasiGDSerializers

    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = RefLokasiGDFilter
    filterset_fields = []  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi_gd']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Jaringan - Ref Jenis Lokasi GD.",
        description="Create Master Data - Jaringan - Ref Jenis Lokasi GD.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_jaringan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'ref_lokasi_gd.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Lokasi GD.",
        description="Get Master Data - Jaringan - Ref Jenis Lokasi GD.",
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

        return get_response(self, request, queryset, 'ref_lokasi_gd.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Lokasi GD (Specified).",
        description="Get Master Data - Jaringan - Ref Jenis Lokasi GD (Specified).",
        tags=['master_jaringan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_lokasi_gd = self.queryset.filter(pk=pk) 
        if not ref_lokasi_gd :
            return not_found('ref_lokasi_gd.not_found') 

        serializer = self.serializer_class(ref_lokasi_gd, many=True)
        return response__(request, serializer, 'ref_lokasi_gd.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Jaringan - Ref Jenis Lokasi GD.",
        description="Update Master Data - Jaringan - Ref Jenis Lokasi GD.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_jaringan']
    )
    def update(self, request, pk):
        ref_lokasi_gd = get_object_or_404(RefLokasiGD, pk=pk)
        serializer = self.update_serializer_class(instance=ref_lokasi_gd, data=request.data)

        return post_update_response(serializer, 'ref_lokasi_gd.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Jaringan - Ref Jenis Lokasi GD.",
        description="Delete Master Data - Jaringan - Ref Jenis Lokasi GD.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def destroy(self, request, pk):
        ref_lokasi_gd = get_object_or_404(RefLokasiGD, pk=pk)
        self.perform_destroy(ref_lokasi_gd)
        return response__(request, ref_lokasi_gd, 'ref_lokasi_gd.delete')

    def perform_destroy(self, instance):
        instance.delete()