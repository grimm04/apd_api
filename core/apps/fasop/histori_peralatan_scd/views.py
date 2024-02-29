from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from library.date_converter import date_converter_dt

from .models import HistoriPeralatanScd, EXPORT_FIELDS, EXPORT_HEADERS, EXPORT_RELATION_FIELD
from . import serializers
from .filters import SearchFilter, HistoriPeralatanScdFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection
from rest_framework import response, status


# Create your views here.
class HistoriPeraltanScdView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.HistoriPeralatanScdSerializer

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = HistoriPeralatanScdFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['']

    @extend_schema(
        methods=["GET"],
        summary="DATA HISTORI PERALATAN SCADA",
        description="FASOP - LAPORAN SCADA - HISTORI PERALATAN SCADA",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
            OpenApiParameter(name='tanggal_mulai', description='Filter Tanggal 2022-01-29', required=False, type=str, default=None),
            OpenApiParameter(name='tanggal_akhir', description='Filter Tanggal 2022-01-29', required=False, type=str, default=None),
            OpenApiParameter(name='nama_pointtype', description='Filter Pointtype ALL, RTU, MASTER DLL', required=False, type=str, default=None),

        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['FASOP LAPORAN SCADA']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'DATA HISTORI PERALATAN SCADA'

        cur = connection.cursor()

        sql = "SELECT a.id as id_his_scd, c.name as peralatan_scd, b.path1text, b.path2text, b.path3text, "
        sql = sql + "a.datum_1 as tanggal_awal, a.status_1 as status_awal, "
        sql = sql + "a.datum_2 as tanggal_akhir, a.status_2 as status_akhir, "
        sql = sql + "(CONVERT(VARCHAR(10),(DATEDIFF(s, a.datum_1, a.datum_2) / 86400 )) + ' Hari ' + "
        sql = sql + "CONVERT(VARCHAR(10),(((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) / 3600 ))) + ' Jam ' +  "
        sql = sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) % 3600 ) / 60 ))) + ' Menit ' +   "
        sql = sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) % 3600 ) % 60 ))) +  ' Detik ' ) as durasi, a.kesimpulan FROM "
        sql = sql + "scd_his_digital a  "
        sql = sql + " LEFT JOIN scd_c_point b ON a.point_number = b.point_number LEFT JOIN  "
        sql = sql + "scd_pointtype c ON b.id_pointtype = c.id_pointtype WHERE "
        if self.request.GET.get('tanggal_mulai') != None:
            datum_harian_start = date_converter_dt(date=self.request.GET.get('tanggal_mulai'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=self.request.GET.get('tanggal_akhir'),time='23:59:00')
            sql = sql + "  a.datum_2 >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND a.datum_2 <= CONVERT(datetime, '" + str(datum_harian_end) + "',120) "
        if self.request.GET.get('nama_pointtype') != 'ALL':
            sql = sql + " AND c.id_induk_pointtype in (select id_pointtype from scd_pointtype where name = '" + str(self.request.GET.get('nama_pointtype')) + "') "
        if self.request.GET.get('nama_pointtype') == 'ALL':
            sql = sql + " AND c.id_induk_pointtype in (select id_pointtype from scd_pointtype where id_induk_pointtype=0) "
        sql = sql + " ORDER BY a.datum_2, c.name desc "

        # print(sql)
        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            datas = {
                'id_his_scd' : row[0],
                'peralatan_scd' : row[1],
                'path1' : row[2],
                'path2' : row[3],
                'path3' :  row[4],
                'tanggal_awal' :  row[5],
                'status_awal' :  row[6],
                'tanggal_akhir' : row[7],
                'status_akhir' : row[8],
                'durasi' : row[9],
                'kesimpulan' : row[10],
            }

          
            
            data.append(datas)
        
        return get_response(self, request, data, 'histori_peralatan_scd.view',headers=header, relation=relation, fields=fields,title=title)  

