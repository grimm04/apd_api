 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import SCD_KIN_RTU_HARIAN , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, SCD_KIN_RTU_HARIANFilter

from base.response import   get_response 
from base.custom_pagination import CustomPagination
from django.db import connection
from library.date_converter import date_converter_dt


# Create your views here.
class SCD_KIN_RTU_HARIANViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = SCD_KIN_RTU_HARIAN.objects.all()
    serializer_class = serializers.SCD_KIN_RTU_HARIANSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SCD_KIN_RTU_HARIANFilter
    filterset_fields = [  'keyword']   # multi filter param
    search_fields = [ 'up','down', 'downtime','uptime','performance','faktor']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_kin_rtu_harian']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - Spectrum - Kinerja RTU Harian",
        description="Get Data Fasop - Spectrum - Kinerja RTU Harian",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['fasop_spectrum_kin']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Kin RTU Harian'
        

        cur = connection.cursor()

        sql = "SELECT id_pointtype, name as nama_pointtype FROM scd_pointtype WHERE jenispoint ='RTU'"

        print(sql)
        cur.execute(sql)
        data = []
        rs = cur.fetchall()

        for row in rs:
            datas = {
                'id_pointtype' : row[0],
                'nama_pointtype' : row[1],
                'child' : self.get_childd(str(row[0])),
            }
        
            data.append(datas)
          

        print(data)

        
        return get_response(self, request, data, 'scd_kin_rtu_harian.view',headers=header, relation=relation, fields=fields,title=title)  

    def get_childd (self, id_pointtype):
        cur = connection.cursor()
        addsql = ''
        sql = "SELECT a.*, b.path3text, c.name as pointtypename, (round(abs(a.downtime)*1440,2)) as durasi "
        sql = sql + " FROM scd_kin_rtu_harian a, scd_ref_rtu b, scd_pointtype c WHERE a.point_number = b.point_number and c.id_pointtype = b.id_pointtype"
        if self.request.GET.get('datum'):
            datum_harian_start = date_converter_dt(date=self.request.GET.get('datum'),time='00:00:00')
            datum_harian_end = date_converter_dt(date=self.request.GET.get('datum'),time='23:59:00')
            addsql = addsql + " AND a.datum >= CONVERT(datetime, '" + str(datum_harian_start) + "',120) AND a.datum <= CONVERT(datetime, '" + str(datum_harian_end) + "',120)"

            sql = sql + addsql

        sql = sql + " AND b.id_pointtype = '"+id_pointtype+"'"
        sql = sql + " ORDER BY b.path3text"

        print(sql)
        cur.execute(sql)
        rs = cur.fetchall()
        data = []
        for row in rs:
            datas = {
                'id_kin_rtu_harian' : row[0] ,
                'up' : row[1],
                'down' : row[2],
                'downtime' : row[3],
                'uptime' : row[4],
                'perfomance' : row[5],
                'faktor' : row[6],
                'datum' : row[7],
                'datum_created' : row[8],
                'point_number' : row[9],
                'altime' :row[10] ,
                'kinerja' : row[11],
                'path3text' : row[12],
                'pointtypename' : row[13],
                'durasi' : row[14],
            }

            data.append(datas)

        return data




  