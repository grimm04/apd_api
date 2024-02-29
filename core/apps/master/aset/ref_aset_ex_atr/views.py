from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefAsetExAtr
from .filters import RefAsetExAtrFilter, SearchFilter, RefAsetExAtr

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class RefAsetExAtrViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefAsetExAtr.objects.all()
    serializer_class = serializers.CDRefAsetExAtrSerializers 
    update_serializer_class = serializers.UDRefAsetExAtrSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefAsetExAtrFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama','status','satuan']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_aset_ex_atr']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Aset - Ref Aset Ex Atr.",
        description="Get Master Data - Aset - Ref Aset Ex Atr.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_aset_ex_atr.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Aset - Ref Aset Ex Atr.",
        description="Create Master Data - Aset - Ref Aset Ex Atr.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_aset_ex_atr.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Aset - Ref Aset Ex Atr (Specified).",
        description="Get Master Data - Aset - Ref Aset Ex Atr (Specified).",
        tags=['master_aset']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_aset_ex_atr = self.queryset.filter(id_ref_aset_ex_atr=pk)
        if not ref_aset_ex_atr:
            return not_found('ref_aset_ex_atr.not_found')

        serializer = self.serializer_class(ref_aset_ex_atr, many=True)
        return response__(request, serializer, 'ref_aset_ex_atr.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Aset - Ref Aset Doc",
        description="Update Master Data - Aset - Ref Aset Doc",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_aset']
    )
    def update(self, request, pk):
        ref_aset_ex_atr = get_object_or_404(RefAsetExAtr, pk=pk)
        serializer = self.update_serializer_class(instance=ref_aset_ex_atr, data=request.data)

        return post_update_response(serializer, 'ref_aset_ex_atr.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Aset - Ref Aset Ex Atr.",
        description="Delete Master Data - Aset - Ref Aset Ex Atr.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    def destroy(self, request, pk):
        ref_aset_ex_atr = get_object_or_404(RefAsetExAtr, pk=pk)
        self.perform_destroy(ref_aset_ex_atr)
        return response__(request, ref_aset_ex_atr, 'ref_aset_ex_atr.delete')

    def perform_destroy(self, instance):
        instance.delete()