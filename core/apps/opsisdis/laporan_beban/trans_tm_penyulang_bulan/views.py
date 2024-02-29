 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import TransTmPenyulangBulan ,EXPORT_HEADERS,EXPORT_HEADERS_HARIAN,EXPORT_FIELDS,EXPORT_RELATION_FIELD 
from . import serializers
from .filters import SearchFilter, TransTmPenyulangBulanFilter

from base.response import get_response, get_response_no_page,not_found
from base.custom_pagination import CustomPagination

import os 
from ..jam import get_bulan 
from ..plottext import addtext  
from dateutil import parser 
from django.conf import settings  
from django.http import FileResponse

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages 
import matplotlib
matplotlib.use('Agg')
from matplotlib.pylab import *
 
class TransTmPenyulangBulanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransTmPenyulangBulan.objects.all()
    serializer_class = serializers.TransTmPenyulangBulanSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransTmPenyulangBulanFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['datum', 'id_ref_lokasi_gi_id__nama_lokasi','id_ref_lokasi_trafo_gi_id__nama_lokasi','id_ref_lokasi_penyulang_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_penyulang_bulan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - Penyulang Bulan",
        description="Get Data Opsis - Laporan Beban - Penyulang Bulan",
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
        title = 'Laporan Beban Tegangan Penyulang PerBulan'
        custom_label = None
        month_after = request.GET['month_after'] if 'month_after' in request.GET else None
        month_before = request.GET['month_before'] if 'month_before' in request.GET else None 
        if month_after and month_before:
               month_after =  parser.parse(month_after)   
               month_before = parser.parse(month_before)    
               custom_label =  '%s/%s' % (month_after.month ,month_after.year) + ' - ' + '%s/%s' % (month_before.month ,month_before.year)
        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'trans_tm_penyulang_bulan.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption, custom_label=custom_label)  
  

class LaporanPenyulangBulanPDFTESTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransTmPenyulangBulan.objects.all()
    serializer_class = serializers.LaporanBebanPenyulangBulanPDFSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransTmPenyulangBulanFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['datum', 'id_ref_lokasi_gi_id__nama_lokasi','id_ref_lokasi_trafo_gi_id__nama_lokasi','id_ref_lokasi_penyulang_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_penyulang_bulan']
 
    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - Penyulang Per Bulan Export Chart PDF",
        description="Get Data Opsis - Laporan Beban - Penyulang Per Bulan Export Chart PDF",
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
            return not_found('trans_tm_penyulang_bulan.not_found')  
        
        month_after = request.GET['month_after'] if 'month_after' in request.GET else None
        month_before = request.GET['month_before'] if 'month_before' in request.GET else None 
        # print(month_after,month_before) 
        if month_after and month_before: 
            label_parent = d[0].get('ref_lokasi_gi').get('nama_lokasi')
            label_child = d[0].get('ref_lokasi_penyulang').get('nama_lokasi')
            label = 'GI %s - Penyulang %s' % (label_parent,label_child) 
            bulan = get_bulan(month_after=month_after, month_before=month_before) 
            dt_obj = parser.parse(month_after)   
            # tgl =  '%s/%s' % (dt_obj.year,dt_obj.month) 
 
            data_date =[]
            for index, item in enumerate(d):
                pars = parser.parse(item.get('datum'))  
                date  = '%s/%s' % (pars.year,'%02d' % pars.month)
                data_date.append(str(date))  
            plot_x = list(set(bulan).intersection(set(data_date)))
            plot_x.sort()  
            prot_y_i_max = [float(x.get('i_max')) if x.get('i_max') else 0 for x in d]  
            prot_y_i_avg = [float(x.get('i_avg')) if x.get('i_avg') else 0 for x in d] 
            prot_y_i_max_siang = [float(x.get('i_max_siang')) if x.get('i_max_siang') else 0 for x in d] 
            prot_y_i_max_malam = [float(x.get('i_max_malam')) if x.get('i_max_malam') else 0 for x in d] 
            prot_y_p_max = [float(x.get('p_max')) if x.get('p_max') else 0 for x in d] 
            prot_y_p_avg = [float(x.get('p_avg')) if x.get('p_avg') else 0 for x in d] 
            prot_y_p_max_siang = [float(x.get('p_max_siang')) if x.get('p_max_siang') else 0 for x in d] 
            prot_y_p_max_malam = [float(x.get('p_max_malam')) if x.get('p_max_malam') else 0 for x in d] 
            prot_y_load_faktor = [float(x.get('load_faktor')) if x.get('load_faktor') else 0 for x in d] 
            
            # print(prot_y_i_max,prot_y_i_avg,prot_y_i_max_siang,prot_y_i_max_malam) 
            # print(prot_y_p_max,prot_y_p_avg,prot_y_p_max_siang,prot_y_p_max_malam) 
            # exit()
            fname = 'laporan beban penyulang per Bulan.pdf' 
            dir = os.path.join(settings.BASE_DIR, 'static/')
            path = dir + fname  

            with PdfPages(path) as export_pdf:  
                plt.figure(figsize=(11.69,8.27))  
                plt.title('%s - (Beban A)' % label, fontsize=10)
                plt.plot(plot_x, prot_y_i_max, label = 'Beban Max (A)',color='blue', marker='o')  
                plt.plot(plot_x, prot_y_i_avg, label = 'Beban AVG (A)',color='cyan', marker='o')  
                plt.plot(plot_x, prot_y_i_max_siang, label = 'Beban Max Siang (A)',color='green', marker='o')  
                plt.plot(plot_x, prot_y_i_max_malam, label = 'Beban Max Malam (A)',color='purple', marker='o')  
                addtext(plot_x, prot_y_i_max)   
                addtext(plot_x, prot_y_i_avg)   
                addtext(plot_x, prot_y_i_max_siang)   
                addtext(plot_x, prot_y_i_max_malam) 
                plt.tick_params(axis='x', rotation=70)  
                # plt.xlabel(tgl, fontsize=8)
                plt.ylabel('A', fontsize=8) 
                plt.grid(True)
                plt.legend()
                export_pdf.savefig()
                plt.close() 

                plt.figure(figsize=(11.69,8.27))  
                plt.title('%s - (Beban MW)' % label, fontsize=10) 
                plt.plot(plot_x, prot_y_p_max, label = 'Beban Max (MW)',color='blue', marker='o')  
                plt.plot(plot_x, prot_y_p_avg, label = 'Beban AVG (MW)',color='cyan', marker='o')  
                plt.plot(plot_x, prot_y_p_max_siang, label = 'Beban Max Siang (MW)',color='green', marker='o')  
                plt.plot(plot_x, prot_y_p_max_malam, label = 'Beban Max Malam (MW)',color='purple', marker='o')  
                addtext(plot_x, prot_y_p_max)   
                addtext(plot_x, prot_y_p_avg)   
                addtext(plot_x, prot_y_p_max_siang)   
                addtext(plot_x, prot_y_p_max_malam) 
                plt.tick_params(axis='x', rotation=70) 
                # plt.xlabel(tgl, fontsize=8)
                plt.ylabel('MW', fontsize=8) 
                plt.grid(True)
                plt.legend()
                export_pdf.savefig()
                plt.close() 

                plt.figure(figsize=(11.69,8.27))  
                plt.title('%s - (Load Faktor)' % label, fontsize=10) 
                plt.plot(plot_x, prot_y_load_faktor, label = 'Load Faktor',color='blue', marker='o')   
                addtext(plot_x, prot_y_load_faktor)   
                plt.tick_params(axis='x', rotation=70)
                # plt.xlabel(tgl, fontsize=8) 
                plt.grid(True)
                plt.legend()
                export_pdf.savefig()
                plt.close() 
            return FileResponse(open(path, 'rb'), content_type='application/octet-stream') 
        return not_found('trans_tm_penyulang_bulan.not_found')