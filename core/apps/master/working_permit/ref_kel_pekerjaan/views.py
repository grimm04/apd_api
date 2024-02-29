from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import RefKelPekerjaan,EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, RefKelPekerjaanFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from rest_framework.decorators import action
from rest_framework import viewsets, response, status

class RefKelPekerjaanView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefKelPekerjaan.objects.all()
    serializer_class = serializers.RefKelPekerjaanSerializers
    create_serializer_class = serializers.CRRefKelPekerjaanSerializers
    update_serializer_class = serializers.UDRefKelPekerjaanSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefKelPekerjaanFilter
    filterset_fields = ['keyword']
    search_fields = ['name', 'alias']
    ordering_fields = '__all__'
    ordering = ['id_ref_kel_pekerjaan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Kelengkapan Pekerjaan.",
        description="Get Data Kelengkapan Pekerjaan.",
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
        title        = 'Kelengkapan Pekerjaan'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'ref_kel_pekerjaan.view',headers=header, relation=relation, fields=fields,title=title) 
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Kelengkapan Pekerjaan.",
        description="Create Data Kelengkapan Pekerjaan.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_working_permit']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'ref_kel_pekerjaan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Kelengkapan Pekerjaan",
        description="Get Details Kelengkapan Pekerjaan",
        tags=['master_working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_kel_pekerjaan = self.queryset.filter(id_ref_kel_pekerjaan=pk)
        if not ref_kel_pekerjaan:
            return not_found('ref_kel_pekerjaan.not_found')

        serializer = self.serializer_class(ref_kel_pekerjaan, many=True)
        return response__(request, serializer, 'ref_kel_pekerjaan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Kelengkapan Pekerjaan.",
        description="Update Data Kelengkapan Pekerjaan.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_working_permit']
    )
    def update(self, request, pk):
        ref_kel_pekerjaan = get_object_or_404(RefKelPekerjaan, pk=pk)
        serializer = self.update_serializer_class(instance=ref_kel_pekerjaan, data=request.data)
        return post_update_response(serializer, 'ref_kel_pekerjaan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Kelengkapan Pekerjaan.",
        description="Delete Data Kelengkapan Pekerjaan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def destroy(self, request, pk):
        ref_kel_pekerjaan = get_object_or_404(RefKelPekerjaan, pk=pk)
        self.perform_destroy(ref_kel_pekerjaan)
        return response__(request, ref_kel_pekerjaan, 'ref_kel_pekerjaan.delete')

    def perform_destroy(self, instance):
        instance.delete()
    

    @extend_schema(
        methods=["GET"],
        summary=" Get Data Kelengkapan Pekerjaan by kategori.",
        description=" Get Data Kelengkapan Pekerjaan by kategori. ",
        request=None,
        responses=None,
        tags=['master_working_permit']
    )
    @action(detail=False, methods=['GET'], url_path='kat', url_name='get_ref_pekerjaan_kategori') 
    def get_kel_pekerjaan_by_kategori(self, request, *args, **kwargs):  
        klasifikasi       = RefKelPekerjaan.objects.filter(kategori='klasifikasi') 
        prosedur  = RefKelPekerjaan.objects.filter(kategori='prosedur')
        lampiran  = RefKelPekerjaan.objects.filter(kategori='lampiran')

        k = self.serializer_class(klasifikasi, many=True)
        p = self.serializer_class(prosedur, many=True)
        l = self.serializer_class(lampiran, many=True)
        data = {
            0: k.data ,
            1: p.data,
            2: l.data,
        }
        # print(data)
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'Berhasi mendapatkan data ref kelengkapan pekerjaan by kategori',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK)
