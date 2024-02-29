from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefEpPetugas  
from .filters import SearchFilter, RefEpPetugasFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefEpPetugasViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefEpPetugas.objects.all()
    serializer_class = serializers.CRRefEpPetugasSerializers
    update_serializer_class = serializers.UDRefEpPetugasSerializers

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefEpPetugasFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama','jenis']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_ep_petugas']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Opsisdis - Ref Ep Petugas.",
        description="Create Master Data - Opsisdis - Ref Ep Petugas.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        

        return post_update_response(serializer, 'ref_ep_indikasi.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Ep Petugas.",
        description="Get Master Data - Opsisdis - Ref Ep Petugas.",
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
        queryset = self.filter_queryset(self.get_queryset()) 
        
        return get_response(self, request, queryset, 'ref_ep_indikasi.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Ep Petugas (Specified).",
        description="Get Master Data - Opsisdis - Ref Ep Petugas (Specified).",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_ep_indikasi = self.queryset.filter(pk=pk)
        if not ref_ep_indikasi :
            return not_found('ref_ep_indikasi.not_found')

        serializer = self.serializer_class(ref_ep_indikasi, many=True)
        return response__(request, serializer, 'ref_ep_indikasi.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Opsisdis - Ref Ep Petugas.",
        description="Update Master Data - Opsisdis - Ref Ep Petugas.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        ref_ep_indikasi = get_object_or_404(RefEpPetugas, pk=pk)
        serializer = self.update_serializer_class(instance=ref_ep_indikasi, data=request.data)

        return post_update_response(serializer, 'ref_ep_indikasi.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Opsisdis - Ref Ep Petugas.",
        description="Delete Master Data - Opsisdis - Ref Ep Petugas.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        ref_ep_indikasi = get_object_or_404(RefEpPetugas, pk=pk)
        self.perform_destroy(ref_ep_indikasi)
        return response__(request, ref_ep_indikasi, 'ref_ep_indikasi.delete')

    def perform_destroy(self, instance):
        instance.delete()
