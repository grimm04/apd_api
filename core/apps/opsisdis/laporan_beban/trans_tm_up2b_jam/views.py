 
import re
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter
 
from .models import TransTmUp2B  ,EXPORT_HEADERS,EXPORT_HEADERS_HARIAN,EXPORT_FIELDS,EXPORT_RELATION_FIELD

from . import serializers
from .filters import SearchFilter, LaporanTransTmUp2BFilter
 
from base.response import get_response,not_found,get_response_no_page
from base.custom_pagination import CustomPagination 

import os 
from ..jam import get_jam 
from ..plottext import addtext 
from dateutil import parser 
from django.conf import settings  
from django.http import FileResponse
 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages 
import matplotlib
matplotlib.use('Agg')
from matplotlib.pylab import *
class LaporanTransTmUp2BViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransTmUp2B.objects.all()
    serializer_class = serializers.LaporanBebanUp3Serializers  

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaporanTransTmUp2BFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['id_trans_tm_up2b_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_up2b']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - UP2B Per Jam",
        description="Get Data Opsis - Laporan Beban - UP2B Per Jam",
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
        title = 'Laporan Beban Tegangan UP2B Perjam'
        queryset = self.filter_queryset(self.get_queryset())    
        
        return get_response(self, request, queryset, 'trans_tm_up2b_jam.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption)   
class LaporanUP2BPDFViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransTmUp2B.objects.all()
    serializer_class = serializers.LaporanBebanUP2BPDFSerializers  

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaporanTransTmUp2BFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['id_trans_tm_up2b_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_up2b']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - UP2B Per Jam Export Chart PDF",
        description="Get Data Opsis - Laporan Beban - UP2B Per Jam Export Chart PDF",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),  
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsis_laporan_beban']
    )
    def list(self, request):    
        queryset = self.filter_queryset(self.get_queryset())   
        d = get_response_no_page(self, request=request, queryset=queryset) 
        if not d:
            return not_found('trans_tm_up2b_jam.not_found') 
        
        datum_after = request.GET['datum_after'] if 'datum_after' in request.GET else None
        datum_before = request.GET['datum_before'] if 'datum_before' in request.GET else None 

        if datum_after and datum_before:   
            label_child = d[0].get('ref_lokasi_subsistem').get('nama_lokasi')

            label = 'UP2B %s' % (label_child) 
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
            
            fname = 'laporan beban UP2B per jam.pdf' 
            
            dir = os.path.join(settings.BASE_DIR, 'static/')
            path = dir + fname
 
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
        return not_found('trans_tm_up2b_jam.not_found')
  