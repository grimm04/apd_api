from cmath import cos
from imp import PKG_DIRECTORY
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from rest_framework import viewsets, response, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TelemetringTrafoGI, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS, EXPORT_HEADERS_CAPTION_KTT,EXPORT_HEADERS_CAPTION_NON_KTT
from apps.opsisdis.telemetring.models import TelemetringModel
from apps.opsisdis.telemetring.mapper import TelemetringMapper
from .filters import TelemetringTrafoGIFilter, SearchFilter
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializer

from base.response import response__, get_response, not_found, response_basic,validate_serializer, error_response,response_json
from base.custom_pagination import CustomPagination

#generator 24 hour
from library.date_generator24 import datetime_range
from library.date_converter import date_converter_dt ,date_converter_str
from base.response_message import message
from django.db.models import Q   

#ambil formula
from ..def_formula import formula_daya, formula 
class TelemetringTrafoGIKTTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringTrafoGI.objects.filter(id_lokasi__jenis_layanan__exact='KTT')
    custom_serializer_class = serializers.GetTelemetringTrafoGISerializers 
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringTrafoGISerializers
    generate_serializer_class = serializers.TelemetringTrafoGIGenerateSerializers
    update_serializer_class = serializers.UDTelemetringTrafoGISerializers

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringTrafoGIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_trafo_gi'] 
    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Trafo GI KTT",
        description="Get OPSISDIS - Telemetring - Trafo GI KTT",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def list(self, request):
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        fields = EXPORT_FIELDS
        header_caption = EXPORT_HEADERS_CAPTION_KTT

        title = 'Laporan Telemetring Trafo GI KTT'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_trafo_gi.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption)
    
    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Trafo GI KTT - Specified.",
        description="Get OPSISDIS - Telemetring - Trafo GI KTT - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_trafo_gi = self.queryset.filter(id_trans_tm_trafo_gi=pk)
        if not telemetring_trafo_gi:
            return not_found('telemetring_trafo_gi.not_found')

        serializer = self.serializer_class(telemetring_trafo_gi, many=True)
        return response__(request, serializer, 'telemetring_trafo_gi.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Trafo GI KTT",
        description="Update OPSISDIS - Telemetring - Trafo GI KTT",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    def update(self, request, pk):
        telemetring_trafo_gi = get_object_or_404(TelemetringTrafoGI, pk=pk)
        #  update daya ktt
        serializer = self.custom_serializer_class(telemetring_trafo_gi, many=False)  
        tm_trafo_gi = serializer.data 
        # print(tm_trafo_gi)
        if 'i' in request.data or 'v' in request.data or 'cosq' in request.data: 
            def_pengukuran_teg_primer = tm_trafo_gi['ref_lokasi'].get('def_pengukuran_teg_primer') 
            if 'cosq' in request.data:
                cosq = request.data['cosq']
            else: 
                cosq = tm_trafo_gi['cosq']  
            if 'i' in request.data:
                arus = request.data['i']
            else: 
                arus = tm_trafo_gi['i']    
            
            if 'v' in request.data:
                v = request.data['v']
            else: 
                v = tm_trafo_gi['v']  
                
            if arus and v and cosq:
                daya = formula_daya(jenis_pengukuran='trafo_gi',arus=arus,jenis_layanan='KTT',def_pengukuran=def_pengukuran_teg_primer, cosq=cosq,tegangan=v) 
                #masukan nilai daya ke data
                request.data['p'] = round(daya ,2)   
        serializer = self.update_serializer_class(instance=telemetring_trafo_gi, data=request.data)
        data_json = validate_serializer(serializer, s=True)  

        if data_json.get('error') == True: 
            return error_response(data_json.get('data'))  

        if 'no_urut_cell' in request.data: 
            id_lokasi = tm_trafo_gi['id_lokasi']
            #update no_urut_cell
            trafo_gi =  TelemetringTrafoGI.objects.filter(id_lokasi=id_lokasi)
            no_urut_cell = request.data['no_urut_cell']
            u_no_urut_cell = trafo_gi.update(no_urut_cell=no_urut_cell)
            if u_no_urut_cell:
                ref_lokasi = RefLokasi.objects.filter(id_ref_lokasi=id_lokasi) 
                ref_lokasi.update(no_urut=no_urut_cell) 

        return response_json(data = data_json.get('data'), msg ='telemetring_trafo_gi.update') 


    @extend_schema(
        methods=["DELETE"],
        summary="Delete OPSISDIS - Telemetring - Trafo GI KTT",
        description="Delete OPSISDIS - Telemetring - Trafo GI KTT",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def destroy(self, request, pk):
        telemetring_trafo_gi = get_object_or_404(TelemetringTrafoGI, pk=pk)
        self.perform_destroy(telemetring_trafo_gi)
        return response__(request, telemetring_trafo_gi, 'telemetring_trafo_gi.delete')

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Trafo GI KTT - Batch",
        description="update OPSISDIS - Telemetring - Trafo GI KTT - Ext Atr Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_telemetring_trafo_gi')
    def update_batch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instances = []
        for item in request.data:
            instance = get_object_or_404(TelemetringTrafoGI, pk=int(item['id_trans_tm_trafo_gi']))
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='telemetring_trafo_gi.update_failed')

        return response_basic(_status=True, results=instances, msg='telemetring_trafo_gi.update')
    
    @extend_schema(
        summary="Generate OPSISDIS - Telemetring - Trafo GI KTT",
        description="Generate OPSISDIS - Telemetring - Trafo GI KTT",
        request=generate_serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['POST'], url_path='generate', url_name='generate_telemetring_trafo_gi')
    def generate_data(self, request):
        serializer = self.generate_serializer_class(data=request.data, many=False)
        if serializer.is_valid():  
            if 'id_lokasi' in request.data: 
                ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_lokasi'],id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            else:
                ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            # ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut') 
            if not ref_lokasi: 
                return not_found('telemetring_trafo_gi.not_child')   
            ref_lokasi_serializer = RefLokasiSerializer(ref_lokasi, many=True) 
            
            today = date.today()
            if 'datum' in request.data:
                datum = request.data['datum']
            else:
                datum =today.strftime("%Y-%m-%d") 
            datetext = datetime_range(datum) 
            dsave = 0
            for data_raw in ref_lokasi_serializer.data: 
                if(int(data_raw['status_listrik']) == 1):  
                    dsave +=1 
                    data = []
                    for date_t in datetext:  
                        new_date = date_converter_str(date=date_t)   
                        # print(new_date) 
                        tm_trafo_gi_hour = TelemetringTrafoGI.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_trafo_gi') 
                        if not tm_trafo_gi_hour:
                            #get jenis_layanan, def_pengukuran_teg_primer, def_pengukuran_teg_sekunder, def_nilai_cosq dari parent penyulang/ trafo_gi
                            jenis = data_raw['jenis_layanan']
                            def_nilai_cosq = data_raw['def_nilai_cosq']
                            def_pengukuran_teg_primer = data_raw['def_pengukuran_teg_primer']
                            def_pengukuran_teg_sekunder = data_raw['def_pengukuran_teg_sekunder']
                            
                            if jenis == 'KTT':
                                pengukuran = def_pengukuran_teg_primer
                            elif jenis == 'NON KTT':
                                pengukuran = def_pengukuran_teg_sekunder
                            else :
                                v = None
                            #get default Pengukuran (v) dari trafo berdasarkan jenis_layanan
                            v = formula(jenis=jenis,value=pengukuran) 
                            def_nilai_cosq = data_raw['def_nilai_cosq'] 
                            sinkron_data = data_raw['sinkron_data'] 
                            cosq = formula(jenis='cosq',value=def_nilai_cosq)   
                            data_mapper = dict({'id_lokasi': data_raw['id_ref_lokasi'], 
                                                    'id_parent_lokasi': data_raw['id_parent_lokasi'],
                                                    'datum':date_t,
                                                    'id_user_entri' : request.data['id_user_entri'],
                                                    'id_user_update' : request.data['id_user_entri'],
                                                    'v':v, 
                                                    'cosq':cosq,
                                                    'sinkron_data':sinkron_data,
                                                    'no_urut_cell':data_raw['no_urut'],
                                                    }) 
                            data.append(data_mapper)
 
                    serializer = self.serializer_class(data=data, many=True)
                    if serializer.is_valid():
                        serializer.save()
             
            if(dsave == 0):
                raw_response = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": ', tidak ada data yang tergenerate.',
                    "results": []
                }   
                return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)

            raw_response = {
                "status": status.HTTP_200_OK,
                "message": message('telemetring_trafo_gi.create'),
                "results": []
            } 

            return response.Response(data=raw_response, status=status.HTTP_200_OK)
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)

class TelemetringTrafoGINonKTTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringTrafoGI.objects.filter(id_lokasi__jenis_layanan__exact='NON KTT')
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringTrafoGISerializers
    custom_serializer_class = serializers.GetTelemetringTrafoGISerializers
    generate_serializer_class = serializers.TelemetringTrafoGIGenerateSerializers
    update_serializer_class = serializers.UDTelemetringTrafoGISerializers

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringTrafoGIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_trafo_gi']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Trafo GI Non KTT",
        description="Get OPSISDIS - Telemetring - Trafo GI Non KTT",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def list(self, request):
        header = EXPORT_HEADERS
        relation = EXPORT_RELATION_FIELD
        fields = EXPORT_FIELDS
        header_caption = EXPORT_HEADERS_CAPTION_NON_KTT

        title = 'Laporan Telemetring Trafo GI Non KTT'
        queryset = self.filter_queryset(self.get_queryset()) 

        return get_response(self, request, queryset, 'telemetring_trafo_gi.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption) 
    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Trafo GI Non KTT - Specified.",
        description="Get OPSISDIS - Telemetring - Trafo GI Non KTT - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_trafo_gi = self.queryset.filter(id_trans_tm_trafo_gi=pk)
        if not telemetring_trafo_gi:
            return not_found('telemetring_trafo_gi.not_found')

        serializer = self.serializer_class(telemetring_trafo_gi, many=True)
        return response__(request, serializer, 'telemetring_trafo_gi.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Trafo GI Non KTT ",
        description="Update OPSISDIS - Telemetring - Trafo GI Non KTT ",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    def update(self, request, pk):
        telemetring_trafo_gi = get_object_or_404(TelemetringTrafoGI, pk=pk)   
        serializer = self.custom_serializer_class(telemetring_trafo_gi, many=False)  
        tm_trafo_gi = serializer.data
        #  update daya non ktt 
        if 'i' in request.data or 'v' in request.data or 'cosq' in request.data: 
            def_pengukuran_teg_sekunder = tm_trafo_gi['ref_lokasi'].get('def_pengukuran_teg_sekunder') 
            if 'cosq' in request.data:
                cosq = request.data['cosq']
            else: 
                cosq = tm_trafo_gi['cosq']  
            if 'i' in request.data:
                arus = request.data['i']
            else: 
                arus = tm_trafo_gi['i']    
            if 'v' in request.data:
                v = request.data['v']
            else: 
                v = tm_trafo_gi['v']  
                
            if arus and v and cosq:
                daya = formula_daya(jenis_pengukuran='trafo_gi',arus=arus,jenis_layanan='NON KTT',def_pengukuran=def_pengukuran_teg_sekunder, cosq=cosq,tegangan=v) 
                #masukan nilai daya ke data
                request.data['p'] = round(daya ,2)   
        serializer = self.update_serializer_class(instance=telemetring_trafo_gi, data=request.data)
        data_json = validate_serializer(serializer, s=True)  
        if data_json.get('error') == True: 
            return error_response(data_json.get('data'))  

        if 'no_urut_cell' in request.data: 
            id_lokasi = tm_trafo_gi['id_lokasi']
            #update no_urut_cell
            trafo_gi =  TelemetringTrafoGI.objects.filter(id_lokasi=id_lokasi)
            no_urut_cell = request.data['no_urut_cell']
            u_no_urut_cell = trafo_gi.update(no_urut_cell=no_urut_cell)
            if u_no_urut_cell:
                ref_lokasi = RefLokasi.objects.filter(id_ref_lokasi=id_lokasi) 
                ref_lokasi.update(no_urut=no_urut_cell)
        return response_json(data = data_json.get('data'), msg ='telemetring_trafo_gi.update')  

    @extend_schema(
        methods=["DELETE"],
        summary="Delete OPSISDIS - Telemetring - Trafo GI Non KTT",
        description="Delete OPSISDIS - Telemetring - Trafo GI Non KTT",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def destroy(self, request, pk):
        telemetring_trafo_gi = get_object_or_404(TelemetringTrafoGI, pk=pk)
        self.perform_destroy(telemetring_trafo_gi)
        return response__(request, telemetring_trafo_gi, 'telemetring_trafo_gi.delete')

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Trafo GI Non KTT - Batch",
        description="update OPSISDIS - Telemetring - Trafo GI Non KTT - Ext Atr Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_telemetring_trafo_gi')
    def update_batch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instances = []
        for item in request.data:
            instance = get_object_or_404(TelemetringTrafoGI, pk=int(item['id_trans_tm_trafo_gi']))
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='telemetring_trafo_gi.update_failed')

        return response_basic(_status=True, results=instances, msg='telemetring_trafo_gi.update')
    
    @extend_schema(
        summary="Generate OPSISDIS - Telemetring - Trafo GI Non KTT",
        description="Generate OPSISDIS - Telemetring - Trafo GI Non KTT",
        request=generate_serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['POST'], url_path='generate', url_name='generate_telemetring_trafo_gi')
    def generate_data(self, request):
        serializer = self.generate_serializer_class(data=request.data, many=False)
        if serializer.is_valid():  
            if 'id_lokasi' in request.data: 
                ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_lokasi'],id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            else:
                ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            # ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut') 
            if not ref_lokasi: 
                return not_found('telemetring_trafo_gi.not_child')   
            ref_lokasi_serializer = RefLokasiSerializer(ref_lokasi, many=True) 
            
            today = date.today()
            if 'datum' in request.data:
                datum = request.data['datum']
            else:
                datum =today.strftime("%Y-%m-%d") 
            datetext = datetime_range(datum) 
            dsave = 0
            for data_raw in ref_lokasi_serializer.data: 
                if(int(data_raw['status_listrik']) == 1):  
                    # dt = date_converter_dt(date=request.data['datum'],time='00:30:00')  
                    # dat_t = make_aware(dt, timezone=pytz.timezone(settings.TIME_ZONE))  
                    # tm_trafo_gi = TelemetringTrafoGI.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum=dat_t).order_by('-id_trans_tm_trafo_gi')
                    # # print(tm_trafo_gi) 
                    # if not tm_trafo_gi: 
                    dsave +=1 
                    data = []
                    for date_t in datetext:  
                        new_date = date_converter_str(date=date_t)   
                        # print(new_date)
                        tm_trafo_gi_hour = TelemetringTrafoGI.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_trafo_gi') 
                        if not tm_trafo_gi_hour:
                             #get jenis_layanan, def_pengukuran_teg_primer, def_pengukuran_teg_sekunder, def_nilai_cosq dari parent penyulang/ trafo_gi
                            jenis = data_raw['jenis_layanan']
                            def_nilai_cosq = data_raw['def_nilai_cosq']
                            def_pengukuran_teg_primer = data_raw['def_pengukuran_teg_primer']
                            def_pengukuran_teg_sekunder = data_raw['def_pengukuran_teg_sekunder']
                            
                            if jenis == 'KTT':
                                pengukuran = def_pengukuran_teg_primer
                            elif jenis == 'NON KTT':
                                pengukuran = def_pengukuran_teg_sekunder
                            else :
                                v = None
                            #get default Pengukuran (v) dari trafo berdasarkan jenis_layanan
                            v = formula(jenis=jenis,value=pengukuran) 
                            def_nilai_cosq = data_raw['def_nilai_cosq'] 
                            sinkron_data = data_raw['sinkron_data'] 
                            cosq = formula(jenis='cosq',value=def_nilai_cosq)   
                            data_mapper = dict({'id_lokasi': data_raw['id_ref_lokasi'], 
                                                    'id_parent_lokasi': data_raw['id_parent_lokasi'],
                                                    'datum':date_t,
                                                    'id_user_entri' : request.data['id_user_entri'],
                                                    'id_user_update' : request.data['id_user_entri'], 
                                                    'cosq':cosq,
                                                    'v':v,
                                                    'sinkron_data':sinkron_data,
                                                    'no_urut_cell':data_raw['no_urut'],
                                                    }) 
                            data.append(data_mapper)  
                    serializer = self.serializer_class(data=data, many=True)
                    if serializer.is_valid():
                        serializer.save()
             
            if(dsave == 0):
                raw_response = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": ', tidak ada data yang tergenerate.',
                    "results": []
                }   
                return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)

            raw_response = {
                "status": status.HTTP_200_OK,
                "message": message('telemetring_trafo_gi.create'),
                "results": []
            } 

            return response.Response(data=raw_response, status=status.HTTP_200_OK)
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)


class TelemetringGetCountTrafoGINonKTTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringTrafoGI.objects.filter(id_lokasi__jenis_layanan__exact='NON KTT')
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringTrafoGISerializers
    generate_serializer_class = serializers.TelemetringTrafoGIGenerateSerializers
    update_serializer_class = serializers.UDTelemetringTrafoGISerializers

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringTrafoGIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_trafo_gi']

    @extend_schema(
        summary="Get OPSISDIS - Telemetring - Trafo GI Non KTTCount i,v,p (null)",
        description="Get OPSISDIS - Telemetring - Trafo GI  Non KTT Count i,v,p (null)", 
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    ) 
    def list(self, request, *args, **kwargs):
        i = self.get_filter(request,field='i')
        v = self.get_filter(request,field='v')
        p = self.get_filter(request,field='p')
        data = {
            "i": i,
            "v": v,
            "p": p,
        } 
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'Berhasi mendapatkan data total telemetring Trafo GI Non KTT',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

    def get_filter(self, request, field=None): 
        datum            =  request.GET.get('datum', None)
        datum_date            =  request.GET.get('datum_date', None) 
        id_lokasi        =  request.GET.get('id_lokasi', None) 
        id_parent_lokasi = request.GET.get('id_parent_lokasi')
        keyword = request.GET.get('keyword')  

        if id_lokasi:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(id_lokasi__exact=id_lokasi))

        if id_parent_lokasi:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(id_parent_lokasi__exact=id_parent_lokasi))

        if datum:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(datum__exact=datum))
        
        if datum_date: 
            start_date = date_converter_dt(date=datum_date,time='00:00:00')
            end_date = date_converter_dt(date=datum_date,time='23:59:00')   
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(datum__range=(start_date,end_date))) 

        if field == "i":
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(Q(i__isnull=True)))
        if field == "v":
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(Q(v__isnull=True)))
        if field == "p":
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(Q(p__isnull=True)))

        if keyword:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(
                ( 
                    Q(datum__contains=keyword)  | Q(i__contains=keyword) | Q(v__contains=keyword) | Q(p__contains=keyword) | Q(q__contains=keyword) | Q(f__contains=keyword) 
                )
            )) 

        queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(id_lokasi__jenis_layanan__exact='NON KTT'))  
        data = queryset.count()
        return data 


class TelemetringGetCountTrafoGIKTTViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringTrafoGI.objects.filter(id_lokasi__jenis_layanan__exact='KTT') 
    serializer_class = serializers.TelemetringTrafoGISerializers  
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringTrafoGIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_trafo_gi']

    @extend_schema(
        summary="Get OPSISDIS - Telemetring - Trafo GI KTT Count i,v,p (null)",
        description="Get OPSISDIS - Telemetring - Trafo GI KTT Count i,v,p (null)", 
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    ) 
    def list(self, request, *args, **kwargs):
        i = self.get_filter(request,field='i')
        v = self.get_filter(request,field='v')
        p = self.get_filter(request,field='p')
        data = {
            "i": i,
            "v": v,
            "p": p,
        } 
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'Berhasi mendapatkan data total telemetring Trafo GI KTT',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

    def get_filter(self, request, field=None): 
        datum            =  request.GET.get('datum', None)
        datum_date            =  request.GET.get('datum_date', None) 
        id_lokasi        =  request.GET.get('id_lokasi', None) 
        id_parent_lokasi = request.GET.get('id_parent_lokasi') 
        keyword = request.GET.get('keyword')  
 
        if id_lokasi:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(id_lokasi__exact=id_lokasi))

        if id_parent_lokasi:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(id_parent_lokasi__exact=id_parent_lokasi))

        if datum:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(datum__exact=datum))
        
        if datum_date: 
            start_date = date_converter_dt(date=datum_date,time='00:00:00')
            end_date = date_converter_dt(date=datum_date,time='23:59:00')   
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(datum__range=(start_date,end_date))) 

        if field == "i":
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(Q(i__isnull=True)))
        if field == "v":
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(Q(v__isnull=True)))
        if field == "p":
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(Q(p__isnull=True)))

        if keyword:
            queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(
                ( 
                    Q(datum__contains=keyword)  | Q(i__contains=keyword) | Q(v__contains=keyword) | Q(p__contains=keyword) | Q(q__contains=keyword) | Q(f__contains=keyword) 
                )
            )) 

        queryset = self.filter_queryset(TelemetringTrafoGI.objects.filter(id_lokasi__jenis_layanan__exact='KTT'))   
        data = queryset.count()
        return data 