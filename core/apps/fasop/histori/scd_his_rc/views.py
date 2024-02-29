 
from array import ArrayType, array
from audioop import add
from datetime import datetime
from multiprocessing.dummy import Array
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import SCD_HIS_RC , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, SCD_HIS_RCFilter

from base.response import  get_response
from base.custom_pagination import CustomPagination
from django.db.models import Count, Sum, Case, When, Q
from library.date_converter import date_converter_dt ,date_converter_str

from django.db import connection


# Create your views here.
class SCD_HIS_RCViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    
    serializer_class = serializers.SCD_HIS_RCSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SCD_HIS_RCFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = ['path1','path2','path3','b1','b3','status_1','elem']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_his_rc']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - Spectrum - Histori RC",
        description="Get Data Fasop - Spectrum - Histori RC",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),

            OpenApiParameter(name='datum_harian', description='Format Tanggal : 2022-05-11',required=False, type=str),
            OpenApiParameter(name='datum_bulanan', description='Format Tanggal : 05-2022',required=False, type=str),
            OpenApiParameter(name='b1', description='Value B1',required=False, type=str),
            OpenApiParameter(name='b3', description='Value B3',required=False, type=str),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['fasop_spectrum_his']
    )
    def list(self, request, *args, **kwargs):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'His RC'
        addsql = ''

        

        cur = connection.cursor()
        sql = "SELECT b.path1, b.path2, b.path3, b.elem, count(*) AS remote, "
        sql = sql + "SUM((CASE WHEN b.status_2 = 'BERHASIL' THEN 1 ELSE 0 END)) AS berhasil, "
        sql = sql + "SUM((CASE WHEN b.status_2 = 'GAGAL' THEN 1 ELSE 0 END)) AS gagal "
        sql = sql + "FROM scd_his_rc b  WHERE b.datum_2 IS NOT NULL AND b.cek_remote=1 "

        if request.GET.get('datum_harian') != None:
            datum_harian_start = date_converter_dt(date=request.GET.get('datum_harian'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=request.GET.get('datum_harian'),time='23:59:00')
            addsql =  addsql + " AND b.datum_1 >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND b.datum_1 <= CONVERT(datetime, '" + str(datum_harian_end) + "',120)"
        
        if request.GET.get('datum_bulanan') != None:
            bln_thn = request.GET.get('datum_bulanan')
            x = bln_thn.split("-")
            addsql =  addsql + " AND MONTH(b.datum_1) = '"+str(x[0])+"' AND YEAR(b.datum_1) = '"+str(x[1])+"'"
 
        if request.GET.get('b1') != None:
            addsql =  addsql + " AND b.b1 like '%"+ str(request.GET.get('b1')) +"%'"
        if request.GET.get('b3') != None:
            addsql =  addsql + " AND b.b3 like '%"+ str(request.GET.get('b3')) +"%'"
        
        sql = sql + addsql

        sql = sql + "GROUP BY b.path1, b.path2, b.path3, b.elem "
        sql = sql + "ORDER BY b.path1, b.path2, b.path3, b.elem "

        print(sql)
        cur.execute(sql)  
        rs = cur.fetchall()

        data = []
        for course in rs:
            print(course)
            if int(course[4]):
                print('disini')
                kinerja = round(course[5] / course[6] * 100,2)
            else:
                kinerja = '-'
                print('disana')
            datas = {
                'path1' : course[0],
                'path2' : course[1],
                'path3' : course[2],
                'elem' : course[3],
                'remote' : course[4],
                'berhasil' : course[5],
                'gagal' : course[6],
                'kinerja' : kinerja,

            }

            data.append(datas)
        return get_response(self, request, data, 'scd_his_rc.view',headers=header, relation=relation, fields=fields,title=title) 
        
         
  