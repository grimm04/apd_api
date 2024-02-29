from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from numpy import equal
from django.db import connection
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefLokasi
from . import filters

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination

from django.http import QueryDict

class RefLokasiViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.all()
    serializer_class = serializers.RefLokasiSerializer
    create_serializer_class = serializers.CRRefLokasiSerializers
    update_serializer_class = serializers.UDRefLokasiSerializers 

    pagination_class = CustomPagination

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Jaringan.",
        description="Create Master Data - Jaringan.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_jaringan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'ref_lokasi.create')

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = filters.RefLokasiFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi','jenis_trafo','kode_lokasi','jenis_layanan','fungsi_scada','pemilik','jenis_gi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan.",
        description="Get Master Data - Jaringan.",
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
        # id_ref_jenis_lokasi = request.GET.get('id_ref_jenis_lokasi')
        # print(id_ref_jenis_lokasi)
        # if id_ref_jenis_lokasi == '11': 
        #     id_ref_lokasi = id_ref_lokasi.strip()
        #     id_ref_lokasi = id_ref_lokasi.split(',')
        #     # q_set = self.get_queryset().filter(id_parent_lokasi__isnull=True).filter(id_ref_lokasi__in=id_ref_lokasi)\
        #     #     .filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')
        #     q_set = self.get_queryset().filter(id_ref_lokasi__in=id_ref_lokasi)\
        #         .filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')

        #     final_tree = list()
        #     for ref_lokasi_tree in q_set:
        #         final_tree.append(self.get_tree(ref_lokasi_tree))

        #     return response_basic(_status=True, results=final_tree, msg='ref_lokasi.view')
        
        queryset = self.filter_queryset(self.get_queryset()) 
        return get_response(self, request, queryset, 'ref_lokasi.view') 

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan (Specified).",
        description="Get Master Data - Jaringan (Specified).",
        tags=['master_jaringan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_lokasi = self.queryset.filter(pk=pk)
        if not ref_lokasi:
            return not_found('ref_lokasi.not_found')

        serializer = self.serializer_class(ref_lokasi, many=True)
        return response__(request, serializer, 'ref_lokasi.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Jaringan.",
        description="Update Master Data - Jaringan.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_jaringan']
    )
    def update(self, request, pk):
        ref_lokasi = get_object_or_404(RefLokasi, pk=pk)
        serializer = self.update_serializer_class(instance=ref_lokasi, data=request.data)

        return post_update_response(serializer, 'ref_lokasi.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Jaringan.",
        description="Delete Master Data - Jaringan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def destroy(self, request, pk):
        ref_lokasi = get_object_or_404(RefLokasi, pk=pk) 

        cursor = connection.cursor()
        cursor.execute('DELETE FROM ref_lokasi WHERE id_ref_lokasi = %s', [pk])
        connection.commit()
 
        # self.perform_destroy(ref_lokasi)
        return response__(request, ref_lokasi, 'ref_lokasi.delete')

    def perform_destroy(self, instance):
        instance.delete()


class UnitPembangkitViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.all()
    serializer_class = serializers.UnitPembangkitSerializer 

    pagination_class = CustomPagination 

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = filters.UnitPembangkitFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi', 'kode_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi']

    def get_queryset(self): 
        qs = RefLokasi.objects.filter(id_ref_jenis_lokasi=1)
        return qs

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Unit Pembangkit.",
        description="Get Master Data - Jaringan - Unit Pembangkit.",
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

        return get_response(self, request, queryset, 'ref_lokasi.view')

class PembangkitViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.all()
    serializer_class = serializers.PembangkitSerializer 

    pagination_class = CustomPagination 

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = filters.PembangkitFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi', 'kode_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi']

    def get_queryset(self): 
        qs = RefLokasi.objects.filter(id_ref_jenis_lokasi=2)
        return qs

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Unit Pembangkit.",
        description="Get Master Data - Jaringan - Unit Pembangkit.",
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

        return get_response(self, request, queryset, 'ref_lokasi.view')

class GIViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.all()
    serializer_class = serializers.GISerializer 

    pagination_class = CustomPagination 

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = filters.GIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi', 'kode_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi']

    def get_queryset(self): 
        qs = RefLokasi.objects.filter(id_ref_jenis_lokasi=4)
        return qs

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan -  GI.",
        description="Get Master Data - Jaringan -  GI.",
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

        return get_response(self, request, queryset, 'ref_lokasi.view')