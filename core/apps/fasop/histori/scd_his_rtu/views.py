from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import SCD_HIS_RTU , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, SCD_HIS_RTUFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination
from library.date_converter import date_converter_dt ,date_converter_str

from django.db import connection


# Create your views here.
class SCD_HIS_RTUViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = SCD_HIS_RTU.objects.all()
    serializer_class = serializers.SCD_HIS_RTUSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SCD_HIS_RTUFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = ['status','status_1','status_2']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - Spectrum - Histori RTU",
        description="Get Data Fasop - Spectrum - Histori RTU",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),

            OpenApiParameter(name='datum_start', description='Format Tanggal : 2022-05-11',required=False, type=str),
            OpenApiParameter(name='datum_end', description='Format Tanggal : 2022-05-11',required=False, type=str),
            OpenApiParameter(name='b1', description='Value Path3 ',required=False, type=str),
            OpenApiParameter(name='pointtype', description='ID Point Type ',required=False, type=str),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['fasop_spectrum_his']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'His RTU'
        addsql = ''

        cur = connection.cursor()

        sql = "SELECT CONVERT ( VARCHAR, a.datum_1, 120 ) AS datum_1, a.statekey_1, a.status_1, CONVERT ( VARCHAR, a.datum_2, 120 ) AS datum_2, a.statekey_2, a.status_2, b.path3text, "
       
        sql = sql + " ( CONVERT(VARCHAR(10), (DATEDIFF(s, a.datum_1, a.datum_2) / 86400 ))  + ' Hari ' + "
        sql = sql + "   CONVERT(VARCHAR(10), ((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) / 3600 )) + ' Jam ' + "
        sql = sql + "   CONVERT(VARCHAR(10), (((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) % 3600 ) / 60 )) + ' Menit ' + "
        sql = sql + "   CONVERT(VARCHAR(10), (((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) % 3600 ) % 60 )) + ' Detik ' "
        sql = sql + " ) as durasi, c.name AS jenis_rtu, a.kesimpulan"
        sql = sql + " FROM scd_his_rtu a, scd_ref_rtu b, scd_pointtype c "
        sql = sql + " WHERE a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype "

        if request.GET.get('datum_start') != None:
            datum_start =   date_converter_dt(date=request.GET.get('datum_start'),time='00:00:00')          
            datum_end =   date_converter_dt(date=request.GET.get('datum_end'),time='23:59:00')    
            addsql = addsql + " AND a.datum_2 >= CONVERT(datetime, '" + str(datum_start) + "',120) AND a.datum_2 <=  CONVERT(datetime, '" + str(datum_end) + "',120) "      
        
        if request.GET.get('b1'):
            addsql = addsql + " AND b.path3text like '%"+ str(request.GET.get('b1')) +"%'"

        if request.GET.get('pointtype'):
            addsql = addsql + " AND c.id_pointtype= '"+ str(request.GET.get('pointtype')) +"'"

        sql = sql + addsql
        sql = sql + " ORDER BY b.path3text, a.datum_1"

        print(sql)
        cur.execute(sql)
        rs = cur.fetchall()

        data = []
        for row in rs:
            datas = {
                'datum_1' : row[0],
                'statekey_1' : row[1],
                'status_1' : row[2],
                'datum_2' : row[3],
                'statekey_2' : row[4],
                'status_2' : row[5],
                'path3text' : row[6],
                'durasi' : row[7],
                'jenis_rtu' : row[8],
                'kesimpulan' : row[9],
            }

            data.append(datas)


        return get_response(self, request, data, 'scd_his_rtu.view',headers=header, relation=relation, fields=fields,title=title)  
 