from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefPemilikJaringan  
from .filters import SearchFilter, RefPemilikJaringanFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefPemilikJaringanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefPemilikJaringan.objects.all()
    serializer_class = serializers.CRRefPemilikJaringanSerializers
    update_serializer_class = serializers.UDRefPemilikJaringanSerializers

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefPemilikJaringanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_pemilik_jaringan']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Jaringan - Ref Pemilik Jaringan.",
        description="Create Master Data - Jaringan - Ref Pemilik Jaringan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        

        return post_update_response(serializer, 'ref_melilik_jaringan.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Pemilik Jaringan.",
        description="Get Master Data - Jaringan - Ref Pemilik Jaringan.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()) 
        
        return get_response(self, request, queryset, 'ref_melilik_jaringan.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Lokasi (Specified).",
        description="Get Master Data - Jaringan - Ref Jenis Lokasi (Specified).",
        tags=['master_jaringan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_melilik_jaringan = self.queryset.filter(pk=pk)
        if not ref_melilik_jaringan :
            return not_found('ref_melilik_jaringan.not_found')

        serializer = self.serializer_class(ref_melilik_jaringan, many=True)
        return response__(request, serializer, 'ref_melilik_jaringan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Jaringan - Ref Pemilik Jaringan.",
        description="Update Master Data - Jaringan - Ref Pemilik Jaringan.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_jaringan']
    )
    def update(self, request, pk):
        ref_melilik_jaringan = get_object_or_404(RefPemilikJaringan, pk=pk)
        serializer = self.update_serializer_class(instance=ref_melilik_jaringan, data=request.data)

        return post_update_response(serializer, 'ref_melilik_jaringan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Jaringan - Ref Pemilik Jaringan.",
        description="Delete Master Data - Jaringan - Ref Pemilik Jaringan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def destroy(self, request, pk):
        ref_melilik_jaringan = get_object_or_404(RefPemilikJaringan, pk=pk)
        self.perform_destroy(ref_melilik_jaringan)
        return response__(request, ref_melilik_jaringan, 'ref_melilik_jaringan.delete')

    def perform_destroy(self, instance):
        instance.delete()
