from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from library.date_converter import date_converter_dt

from .models import KinerjaRC, EXPORT_FIELDS, EXPORT_HEADERS, EXPORT_RELATION_FIELD
from . import serializers
from .filters import SearchFilter, KinerjaRCFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection
from rest_framework import response, status


# Create your views here.
class KinerjaRCView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.KinerjaRCSerializer

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = KinerjaRCFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['']

    @extend_schema(
        methods=["GET"],
        summary="DATA KINERJA RC",
        description="FASOP - LAPORAN SCADA - KINERJA RC",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
            OpenApiParameter(name='harian', description='Format Tanggal 2022-01-29', required=False, type=str, default=None),
            OpenApiParameter(name='bulanan', description='Format Tanggal : 05-2022', required=False, type=str, default=None),
            OpenApiParameter(name='path1', description='Filter Path1', required=False, type=str, default=None),
            OpenApiParameter(name='path3', description='Filter Path3', required=False, type=str, default=None),

        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['FASOP LAPORAN SCADA']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'DATA KINERJA RC'

       
        cur = connection.cursor()

        sql = "SELECT path1, path2, path3, path4, count(*) as jlm_rc, "
        sql =  sql + "SUM((CASE WHEN status_2 = 'BERHASIL' THEN 1 ELSE 0 END)) AS berhasil, "
        sql =  sql + "SUM((CASE WHEN status_2 = 'GAGAL' THEN 1 ELSE 0 END)) AS gagal "
        sql =  sql + "FROM scd_his_rc   WHERE datum_2 IS NOT NULL AND cek_remote=1 "

        if request.GET.get('harian') != None:
            datum_harian_start = date_converter_dt(date=request.GET.get('harian'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=request.GET.get('harian'),time='23:59:00')
            sql =  sql + " AND datum_2 >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND datum_2 <= CONVERT(datetime, '" + str(datum_harian_end) + "',120)"
        if request.GET.get('bulanan') != None:
            bln_thn = request.GET.get('bulanan')
            x = bln_thn.split("-")
            sql =  sql + " AND MONTH(datum_2) = '"+str(x[0])+"' AND YEAR(datum_2) = '"+str(x[1])+"'"
       
        if request.GET.get('path1') != None:
            sql =  sql + " AND path1 like '%"+ str(request.GET.get('path1')) +"%' "
        if request.GET.get('path3') != None:
            sql =  sql + " AND path3 like '%"+ str(request.GET.get('path3')) +"%' "
        
        sql = sql + "GROUP BY path1, path2, path3, path4  "
        sql = sql + "ORDER BY path1, path2, path3, path4 asc "

        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            if int(row[4]) > 0 :
                performance = round(row[5] / (row[4]) * 100,2)
            else:
                performance = '-'

            datas = {
                'path1' : row[0],
                'path2' : row[1],
                'path3' : row[2],
                'path4' : row[3],
                'jlm_rc' :  row[4],
                'sukses' :  row[5],
                'gagal' :  row[6],
                'performance' : performance,
            }
            
            data.append(datas)
        
        return get_response(self, request, data, 'kinerja_rc.view',headers=header, relation=relation, fields=fields,title=title)  