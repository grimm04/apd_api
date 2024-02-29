from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import EXPORT_FIELDS, EXPORT_HEADERS, EXPORT_RELATION_FIELD

from library.date_converter import date_converter_dt

from . import serializers
from .filters import SearchFilter, DashboardKinerjaScdRTUOutOffPoolFilter

from base.response import get_response
from base.custom_pagination import CustomPagination

from django.db import connection
from rest_framework import response, status
from datetime import datetime, timedelta


# Create your views here.

class DashboardKinerjaScdBoxRTUOUOFFPOOLView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdRTUOutOffPoolSerializers


    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA RTU OUT POOL LIST",
        description="DASHBOARD KINERJA RTU OUT POOL LIST",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        
        datum = datetime.now()
        tahun = datum.year
        bulan = datum.month
        cur = connection.cursor()
        sql = "SELECT b.path1text as peralatan , d.lat, d.lon, "
        sql = sql + "(CONVERT(VARCHAR(10),(DATEDIFF(s, a.datum_1, a.datum_2) / 86400 )) + ' Hari ' + "
        sql = sql + "CONVERT(VARCHAR(10),(((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) / 3600 ))) + ' Jam ' +  "
        sql = sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) % 3600 ) / 60 ))) + ' Menit ' +   "
        sql = sql + "CONVERT(VARCHAR(10),((((DATEDIFF(s, a.datum_1, a.datum_2) % 86400 ) % 3600 ) % 60 ))) +  ' Detik ' ) as durasi "
        sql = sql + "FROM ( SELECT id, point_number, datum_1, datum_2, kesimpulan FROM scd_digital_rtl UNION SELECT id, point_number, datum_1, datum_2, kesimpulan FROM scd_analog_rtl ) a, "
        sql = sql + "scd_c_point b, scd_pointtype c, ref_lokasi d WHERE "
        sql = sql + "a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype AND  b.id_ref_lokasi = d.id_ref_lokasi AND c.id_induk_pointtype IN ( "
        sql = sql + "SELECT id_pointtype FROM scd_pointtype WHERE name IN ( 'RTU' ))  "
        sql = sql + "AND MONTH ( a.datum_2 ) = '"+str(bulan)+"'  AND YEAR ( a.datum_2 ) = '"+str(tahun)+"' AND b.kinerja= 1 and a.kesimpulan='INVALID'  "
        
        # print(sql)
        cur.execute(sql)
        rs = cur.fetchall()
        data = []
        for row in rs:
            datas = {
                'peralatan' : row[0],
                'durasi' : row[1],
                'lat' : row[2],
                'lon' : row[3],
            }

            data.append(datas)


        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan RTU OUT OFF POOL  ",
        "result": data
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK)   


# ------------------ AWAL BOX BULANAN ----------------------------------
class DashboardKinerjaScdBoxBulananRTUView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxBulananSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BULANAN BOX RTU",
        description="DASHBOARD KINERJA BULANAN BOX RTU",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box Bulanan RTU ",
        "result": get_kinerja_box('RTU', 'BULANAN')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxBulananMASTERView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxBulananSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BULANAN BOX MASTER",
        description="DASHBOARD KINERJA BULANAN BOX MASTER",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box Bulanan MASTER ",
        "result": get_kinerja_box('MASTER', 'BULANAN')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxBulananTELKOMView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxBulananSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BULANAN BOX TELKOM",
        description="DASHBOARD KINERJA BULANAN BOX TELKOM",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box Bulanan TELKOM ",
        "result": get_kinerja_box('TELKOM', 'BULANAN')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxBulananTELKOMView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxBulananSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BULANAN BOX TELKOM",
        description="DASHBOARD KINERJA BULANAN BOX TELKOM",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box Bulanan TELKOM ",
        "result": get_kinerja_box('TELKOM', 'BULANAN')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxBulananRCView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxBulananSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BULANAN BOX RC",
        description="DASHBOARD KINERJA BULANAN BOX RC",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box Bulanan RC ",
        "result": get_kinerja_box('RC', 'BULANAN')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 
# ------------------ AKHIR BOX BULANAN ----------------------------------

# ------------------ AWAL BOX KOMULATIF ----------------------------------
class DashboardKinerjaScdBoxKOMULATIFRTUView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxKomulatifSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA KOMULATIF BOX RTU",
        description="DASHBOARD KINERJA KOMULATIF BOX RTU",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box KOMULATIF RTU ",
        "result": get_kinerja_box('RTU', 'KOMULATIF')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxKOMULATIFMASTERView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxKomulatifSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA KOMULATIF BOX MASTER",
        description="DASHBOARD KINERJA KOMULATIF BOX MASTER",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box KOMULATIF MASTER ",
        "result": get_kinerja_box('MASTER', 'KOMULATIF')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxKOMULATIFTELKOMView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxKomulatifSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA KOMULATIF BOX TELKOM",
        description="DASHBOARD KINERJA KOMULATIF BOX TELKOM",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box KOMULATIF TELKOM ",
        "result": get_kinerja_box('TELKOM', 'KOMULATIF')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxKOMULATIFTELKOMView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxKomulatifSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA KOMULATIF BOX TELKOM",
        description="DASHBOARD KINERJA KOMULATIF BOX TELKOM",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box KOMULATIF TELKOM ",
        "result": get_kinerja_box('TELKOM', 'KOMULATIF')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxKOMULATIFRCView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxKomulatifSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA KOMULATIF BOX RC",
        description="DASHBOARD KINERJA KOMULATIF BOX RC",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan Box KOMULATIF RC ",
        "result": get_kinerja_box('RC', 'KOMULATIF')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 
# ------------------ AKHIR BOX KOMULATIF ----------------------------------

# ------------------ AWAL GRAFIK ----------------------------------
class DashboardKinerjaScdGrafikRTUView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdGrafik

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA GRAFIK RTU",
        description="DASHBOARD KINERJA GRAFIK RTU",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan GRAFIK RTU ",
        "result": get_kinerja_grafik('RTU')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdGrafikMASTERView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdGrafik

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA GRAFIK MASTER",
        description="DASHBOARD KINERJA GRAFIK MASTER",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan GRAFIK MASTER ",
        "result": get_kinerja_grafik('MASTER')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdGrafikTELKOMView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdGrafik

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA GRAFIK TELKOM",
        description="DASHBOARD KINERJA GRAFIK TELKOM",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan GRAFIK TELKOM ",
        "result": get_kinerja_grafik('TELKOM')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdGrafikRCView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdGrafik

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA GRAFIK RC",
        description="DASHBOARD KINERJA GRAFIK RC",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan GRAFIK RC ",
        "result": get_kinerja_grafik('RC')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 
# ------------------ AKHIR GRAFIK ----------------------------------


# ------------------ AWAL BOX RTU ----------------------------------
class DashboardKinerjaScdBoxRTUGIView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxRTUSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BOX RTU GI",
        description="DASHBOARD KINERJA BOX RTU GI",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan BOX RTU GI ",
        "result": get_kinerja_rtu('RTU GI')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxRTUGHView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxRTUSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BOX RTU GH",
        description="DASHBOARD KINERJA BOX RTU GH",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan BOX RTU GH ",
        "result": get_kinerja_rtu('RTU GH')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 
        
class DashboardKinerjaScdBoxRTUSSOView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxRTUSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BOX RTU SSO",
        description="DASHBOARD KINERJA BOX RTU SSO",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan BOX RTU SSO ",
        "result": get_kinerja_rtu('RTU SSO')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxRTURCLView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxRTUSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BOX RTU RCL",
        description="DASHBOARD KINERJA BOX RTU RCL",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan BOX RTU RCL ",
        "result": get_kinerja_rtu('RTU RECLOSER')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

# ------------------ AKHIR BOX RTU ----------------------------------

# ------------------ AWAL BOX RTU IN OUT POOL----------------------------------
class DashboardKinerjaScdBoxRTUINView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxRTUSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BOX RTU IN POOL",
        description="DASHBOARD KINERJA BOX RTU IN POOL",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan BOX RTU IN POOL ",
        "result": get_kinerja_rtu_in_pool('RTU')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

class DashboardKinerjaScdBoxRTUOUTView(viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    serializer_class = serializers.DashboardKinerjaScdBoxRTUSerializers

    @extend_schema(
        methods=["GET"],
        summary="DASHBOARD KINERJA BOX RTU OUT POOL",
        description="DASHBOARD KINERJA BOX RTU OUT POOL",

        request=serializer_class,
        responses=serializer_class,
        tags=['DASHBOARD KINERJA SCADA'],
    )

    def list(self, request):
        raw_response = {
        "status": status.HTTP_200_OK,
        "message": "Berhasil mendapatkan BOX RTU OUT POOL ",
        "result": get_kinerja_rtu_out_pool('RTU')
        }  
        
        connection.close()
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 


# ------------------ AKHIR BOX RTU IN OUT POOL----------------------------------



def get_kinerja_rtu_in_pool(pointtype):
    datum = datetime.now()
    tahun = datum.year
    bulan = datum.month
    data = []
    cur = connection.cursor()
    sql = "SELECT c.name AS pointtype, COUNT ( * ) AS jlh_pointtype "
    sql = sql + "FROM ( SELECT point_number, datum, kesimpulan FROM scd_digital_rtl UNION SELECT point_number, datum, kesimpulan FROM scd_analog_rtl ) a, "
    sql = sql + "scd_c_point b, scd_pointtype c, scd_pointtype d WHERE "
    sql = sql + "a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype AND c.id_induk_pointtype IN ( "
    sql = sql + "SELECT id_pointtype FROM scd_pointtype WHERE name IN ( '"+str(pointtype)+"' ))  "
    sql = sql + "AND MONTH ( a.datum ) = '"+str(bulan)+"'  AND YEAR ( a.datum ) = '"+str(tahun)+"' AND b.kinerja= 1 and a.kesimpulan='VALID' GROUP BY c.name "
    print(sql)
    cur.execute(sql)
    
    rs = cur.fetchall() 
    for row in rs:
        if row[1] != None:
            nilai = row[1]
            datas = {
                'pointtype' : row[0],
                'jml' : nilai
            }
        else:
            nilai = 0
            datas = {
                'pointtype' : pointtype,
                'jml' : nilai
            }

        data.append(datas) 
    if not data :
        # print('disini')
        datass = {'pointtype' : pointtype, 'jml': 0}
        return datass
    else :
        # print('disddini')
        return data

def get_kinerja_rtu_out_pool(pointtype):
    datum = datetime.now()
    tahun = datum.year
    bulan = datum.month
    data = []
    cur = connection.cursor()
    sql = "SELECT c.name AS pointtype, COUNT ( * ) AS jlh_pointtype "
    sql = sql + "FROM ( SELECT point_number, datum, kesimpulan FROM scd_digital_rtl UNION SELECT point_number, datum, kesimpulan FROM scd_analog_rtl ) a, "
    sql = sql + "scd_c_point b, scd_pointtype c, scd_pointtype d WHERE "
    sql = sql + "a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype AND c.id_induk_pointtype IN ( "
    sql = sql + "SELECT id_pointtype FROM scd_pointtype WHERE name IN ( '"+str(pointtype)+"' ))  "
    sql = sql + "AND MONTH ( a.datum ) = '"+str(bulan)+"'  AND YEAR ( a.datum ) = '"+str(tahun)+"' AND b.kinerja= 1 and a.kesimpulan='INVALID' GROUP BY c.name "
    cur.execute(sql)
    print(sql)
    rs = cur.fetchall() 
    for row in rs:
        if row[1] != None:
            nilai = row[1]
            datas = {
                'pointtype' : row[0],
                'jml' : nilai
            }
        else:
            nilai = 0
            datas = {
                'pointtype' : pointtype,
                'jml' : nilai
            }

        data.append(datas) 
    if not data :
        # print('disini')
        datass = {'pointtype' : pointtype, 'jml': 0}
        return datass
    else :
        # print('disddini')
        return data



def get_kinerja_rtu(pointtype):
    datum = datetime.now()
    tahun = datum.year
    bulan = datum.month
    data = []
    cur = connection.cursor()
    sql = "SELECT c.name AS pointtype, COUNT ( * ) AS jlh_pointtype "
    sql = sql + "FROM ( SELECT point_number, datum, kesimpulan FROM scd_digital_rtl UNION SELECT point_number, datum, kesimpulan FROM scd_analog_rtl ) a, "
    sql = sql + "scd_c_point b, scd_pointtype c, scd_pointtype d WHERE "
    sql = sql + "a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype AND c.id_pointtype IN ( "
    sql = sql + "SELECT id_pointtype FROM scd_pointtype WHERE name IN ( '"+str(pointtype)+"' ))  "
    sql = sql + "AND MONTH ( a.datum ) = '"+str(bulan)+"'  AND YEAR ( a.datum ) = '"+str(tahun)+"' AND b.kinerja= 1 GROUP BY c.name "
    cur.execute(sql)
    # print(sql)
    rs = cur.fetchall() 
    for row in rs:
        if row[1] != None:
            nilai = row[1]
            datas = {
                'pointtype' : row[0],
                'jml' : nilai
            }
        else:
            nilai = 0
            datas = {
                'pointtype' : pointtype,
                'jml' : nilai
            }

        data.append(datas) 
    if not data :
        # print('disini')
        datass = {'pointtype' : pointtype, 'jml': 0}
        return datass
    else :
        # print('disddini')
        return data
    

def get_kinerja_grafik(pointtype):
    datum = datetime.now()
    tahun = datum.year
    bulan = datum.month
    bulanAngka = 0
    nilai_bulanan = []
    nilai_komulatif = []
    target = []
    for i in range(bulan):
        bulanAngka = bulanAngka +1
        cur = connection.cursor()
        sql = "SELECT  round(SUM ( aa.avability ), 2) as avability  FROM( "
        sql = sql + "SELECT d.name AS induk_pointtype, AVG ( a.performance ) AS avability FROM( " 
        sql = sql + "SELECT point_number, performance, kinerja, datum FROM scd_kin_digital_harian UNION SELECT point_number, performance, kinerja, datum FROM scd_kin_analog_harian ) a, "
        sql = sql + "scd_c_point b, scd_pointtype c, scd_pointtype d WHERE a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype AND c.id_induk_pointtype = d.id_pointtype  "
        sql = sql + "AND c.id_induk_pointtype IN (SELECT id_pointtype FROM scd_pointtype WHERE name IN ( '"+str(pointtype)+"'  )) AND MONTH ( a.datum ) = '"+str(bulanAngka)+"' AND YEAR ( a.datum ) = '"+str(tahun)+"' "
        sql = sql + "GROUP BY d.name, c.name, a.performance ) aa "

        cur.execute(sql)
        rs = cur.fetchall() 
        for row in rs:
            if row[0] != None:
                nilai = row[0]
            else:
                nilai = 0

            nilai_bulanan.append(nilai) 
    
    cur2 = connection.cursor()
    sql2 = "SELECT a.t_01, a.t_02, a.t_03, a.t_04, a.t_05, a.t_06, a.t_07, a.t_08, a.t_09, a.t_10, a.t_11, a.t_12 "
    sql2 = sql2 + "FROM	trans_kinerja_unit a, scd_pointtype b "
    sql2 = sql2 + "WHERE a.id_pointtype = b.id_pointtype and a.id_pointtype IN ( "
    sql2 = sql2 + "SELECT id_pointtype FROM scd_pointtype WHERE name IN ( '"+str(pointtype)+"' )) and a.tahun = '"+str(tahun)+"' "
    
    cur2.execute(sql2)
    rs2 = cur2.fetchall()
    for rows2 in rs2:
        val_target = rows2[0], rows2[1], rows2[2], rows2[3], rows2[4], rows2[5], rows2[6], rows2[7], rows2[8], rows2[9], rows2[10], rows2[11]
        target.append(val_target)

    val_komulatif = 0
    for z in nilai_bulanan:
        x = z
        val_komulatif = val_komulatif + x

        nilai_komulatif.append(val_komulatif)

    data = {
        'pointtype' : pointtype,
        'target' : target[0],
        'real_bulanan' : nilai_bulanan,
        'real_komulatif' : nilai_komulatif,
    }

    return data


def get_kinerja_box(pointtype,val):
    
    bulanAngka = 0
    val_bulanan = []
    val_kom = []
    val_bln = 0
    datum = datetime.now()
    tahun = datum.year
    bulan = datum.month

    
    for i in range(bulan):
        bulanAngka = bulanAngka +1
        cur = connection.cursor()
        sql = "SELECT  round(SUM ( aa.avability ), 2) as avability  FROM( "
        sql = sql + "SELECT d.name AS induk_pointtype, AVG ( a.performance ) AS avability FROM( " 
        sql = sql + "SELECT point_number, performance, kinerja, datum FROM scd_kin_digital_harian UNION SELECT point_number, performance, kinerja, datum FROM scd_kin_analog_harian ) a, "
        sql = sql + "scd_c_point b, scd_pointtype c, scd_pointtype d WHERE a.point_number = b.point_number AND b.id_pointtype = c.id_pointtype AND c.id_induk_pointtype = d.id_pointtype  "
        sql = sql + "AND c.id_induk_pointtype IN (SELECT id_pointtype FROM scd_pointtype WHERE name IN ( '"+str(pointtype)+"'  )) AND MONTH ( a.datum ) = '"+str(bulanAngka)+"' AND YEAR ( a.datum ) = '"+str(tahun)+"' "
        sql = sql + "GROUP BY d.name, c.name, a.performance ) aa "

        cur.execute(sql)
        rs = cur.fetchall() 
        for row in rs:
            if row[0] != None:
                nilai = row[0]
            else:
                nilai = 0.0

            if bulanAngka == bulan :
                if row[0] != None:
                    val_bln = row[0]
                else:
                    val_bln = 0.0

            
            val_bulanan.append(nilai) 

    val_komulatif = 0
    for z in val_bulanan:
        x = z
        val_komulatif = val_komulatif + x

        val_kom.append(val_komulatif)


    nilai_bulanan = round(val_bln,2)
    nilai_komulatif = round(sum(val_kom),2)



    if val == 'BULANAN':
        data = {
            'pointtype' : pointtype,
            'nilai_bulanan' : nilai_bulanan,
        } 
    elif val == 'KOMULATIF':
        data = {
            'pointtype' : pointtype,
            'nilai_komulatif' : nilai_komulatif,
        } 

    
    return data
    