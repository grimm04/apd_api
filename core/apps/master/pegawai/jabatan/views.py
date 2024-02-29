from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Jabatan  , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, JabatanFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class JabatanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = Jabatan.objects.all()
    serializer_class = serializers.CRJabatanSerializers
    # update_serializer_class = serializers.UDJabatanSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = JabatanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_jabatan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Jabatan.",
        description="Get Data Jabatan.",
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
        title        = 'Jabatan'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'jabatan.view',headers=header, relation=relation, fields=fields,title=title)  

    @extend_schema(
        methods=["POST"],
        summary="Create Data Jabatan.",
        description="Create Data Jabatan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'jabatan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Jabatan",
        description="Get Details Jabatan",
        tags=['master_pegawai']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        jabatan = self.queryset.filter(id_jabatan=pk)
        if jabatan is None:
            return not_found('jabatan.not_found')

        serializer = self.serializer_class(jabatan, many=True)
        return response__(request, serializer, 'jabatan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Jabatan.",
        description="Update Data Jabatan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def update(self, request, pk):
        jabatan = get_object_or_404(Jabatan, pk=pk)
        serializer = self.serializer_class(instance=jabatan, data=request.data)

        return post_update_response(serializer, 'jabatan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Jabatan.",
        description="Delete Data Jabatan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def destroy(self, request, pk):
        jabatan = get_object_or_404(Jabatan, pk=pk)
        self.perform_destroy(jabatan)
        return response__(request, jabatan, 'jabatan.delete')

    def perform_destroy(self, instance):
        instance.delete()
