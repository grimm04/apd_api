from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from library.date_converter import date_converter_dt

from .models import KinerjaPeralatanScd, EXPORT_FIELDS, EXPORT_HEADERS, EXPORT_RELATION_FIELD
from . import serializers
from .filters import SearchFilter, KinerjaPeralatanScdFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection
from rest_framework import response, status


# Create your views here.
class KinerjaPeraltanScdView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.KinerjaPeralatanScdSerializer

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = KinerjaPeralatanScdFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['']

    @extend_schema(
        methods=["GET"],
        summary="DATA KINERJA PERALATAN SCADA",
        description="FASOP - LAPORAN SCADA - KINERJA PERALATAN SCADA",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
            OpenApiParameter(name='harian', description='Filter Tanggal 2022-01-29', required=False, type=str, default=None),
            OpenApiParameter(name='bulanan', description='Format Tanggal : 05-2022', required=False, type=str, default=None),
            OpenApiParameter(name='path1text', description='Filter path1text', required=False, type=str, default=None),
            OpenApiParameter(name='path3text', description='Filter path3text', required=False, type=str, default=None),

        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['FASOP LAPORAN SCADA']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'DATA KINERJA PERALATAN SCADA'

        cur = connection.cursor()

        sql = "SELECT c.name as peralatan_scd, b.path1text, b.path2text,b.path3text, a.down, a.downtime, "
        sql = sql + "dbo.NUM_TO_DURASI(a.downtime,1,2) as durasi, a.performance FROM "
        if self.request.GET.get('bulanan') != None:
            bln_thn = request.GET.get('bulanan')
            x = bln_thn.split("-")
            sql = sql + "(select d.point_number, sum(d.downtime) as downtime,SUM ( d.down ) AS down, avg(d.performance) as performance from scd_kin_digital_harian d where MONTH(d.datum) = '"+str(x[0])+"' AND YEAR(d.datum) = '"+str(x[1])+"' group by d.point_number ) a left join "

        if self.request.GET.get('harian') != None:
            sql = sql + "scd_kin_digital_harian a left join "
        
        sql = sql + "scd_c_point b on a.point_number = b.point_number left join "
        sql = sql + "scd_pointtype c on b.id_pointtype = c.id_pointtype  "

        if self.request.GET.get('harian') != None:
            datum_harian_start = date_converter_dt(date=request.GET.get('harian'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=request.GET.get('harian'),time='23:59:00')
            sql =  sql + "WHERE a.datum >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND a.datum <= CONVERT(datetime, '" + str(datum_harian_end) + "',120)"
            if self.request.GET.get('path1text') != None:
                sql = sql + "and b.path1text like '%"+ str(request.GET.get('path1text')) +"%' "
            if self.request.GET.get('path3text') != None:
                sql = sql + "and b.path3text like '%"+ str(request.GET.get('path3text')) +"%' "
        if self.request.GET.get('bulanan') != None:
            if self.request.GET.get('path1text') != None:
                sql = sql + "WHERE b.path1text like '%"+ str(request.GET.get('path1text')) +"%' "
            if self.request.GET.get('path3text') != None:
                sql = sql + " and b.path3text like '%"+ str(request.GET.get('path3text')) +"%' "

        sql = sql + " order by b.path1text, b.path2text, b.path3text"
        
        print(sql)
        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            datas = {
                'peralatan_scd' : row[0],
                'path1text' : row[1],
                'path2text' : row[2],
                'path3text' :  row[3],
                'down' :  row[4],
                'downtime' :  row[5],
                'durasi' : row[6],
                'avability' : round(int(row[7]),2),
            }

             

          
            
            data.append(datas)
        
        return get_response(self, request, data, 'kinerja_peralatan_scd.view',headers=header, relation=relation, fields=fields,title=title)  

