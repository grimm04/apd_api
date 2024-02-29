from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import PointtypeInduk , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, RealtimeScadaFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection


# Create your views here.
class RealtimeScadaView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PointtypeInduk.objects.all()
    serializer_class = serializers.PointtypeIndukSerializer
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RealtimeScadaFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['']

    @extend_schema(
        methods=["GET"],
        summary="DATA GANGGUAN PERALATAN SCADA",
        description="FASOP - LAPORAN SCADA - GANGGUAN PERALATAN SCADA",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
            OpenApiParameter(name='nama_pointtype', description='Filter Pointtype', required=False, type=str, default=None),

        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['FASOP LAPORAN SCADA']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'DATA GANGGUAN PERALATAN SCADA'

       
        cur = connection.cursor()

        sql = "SELECT id_pointtype, name as nama_pointtype, jenispoint as jenis_point, id_induk_pointtype FROM "
        sql = sql + "scd_pointtype WHERE id_induk_pointtype = 0 "
        if self.request.GET.get('nama_pointtype') != 'ALL' :
            sql = sql + " AND name = '" + str(self.request.GET.get('nama_pointtype')) + "'"
        sql = sql + " ORDER BY name ASC"

        # print(sql)
        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            datas = {
                'id_pointtype' : row[0],
                'nama_pointtype' : row[1],
                'jenis_pointtype' : row[2],
                'id_pointtype_induk' : row[3],
                'jml_pointtype' : self.get_total_child(str(row[0])),
                'anak_pointtype' : self.get_child(str(row[0])),
            }
            
            data.append(datas)
        
        return get_response(self, request, data, 'realtime_scada.view',headers=header, relation=relation, fields=fields,title=title)  



    def get_child(self, id_pointtype_induk):
    
        cur = connection.cursor()
        sql = "SELECT id_pointtype, name as nama_pointtype, jenispoint as jenis_point, id_induk_pointtype FROM "
        sql = sql + "scd_pointtype WHERE id_induk_pointtype != 0 and id_induk_pointtype= '"+str(id_pointtype_induk)+"' ORDER BY name ASC"
        cur.execute(sql)
        rs = cur.fetchall()
        data = []
        # print(sql)
        for row in rs:
            datas = {
                'id_pointtype' : row[0],
                'nama_pointtype' : row[1],
                'jenis_pointtype' : row[2],
                'id_pointtype_induk' : row[3],
                'jml_children' : self.get_jml_datas(str(row[0]), str(row[2])),
                'children' : self.get_datas(str(row[0]), str(row[2])),
            }
            
            data.append(datas)

        return data


    def get_datas(self, id_pointtype,jenis_point):

        cur = connection.cursor()

        sql = "SELECT a.point_number AS id, ("
        sql = sql + "CONVERT(VARCHAR(10),(DATEDIFF(s, a.datum_2, CURRENT_TIMESTAMP) / 86400 )) + ' Hari ' +"
        sql = sql + "CONVERT(VARCHAR(10),(((DATEDIFF(s, a.datum_2, CURRENT_TIMESTAMP) % 86400 ) / 3600 ))) + ' Jam ' + "
        sql = sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, a.datum_2, CURRENT_TIMESTAMP) % 86400 ) % 3600 ) / 60 ))) + ' Menit ' + "
        sql = sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, a.datum_2, CURRENT_TIMESTAMP) % 86400 ) % 3600 ) % 60 ))) +  ' Detik ' ) as durasi,"
        sql = sql + "a.datum AS tgl_gangguan, a.value,b.point_name FROM "

        if jenis_point == 'ANALOG' :
            sql = sql + "scd_analog_rtl a LEFT JOIN  "
            # print('bener')
        elif jenis_point == 'DIGITAL':
            sql = sql + "scd_digital_rtl a LEFT JOIN  "
            # print('salah')
            
        sql = sql + " scd_c_point b ON a.point_number = b.point_number "
        sql = sql + " WHERE  a.kesimpulan = 'INVALID' and b.id_pointtype = '"+str(id_pointtype)+"' "
        # print(sql)
        cur.execute(sql)
        data = []
        rs = cur.fetchall()
        for row in rs:
            datas = {
                'point_number' : row[0],
                'durasi' : row[1],
                'tgl_gangguan' : str(row[2]),
                'value' : row[3],
                'point_name' : row[4],
            }

            data.append(datas)
        return data


    def get_total_child(self, id_pointtype_induk):

        cur = connection.cursor()
        sql = "SELECT count(*) as jlh FROM "
        sql = sql + "scd_pointtype WHERE id_induk_pointtype != 0 and id_induk_pointtype= '"+str(id_pointtype_induk)+"' "

        # print(sql)
        cur.execute(sql)
        rs = cur.fetchone()
        # print(rs[0])


        return rs[0]


    def get_jml_datas(self, id_pointtype,jenis_point):

        cur = connection.cursor()
        sql = "SELECT count(*) as jml FROM "

        if jenis_point == 'ANALOG' :
            sql = sql + "scd_analog_rtl a LEFT JOIN  "
            # print('bener')
        elif jenis_point == 'DIGITAL':
            sql = sql + "scd_digital_rtl a LEFT JOIN  "
            # print('salah')
            
        sql = sql + " scd_c_point b ON a.point_number = b.point_number "
        sql = sql + " WHERE  a.kesimpulan = 'INVALID' and b.id_pointtype = '"+str(id_pointtype)+"' "
        # print(sql)
        cur.execute(sql)
        rs = cur.fetchone()
        # print(rs[0])


        return rs[0]




 