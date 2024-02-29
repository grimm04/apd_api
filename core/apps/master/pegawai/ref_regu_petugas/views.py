from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import REF_REGU_PETUGAS_MODELS  , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, REF_REGU_PETUGASFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class REF_REGU_PETUGAS_MODELSViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = REF_REGU_PETUGAS_MODELS.objects.all()
    serializer_class = serializers.REF_REGU_PETUGASSerializers
    # update_serializer_class = serializers.UDREF_REGU_PETUGAS_MODELSSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = REF_REGU_PETUGASFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_regu_petugas']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Regu Petugas.",
        description="Get Data Regu Petugas.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'ref_regu_petugas'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'ref_regu_petugas.view',headers=header, relation=relation, fields=fields,title=title)  

    @extend_schema(
        methods=["POST"],
        summary="Create Data Regu Petugas.",
        description="Create Data Regu Petugas.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_regu_petugas.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Regu Petugas",
        description="Get Details Regu Petugas",
        tags=['master_pegawai']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_regu_petugas = self.queryset.filter(id_ref_regu_petugas=pk)
        if ref_regu_petugas is None:
            return not_found('ref_regu_petugas.not_found')

        serializer = self.serializer_class(ref_regu_petugas, many=True)
        return response__(request, serializer, 'ref_regu_petugas.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Regu Petugas.",
        description="Update Data Regu Petugas.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def update(self, request, pk):
        ref_regu_petugas = get_object_or_404(REF_REGU_PETUGAS_MODELS, pk=pk)
        serializer = self.serializer_class(instance=ref_regu_petugas, data=request.data)

        return post_update_response(serializer, 'ref_regu_petugas.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Regu Petugas.",
        description="Delete Data Regu Petugas.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def destroy(self, request, pk):
        ref_regu_petugas = get_object_or_404(REF_REGU_PETUGAS_MODELS, pk=pk)
        self.perform_destroy(ref_regu_petugas)
        return response__(request, ref_regu_petugas, 'ref_regu_petugas.delete')

    def perform_destroy(self, instance):
        instance.delete()
