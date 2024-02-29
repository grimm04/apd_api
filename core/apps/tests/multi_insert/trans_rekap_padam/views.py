
import re
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response ,status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication 

from apps.tests.multi_insert.trans_rekap_padam_section.models import TransRekapPadamSection

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransRekapPadam
from .filters import TransRekapPadamFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,validate_serializer,error_response,response_json
from base.custom_pagination import CustomPagination 
from django.db.models import Q

from apps.tests.multi_insert.trans_rekap_padam_section.serializers import RekapPadamPeralatanSerializer

class TransRekapPadamViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransRekapPadam.objects.all()
    serializer_class = serializers.TransRekapSerializer 
    post_serializer_class = serializers.PostCustomNonModel 
    create_rekap_section_serializer_class = RekapPadamPeralatanSerializer 
    create_serializer_class = serializers.TransRekapSerializer  
    update_serializer_class = serializers.TransRekapSerializer  

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransRekapPadamFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['no_apkt']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_rekap_padam']

    @extend_schema(
        methods=["GET"],
        summary="Get Test Enpoint - Trans Rekap Padam Test.",
        description="Get Test Enpoint - Trans Rekap Padam Test.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['tests']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_rekap_padam_test.view')


    @extend_schema(
        methods=["POST"],
        summary="Test Enpoint - Trans Rekap Padam Test.",
        description="Test Enpoint - Trans Rekap Padam Test Single or Batch, Can Be Multiple create.",
        request=post_serializer_class,
        responses=create_serializer_class,
        tags=['tests']
    )
    # create
    def create(self, request):
        data = request.data  
        # print(data)

        #validasi data post awal tidak untuk di save, sesuaikan dengan kondisi masing2
        serializer = self.post_serializer_class(data=data, many=False)  
        data_serialized = validate_serializer(serializer, s=False)  
        # check jika terjadi error saat validasi data
        if data_serialized.get('error') == True: 
            return error_response(data_serialized.get('data'))  
        
        #redeclare varible data serialized
        data_serialized = data_serialized.get('data')
        # print(data_serialized)

        #dict rekap padam
        rekap_padam = dict({
            'no_event': data_serialized.get('no_event'),
            'no_apkt': data_serialized.get('no_apkt'),
            'r': data_serialized.get('r'),
            's': data_serialized.get('s'),
            't': data_serialized.get('s'),
            'n': data_serialized.get('n'),
            'jam_padam': data_serialized.get('jam_padam'),
            'buka': data_serialized.get('buka'),
            # dan seterusnya....
        })
        #1 proses save rekap padam (tbl 1) 
        rekap_padam_serializer = self.create_serializer_class(data=rekap_padam, many=False) 
        data_rekap_padam_serialized = validate_serializer(rekap_padam_serializer, s=True)  
        # print(data_rekap_padam_serialized)
        # check jika terjadi error saat validasi data
        if data_rekap_padam_serialized.get('error') == True: 
            return error_response(data_rekap_padam_serialized.get('data'))  
        
        #buat variable rekap_padam
        data_rekap_padam = data_rekap_padam_serialized.get('data')
        # print(data_rekap_padam)
        
        #2 Proses Input Ke 2 dn seterusnya(misal rekap_padam_peralatan) 
        #contoh query get filter(custom)
        id_trans_rekap_padam = data_rekap_padam.get('id_trans_rekap_padam')
        #source https://docs.djangoproject.com/en/3.2/topics/db/sql/#performing-raw-sql-queries
        # get_rekap_section = TransRekapPadamSection.objects.raw("SELECT id_trans_rekap_padam_section,jam_masuk - jam_sebelum AS durasi, beban_sebelum as beban_sebelum FROM trans_rekap_padam_section where id_trans_rekap_padam='%s' AND section !='%s'" %(1,str('normal')))
       
      
        # contoh query orm 
        # https://docs.djangoproject.com/en/4.0/ref/models/querysets/
        # get_rekap_section = TransRekapPadamSection.objects.filter(id_trans_rekap_padam=1).order_by('id_trans_rekap_padam_section')
        # print(get_rekap_section)
        # for p in get_rekap_section:
        #     print(p.durasi)

        # #dict rekap padam section
        rekap_section = dict({
            'id_trans_rekap_padam': id_trans_rekap_padam,
            #data bisa ambil dari post atau custom query(example)
            'ens': 0.2, 
        })

        #example save rekap section
        rekap_section_serializer = self.create_rekap_section_serializer_class(data=rekap_section, many=False) 
        data_rekap_section_serialized = validate_serializer(rekap_section_serializer, s=True)  
        # print(data_rekap_section_serialized)
        # check jika terjadi error saat validasi data
        if data_rekap_section_serialized.get('error') == True: 
            return error_response(data_rekap_section_serialized.get('data'))  
 
        # return []

        #example method update rekap padam
        pk = id_trans_rekap_padam
        #cari data sesuai pk di tbl TransRekapPadam
        trans_rekap_padam_id = get_object_or_404(TransRekapPadam, pk=pk)
        serializer = self.update_serializer_class(instance=trans_rekap_padam_id, data=data_rekap_padam)
        data_json = validate_serializer(serializer, s=True)  

        if data_json.get('error') == True: 
            return error_response(data_json.get('data'))  

        
        #bisa multi save tambahkan sesuai kebutuhan
        
        #masukan data mana yg mau di tampilkan  
        # custom = dict ({
            # 'test':'''
        # })
        return response_json(data = data_json.get('data'), msg ='trans_rekap_padam_test.create')




        # print(rekap_padam)

        # return rekap_padam

    @extend_schema(
        methods=["GET"],
        summary="Get Test Enpoint - Trans Rekap Padam Test (Specified).",
        description="Get Test Enpoint - Trans Rekap Padam Test (Specified).",
        tags=['tests']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_rekap_padam_test = self.queryset.filter(trans_rekap_padam=pk)
        if not trans_rekap_padam_test:
            return not_found('trans_rekap_padam_test.not_found')

        serializer = self.serializer_class(trans_rekap_padam_test, many=True)
        return response__(request, serializer, 'trans_rekap_padam_test.view')
    
    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Test Enpoint - Trans Rekap Padam Test",
    #     description="Update Test Enpoint - Trans Rekap Padam Test",
    #     request=update_serializer_class,
    #     responses=update_serializer_class,
    #     tags=['tests']
    # )
    # def update(self, request, pk):
    #     trans_rekap_padam_test = get_object_or_404(trans_rekap_padam_test, pk=pk)
    #     serializer = self.update_serializer_class(instance=trans_rekap_padam_test, data=request.data)

    #     return post_update_response(serializer, 'trans_rekap_padam_test.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Test Enpoint - Trans Rekap Padam Test.",
        description="Delete Test Enpoint - Trans Rekap Padam Test.",
        request=serializer_class,
        responses=serializer_class,
        tags=['tests']
    )
    def destroy(self, request, pk):
        trans_rekap_padam_test = get_object_or_404(trans_rekap_padam_test, pk=pk)
        self.perform_destroy(trans_rekap_padam_test)
        return response__(request, trans_rekap_padam_test, 'trans_rekap_padam_test.delete')

    def perform_destroy(self, instance):
        instance.delete()  
     
     