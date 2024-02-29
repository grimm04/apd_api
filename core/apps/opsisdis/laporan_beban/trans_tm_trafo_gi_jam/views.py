 
import re
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter
 
from apps.opsisdis.telemetring.trafo_gi_non_ktt.models import TelemetringTrafoGI  

from . import serializers
from .filters import SearchFilter, LaporanTrafoGIFilter
from .models import EXPORT_HEADERS,EXPORT_FIELDS,EXPORT_RELATION_FIELD,EXPORT_HEADERS_HARIAN_KTT,EXPORT_HEADERS_HARIAN_NON_KTT

from base.response import get_response,get_response_data,validate_serializer,error_response, response_json,get_response_no_page,not_found
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
class LaporanTrafoGIViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringTrafoGI.objects.all()
    serializer_class = serializers.LaporanBebanTrafoGISerializers 
    validate_serializer_class = serializers.ValidationFilterGISerializer 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaporanTrafoGIFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['datum','id_parent_lokasi_id__nama_lokasi','id_lokasi_id__nama_lokasi','id_parent_lokasi_id__kode_lokasi','id_lokasi_id__kode_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_trafo_gi']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - Trafo GI Per Jam",
        description="Get Data Opsis - Laporan Beban - Trafo GI Per Jam",
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
        jenis_layanan = request.GET['jenis_layanan'] if 'jenis_layanan' in request.GET else None 

        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        header_caption = EXPORT_HEADERS_HARIAN_KTT if jenis_layanan == 'KTT' else EXPORT_HEADERS_HARIAN_NON_KTT
        fields = EXPORT_FIELDS
        title = 'Laporan Beban Tegangan Trafo Gi Perjam'
        queryset = self.filter_queryset(self.get_queryset())     
        return get_response(self, request, queryset, 'trans_tm_trafo_gi_jam.view', headers=header, relation=relation,
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
  

class LaporanTrafoGIPDFTESTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringTrafoGI.objects.all()
    serializer_class = serializers.LaporanBebanTrafoGIPDFSerializers  

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = LaporanTrafoGIFilter
    filterset_fields = ['keyword']   # multi filter param
    search_fields = ['datum','id_parent_lokasi_id__nama_lokasi','id_lokasi_id__nama_lokasi','id_parent_lokasi_id__kode_lokasi','id_lokasi_id__kode_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_trafo_gi']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Opsis - Laporan Beban - TrafoGI Per Jam Export Chart PDF",
        description="Get Data Opsis - Laporan Beban - TrafoGI Per Jam Export Chart PDF",
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
            return not_found('trans_tm_trafo_gi_jam.not_found') 
        
        datum_after = request.GET['datum_after'] if 'datum_after' in request.GET else None
        datum_before = request.GET['datum_before'] if 'datum_before' in request.GET else None 

        if datum_after and datum_before: 
            jenis_layanan = request.GET['jenis_layanan'] if 'jenis_layanan' in request.GET else 'KTT' 
            label_parent = d[0].get('ref_parent_lokasi').get('nama_lokasi')
            label_child = d[0].get('ref_lokasi').get('nama_lokasi')

            label = 'GI %s - Trafo GI %s' % (label_parent,label_child) 
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
            
            fname = 'laporan beban TrafoGI %s per jam.pdf' % jenis_layanan
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
                export_pdf.savefig(orientation='landscape')
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
                export_pdf.savefig(orientation='landscape')
                plt.close() 
            return FileResponse(open(path, 'rb'), content_type='application/octet-stream') 
        return not_found('trans_tm_trafo_gi_jam.not_found')

