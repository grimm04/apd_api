from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import RefKelKeselamatan,EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, RefKelKeselamatanFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from rest_framework.decorators import action
from rest_framework import viewsets, response, status

class RefKelKeselamatanView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefKelKeselamatan.objects.all()
    serializer_class = serializers.RefKelKeselamatanSerializers
    create_serializer_class = serializers.CRRefKelKeselamatanSerializers
    update_serializer_class = serializers.UDRefKelKeselamatanSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefKelKeselamatanFilter
    filterset_fields = ['keyword']
    search_fields = ['name', 'alias']
    ordering_fields = '__all__'
    ordering = ['id_ref_kel_keselamatan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Kelengkapan Keselamatan.",
        description="Get Data Kelengkapan Keselamatan.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Kelengkapan Keselamatan'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'ref_kel_keselamatan.view',headers=header, relation=relation, fields=fields,title=title) 
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Kelengkapan Keselamatan.",
        description="Create Data Kelengkapan Keselamatan.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_working_permit']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'ref_kel_keselamatan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Kelengkapan Keselamatan",
        description="Get Details Kelengkapan Keselamatan",
        tags=['master_working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_kel_keselamatan = self.queryset.filter(id_ref_kel_keselamatan=pk)
        if not ref_kel_keselamatan:
            return not_found('ref_kel_keselamatan.not_found')

        serializer = self.serializer_class(ref_kel_keselamatan, many=True)
        return response__(request, serializer, 'ref_kel_keselamatan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Kelengkapan Keselamatan.",
        description="Update Data Kelengkapan Keselamatan.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_working_permit']
    )
    def update(self, request, pk):
        ref_kel_keselamatan = get_object_or_404(RefKelKeselamatan, pk=pk)
        serializer = self.update_serializer_class(instance=ref_kel_keselamatan, data=request.data)
        return post_update_response(serializer, 'ref_kel_keselamatan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Kelengkapan Keselamatan.",
        description="Delete Data Kelengkapan Keselamatan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def destroy(self, request, pk):
        ref_kel_keselamatan = get_object_or_404(RefKelKeselamatan, pk=pk)
        self.perform_destroy(ref_kel_keselamatan)
        return response__(request, ref_kel_keselamatan, 'ref_kel_keselamatan.delete')

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(
        methods=["GET"],
        summary=" Get Data Kelengkapan Keselamatan by kategori.",
        description=" Get Data Kelengkapan Keselamatan by kategori. ",
        request=None,
        responses=None,
        tags=['master_working_permit']
    )
    @action(detail=False, methods=['GET'], url_path='kat', url_name='get_ref_keselamat_kategori') 
    def get_kel_keselamatan_by_kategori(self, request, *args, **kwargs):  
        pelindung       = RefKelKeselamatan.objects.filter(kategori='pelindung')
        perlengkapan  = RefKelKeselamatan.objects.filter(kategori='perlengkapan')
 
        p1 = self.serializer_class(pelindung, many=True)
        p2 = self.serializer_class(perlengkapan, many=True)
        data = {0: p1.data, 1: p2.data}
        # print(data)
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'Berhasi mendapatkan data ref kelengkapan keselamatan by kategori',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK)