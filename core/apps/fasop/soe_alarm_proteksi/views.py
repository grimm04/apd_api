from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from library.date_converter import date_converter_dt

from .models import SoeAlarmProteksi, EXPORT_FIELDS, EXPORT_HEADERS, EXPORT_RELATION_FIELD
from . import serializers
from .filters import SearchFilter, SoeAlarmProteksiFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection
from rest_framework import response, status


# Create your views here.
class SoeAlarmProteksiView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.SoeAlarmProteksiSerializer

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SoeAlarmProteksiFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['']

    @extend_schema(
        methods=["GET"],
        summary="DATA SEQUENCE OF EVENT & ALARM PROTEKSI",
        description="FASOP - LAPORAN SCADA - SEQUENCE OF EVENT & ALARM PROTEKSI",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
            OpenApiParameter(name='path1text', description='Filter path1text', required=False, type=str, default=None),
            OpenApiParameter(name='path2text', description='Filter path2text', required=False, type=str, default=None),
            OpenApiParameter(name='path3text', description='Filter path3text', required=False, type=str, default=None),
            OpenApiParameter(name='path4text', description='Filter path4text', required=False, type=str, default=None),
            OpenApiParameter(name='path5text', description='Filter path5text', required=False, type=str, default=None),
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
        title        = 'DATA SEQUENCE OF EVENT & ALARM PROTEKSI'

       
        cur = connection.cursor()

        sql = "SELECT a.id_kin_digital_harian, FORMAT ( a.datum, 'dd-MM-yyyy hh:mm:ss:mss ' ) AS tanggal, b.path1text, b.path2text, b.path3text, b.path4text, b.path5text, b.point_text FROM "
        sql = sql + "scd_kin_digital_harian a LEFT JOIN scd_c_point b ON a.point_number = b.point_number WHERE "
        if self.request.GET.get('tanggal_mulai') != None:
            datum_harian_start = date_converter_dt(date=self.request.GET.get('tanggal_mulai'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=self.request.GET.get('tanggal_akhir'),time='23:59:00')
            sql = sql + " a.datum >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND a.datum <= CONVERT(datetime, '" + str(datum_harian_end) + "',120)"
        if self.request.GET.get('path1text') != None:
            sql = sql + " AND path1text = '" + str(self.request.GET.get('path1text')) + "'"
        if self.request.GET.get('path2text') != None:
            sql = sql + " AND path2text = '" + str(self.request.GET.get('path2text')) + "'"
        if self.request.GET.get('path3text') != None:
            sql = sql + " AND path3text = '" + str(self.request.GET.get('path3text')) + "'"
        if self.request.GET.get('path4text') != None:
            sql = sql + " AND path4text = '" + str(self.request.GET.get('path4text')) + "'"
        if self.request.GET.get('path5text') != None:
            sql = sql + " AND path5text = '" + str(self.request.GET.get('path5text')) + "'"

        sql = sql + " ORDER BY a.datum desc "

        # print(sql)
        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            datas = {
                'id_kin_digital_harian' : row[0],
                'tanggal' : row[1],
                'path1text' : row[2],
                'path2text' : row[3],
                'path3text' :  row[4],
                'path4text' :  row[5],
                'path5text' :  row[6],
                'point_text' : row[7],
            }
            
            data.append(datas)
        
        return get_response(self, request, data, 'soe_alarm_proteksi.view',headers=header, relation=relation, fields=fields,title=title)  

class PathView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.PathTextSerializer

    @extend_schema(
        methods=["GET"],
        summary="DATA PATH SEARCH",
        description="FASOP - LAPORAN SCADA - SEQUENCE OF EVENT & ALARM PROTEKSI",
        parameters=[
            
            OpenApiParameter(name='path', description='Filter Path Contoh : path1text, path2text, path3text, path4text, path5text', required=False, type=str, default=None),

        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['FASOP LAPORAN SCADA']
    )

    def list(self, request):

        cur = connection.cursor()

        sql = "SELECT DISTINCT "

        pathtext = self.request.GET.get('path')

        if pathtext == 'path1text':
            sql = sql + " path1text"
        if pathtext == 'path2text':
            sql = sql + " path2text"
        if pathtext == 'path3text':
            sql = sql + "path3text"
        if pathtext == 'path4text':
            sql = sql + " path4text"
        if pathtext == 'path5text':
            sql = sql + " path5text"

        sql = sql + " FROM scd_c_point ORDER BY '"+str(pathtext)+"' ASC"

        print(sql)
        cur.execute(sql)
        rs = cur.fetchall()
        data = []
        for row in rs:
            datas = {
                'path_text' : row[0],
            }
            
            data.append(datas)
        
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": "Berhasil mendapatkan data '"+str(pathtext)+"'",
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 


    


    
