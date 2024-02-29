 
import re
from unittest.mock import patch
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework import response, status
from base.response_message import message
import datetime
# from datetime import datetime 

from drf_spectacular.utils import extend_schema, OpenApiParameter
 
from apps.opsisdis.telemetring.penyulang.models import TelemetringPenyulang   
from .models import EXPORT_HEADERS,EXPORT_HEADERS_HARIAN,EXPORT_FIELDS,EXPORT_RELATION_FIELD
from . import serializers
from .filters import SearchFilter, LaporanPenyulangFilter

from base.response import get_response,get_response_data,validate_serializer,error_response, response_json, get_response_no_page,not_found
from base.custom_pagination import CustomPagination


import os 
from ..jam import get_jam 
from ..plottext import addtext 
from dateutil import parser 
from django.conf import settings 
from django.http import HttpResponse  
from django.http import FileResponse

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages 
import matplotlib
matplotlib.use('Agg')
from matplotlib.pylab import *

class LaporanPenyulangViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringPenyulang.objects.all()
    serializer_class = serializers.LaporanBebanPenyulangSerializers 
    # validate_serializer_class = serializers.ValidationFilterGISerializer 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaporanPenyulangFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['id_parent_lokasi_id__nama_lokasi','id_lokasi_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_penyulang']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - Penyulang Per Jam",
        description="Get Data Opsis - Laporan Beban - Penyulang Per Jam",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsis_laporan_beban']
    )
    def list(self, request):    

        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        header_caption = EXPORT_HEADERS_HARIAN

        fields = EXPORT_FIELDS
        title = 'Laporan Beban Tegangan Penyulang Perjam'
        queryset = self.filter_queryset(self.get_queryset())    
        
        return get_response(self, request, queryset, 'trans_tm_penyulang_jam.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption)  
        datum_after = request.GET['datum_after'] if 'datum_after' in request.GET else None
        datum_before = request.GET['datum_before'] if 'datum_before' in request.GET else None
        jenis_layanan = request.GET['jenis_layanan'] if 'jenis_layanan' in request.GET else None
        validation = {
            'datum_after': datum_after,
            'datum_before': datum_before,
            'jenis_layanan': jenis_layanan,
        } 
        serializer = self.validate_serializer_class(data=validation, many=False)  
        data_validate = validate_serializer(serializer, s=False)   

        if data_validate.get('error') == True: 
            return error_response(data_validate.get('data'))  
 
        datum_after = data_validate.get('data').get('datum_after')
        datum_before = data_validate.get('data').get('datum_before')
        jenis_layanan = data_validate.get('data').get('jenis_layanan')
        
        h = get_jam(datum_after=datum_after, datum_before=datum_before)
        queryset = self.filter_queryset(self.get_queryset())  
        data = get_response_data(self, request=request, queryset=queryset) 
        print(data.data)
        # exit()
        array = ()
        for hours in h:
            arus = 0
            for d in data.data:
                if d['datum'] == hours:
                    if d['i']:
                        arus = arus+float(d['i'])

            array = dict(
                {
                    'jam': hours,
                    'i' :arus
                }
            )
            # data = None
        data =array
        return response_json(data = array, msg ='trans_tm_trafo_gi_hari.view')

        
        # rs = perjam_response(data=data,hours=h)

        print(len(data.data))
       
        # print(data)
        # return get_response(self, request, queryset, 'trans_tm_trafo_gi_hari.view')  
  
class LaporanPenyulangPDFTESTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringPenyulang.objects.all()
    serializer_class = serializers.LaporanBebanPenyulangPDFSerializers   
 
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaporanPenyulangFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['id_parent_lokasi_id__nama_lokasi','id_lokasi_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_penyulang']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - Penyulang Per Jam Export Chart PDF",
        description="Get Data Opsis - Laporan Beban - Penyulang Per Jam Export Chart PDF",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10), 
            # OpenApiParameter(name='type', description='Type(i) Ampere , Type(p) MW', required=True, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsis_laporan_beban']
    )
    def list(self, request):    
        queryset = self.filter_queryset(self.get_queryset())   
        d = get_response_no_page(self, request=request, queryset=queryset) 
        if not d:
            return not_found('trans_tm_penyulang_jam.not_found') 
        
        datum_after = request.GET['datum_after'] if 'datum_after' in request.GET else None
        datum_before = request.GET['datum_before'] if 'datum_before' in request.GET else None 

        if datum_after and datum_before:  
            label_parent = d[0].get('ref_parent_lokasi').get('nama_lokasi')
            label_child = d[0].get('ref_lokasi').get('nama_lokasi')

            label = 'GI %s - Penyulang %s' % (label_parent,label_child) 
            jam = get_jam(datum_after=datum_after, datum_before=datum_before)
            dt_obj = parser.parse(datum_after)   
            tgl =  '%s/%s/%s' % (dt_obj.year,dt_obj.month, dt_obj.day) 

            data_date =[] 
            for index, item in enumerate(d):
                pars = parser.parse(item.get('datum'))  
                date  = '%s:%s' % ('%02d' % pars.hour, '%02d' % pars.minute)
                data_date.append(str(date))  
            plot_x = list(set(jam).intersection(set(data_date)))
            plot_x.sort()  
            prot_y_ampere = [float(x.get('i')) if x.get('i') else 0 for x in d]
            prot_y_mw = [float(x.get('p')) if x.get('p') else 0 for x in d]  
            
            fname = 'laporan beban penyulang per jam.pdf' 
            
            dir = os.path.join(settings.BASE_DIR, 'static/')
            path = dir + fname

            # x = ['29/07/2022','30/07/2022','31/07-2022','01/08/2022','01/08/2022']
            # y = [80,100,20,50,30]
            with PdfPages(path) as export_pdf:  
                
                plt.figure(figsize=(11.69,8.27)) 
                plt.title('%s - (Beban A)' % label, fontsize=12)  
                plt.plot(plot_x, prot_y_ampere, label = 'Beban A',color='blue', marker='o') 
                addtext(plot_x, prot_y_ampere)    
                plt.xlabel(tgl, fontsize=10)
                plt.ylabel('A', fontsize=8) 
                plt.tick_params(axis='x', rotation=70) 
                plt.grid(True)
                plt.legend()
                export_pdf.savefig()
                plt.close()
 

                plt.figure(figsize=(11.69,8.27))  
                plt.title('%s - (Beban MW)' % label, fontsize=12) 
                plt.plot(plot_x, prot_y_mw, label = 'Beban MW',color='blue', marker='o') 
                addtext(plot_x, prot_y_mw)    
                plt.xlabel(tgl, fontsize=10)
                plt.ylabel('MW', fontsize=8) 
                plt.tick_params(axis='x', rotation=70)
                plt.grid(True)
                plt.legend() 
                export_pdf.savefig()
                plt.close() 
            return FileResponse(open(path, 'rb'), content_type='application/octet-stream') 
        return not_found('trans_tm_penyulang_jam.not_found')
        for c in d: 
            print(c.get('id_trans_tm_penyulang'))
        exit()
        fname = 'charts.pdf' 
        dir = os.path.join(settings.BASE_DIR, 'static/')
        path = dir + fname
        print(path)
        Data1 = {'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
        }   
        df1 = DataFrame(Data1,columns=['Unemployment_Rate','Stock_Index_Price'])


        Data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
                'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
            }   
        df2 = DataFrame(Data2,columns=['Year','Unemployment_Rate']) 
        # year = [2014, 2015, 2016, 2017, 2018, 2019]  
        # tutorial_count = [39, 117, 111, 110, 67, 29]

        # plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)  
        # plt.xlabel('Year')  
        # plt.ylabel('Number of futurestud.io Tutorials')  
        

        # plt.plot(df2['Year'], df2['Unemployment_Rate'], color='red', marker='o')
        # plt.title('Unemployment Rate Vs Year', fontsize=10)
        # plt.xlabel('Year', fontsize=8)
        # plt.ylabel('Unemployment Rate', fontsize=8)
        # plt.grid(True) 
        # plt.savefig(path) 
        # plt.close()

        # create data
        x = ['29/07/2022','30/07/2022','31/07-2022','01/08/2022','01/08/2022']
        y = [80,100,20,50,30]
        
        # plot lines
        plt.title('Unemployment Rate Vs Year', fontsize=10)
        plt.plot(x, y, label = "line 1",color='red', marker='o')
        plt.xlabel('Year', fontsize=8)
        plt.ylabel('Unemployment Rate', fontsize=8) 
        # plt.plot(y, x, label = "line 2")
        # plt.plot(x, np.sin(x), label = "curve 1")
        # plt.plot(x, np.cos(x), label = "curve 2")
        plt.legend()
        plt.savefig(path) 
        return FileResponse(open(path, 'rb'), content_type='application/octet-stream')
  
 
        with PdfPages(path) as export_pdf: 
            plt.scatter(df1['Unemployment_Rate'], df1['Stock_Index_Price'], color='green')
            plt.title('Unemployment Rate Vs Stock Index Price', fontsize=10)
            plt.xlabel('Unemployment Rate', fontsize=8)
            plt.ylabel('Stock Index Price', fontsize=8)
            plt.grid(True)
            export_pdf.savefig()
            plt.close()
            
            plt.plot(df2['Year'], df2['Unemployment_Rate'], color='red', marker='o')
            plt.title('Unemployment Rate Vs Year', fontsize=10)
            plt.xlabel('Year', fontsize=8)
            plt.ylabel('Unemployment Rate', fontsize=8)
            plt.grid(True)
            export_pdf.savefig()
            plt.close()

            with open(path, 'r') as pdf:
                response = HttpResponse(pdf.read(),content_type='application/octet-stream')
                response['Content-Disposition'] = 'filename=some_file.pdf'
                return response
            pdf.closed

            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename=hello.pdf'
            response = HttpResponse(export_pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
            return FileResponse(open(path, 'rb'), content_type='application/octet-stream')
            # response['Content-Disposition'] = 'attachment; filename={}.pdf'.format('charts') 
            return response
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": '',
            "results": export_pdf
        }   
        queryset = self.filter_queryset(self.get_queryset())   
        return get_response(self, request, queryset, 'trans_tm_penyulang_jam.view')   