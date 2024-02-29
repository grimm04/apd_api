from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from library.date_converter import date_converter_dt

from .models import HistoriRC, EXPORT_FIELDS, EXPORT_HEADERS, EXPORT_RELATION_FIELD
from . import serializers
from .filters import SearchFilter, HistoriRCFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection
from rest_framework import response, status


# Create your views here.
class SoeAlarmProteksiView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.HistoriRCSerializer

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = HistoriRCFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['']

    @extend_schema(
        methods=["GET"],
        summary="DATA HISTORI RC",
        description="FASOP - LAPORAN SCADA - HISTORI RC",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
            OpenApiParameter(name='tanggal_mulai', description='Filter Tanggal 2022-01-29', required=False, type=str, default=None),
            OpenApiParameter(name='tanggal_akhir', description='Filter Tanggal 2022-01-29', required=False, type=str, default=None),

        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['FASOP LAPORAN SCADA']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'DATA HISTORI RC'

       
        cur = connection.cursor()

        sql = "SELECT id_his_rc, path1, path2, path3,path4, path5, msgoperator, datum_1, datum_2, "
        sql =  sql + "(CONVERT(VARCHAR(10),(DATEDIFF(s, datum_1, datum_2) / 86400 )) + ' Hari ' + "
        sql =  sql + "CONVERT(VARCHAR(10),(((DATEDIFF(s, datum_1, datum_2) % 86400 ) / 3600 ))) + ' Jam ' +  "
        sql =  sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, datum_1, datum_2) % 86400 ) % 3600 ) / 60 ))) + ' Menit ' + "
        sql =  sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, datum_1, datum_2) % 86400 ) % 3600 ) % 60 ))) +  ' Detik ' ) as durasi, status_2 "
        sql =  sql + "FROM scd_his_rc "
        if self.request.GET.get('tanggal_mulai') != None:
            datum_harian_start = date_converter_dt(date=self.request.GET.get('tanggal_mulai'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=self.request.GET.get('tanggal_akhir'),time='23:59:00')
            sql = sql + " WHERE datum_2 >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND datum_2 <= CONVERT(datetime, '" + str(datum_harian_end) + "',120)"

        sql = sql + " ORDER BY datum_2 desc "

        # print(sql)
        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            datas = {
                'id_his_rc' : row[0],
                'path1' : row[1],
                'path2' : row[2],
                'path3' : row[3],
                'path4' :  row[4],
                'path5' :  row[5],
                'msgoperator' :  row[6],
                'datum_1' : row[7],
                'datum_2' : row[8],
                'durasi' : row[9],
                'status_2' : row[10],
            }
            
            data.append(datas)
        
        return get_response(self, request, data, 'histori_rc.view',headers=header, relation=relation, fields=fields,title=title)  