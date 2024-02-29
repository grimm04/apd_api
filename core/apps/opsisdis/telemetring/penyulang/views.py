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
from .models import TelemetringPenyulang, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS,EXPORT_HEADERS_CAPTION
from apps.opsisdis.telemetring.models import TelemetringModel
from apps.opsisdis.telemetring.mapper import TelemetringMapper
from .filters import TelemetringPenyulangFilter, SearchFilter
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializer

from base.response import response__, get_response, not_found, response_basic ,validate_serializer, error_response,response_json
from base.custom_pagination import CustomPagination
from base.response_message import message 

#generator 24 hour
from library.date_generator24 import datetime_range
from library.date_converter import date_converter_dt ,date_converter_str
from base.response_message import message
from django.db.models import Q   

#ambil formula
from ..def_formula import formula_daya,formula
class TelemetringPenyulangViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringPenyulang.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringPenyulangSerializers
    generate_serializer_class = serializers.TelemetringPenyulangGenerateSerializers
    update_serializer_class = serializers.UDTelemetringPenyulangSerializers 

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringPenyulangFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_penyulang']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Penyulang",
        description="Get OPSISDIS - Telemetring - Penyulang",
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
        header_caption = EXPORT_HEADERS_CAPTION

        fields = EXPORT_FIELDS
        title = 'Laporan Telemetring Penyulang'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_penyulang.view', headers=header, relation=relation,
                        fields=fields, title=title,header_caption=header_caption)

    # @extend_schema(
    #     methods=["POST"],
    #     summary="OPSISDIS - Telemetring - Penyulang",
    #     description="OPSISDIS - Telemetring - Penyulang - Single or Batch, Can Be Multiple create.",
    #     request=serializer_class,
    #     responses=serializer_class,
    #     tags=['opsisdis_telemetring']
    # )
    # def create(self, request):
    #     data = request.data
    #     many = False
    #     if type(data) is list:
    #         many = True
    #     serializer = self.serializer_class(data=data, many=many)
    #     return post_update_response(serializer, 'telemetring_penyulang.create')

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Penyulang - Specified.",
        description="Get OPSISDIS - Telemetring - Penyulang - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_penyulang = self.queryset.filter(id_trans_tm_penyulang=pk)
        if not telemetring_penyulang:
            return not_found('telemetring_penyulang.not_found')

        serializer = self.serializer_class(telemetring_penyulang, many=True)
        return response__(request, serializer, 'telemetring_penyulang.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Penyulang - Doc",
        description="Update OPSISDIS - Telemetring - Penyulang - Doc",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    def update(self, request, pk):
        telemetring_penyulang = get_object_or_404(TelemetringPenyulang, pk=pk) 
        serializer = self.serializer_class(telemetring_penyulang, many=False)  
        penyulang = serializer.data 
        #  update daya ktt
        if 'i' in request.data or 'v' in request.data or 'cosq' in request.data:   
            if 'cosq' in request.data:
                cosq = request.data['cosq']
            else: 
                cosq = penyulang['cosq']  
            if 'i' in request.data:
                arus = request.data['i']
            else: 
                arus = penyulang['i']    
            if 'v' in request.data:
                v = request.data['v']
            else: 
                v = penyulang['v']  
            if arus and v and cosq:
                daya = formula_daya(jenis_pengukuran='penyulang',arus=arus,tegangan=v, cosq=cosq) 
                #masukan nilai daya ke data
                request.data['p'] = round(daya ,2)   
        serializer = self.update_serializer_class(instance=telemetring_penyulang, data=request.data)
        data_json = validate_serializer(serializer, s=True)  

        if data_json.get('error') == True: 
            return error_response(data_json.get('data'))  

        if 'no_urut_cell' in request.data: 
            id_lokasi = penyulang['id_lokasi']
            #update no_urut_cell
            penyulang_no_urut =  TelemetringPenyulang.objects.filter(id_lokasi=id_lokasi)
            no_urut_cell = request.data['no_urut_cell']
            u_no_urut_cell = penyulang_no_urut.update(no_urut_cell=no_urut_cell)
            if u_no_urut_cell:
                ref_lokasi = RefLokasi.objects.filter(id_ref_lokasi=id_lokasi) 
                ref_lokasi.update(no_urut=no_urut_cell) 

        return response_json(data = data_json.get('data'), msg ='telemetring_penyulang.update') 

    @extend_schema(
        methods=["DELETE"],
        summary="Delete OPSISDIS - Telemetring - Penyulang",
        description="Delete OPSISDIS - Telemetring - Penyulang",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def destroy(self, request, pk):
        telemetring_penyulang = get_object_or_404(TelemetringPenyulang, pk=pk)
        self.perform_destroy(telemetring_penyulang)
        return response__(request, telemetring_penyulang, 'telemetring_penyulang.delete')

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Penyulang - Batch",
        description="update OPSISDIS - Telemetring - Penyulang - Ext Atr Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_telemetring_penyulang')
    def update_batch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instances = []
        for item in request.data:
            instance = get_object_or_404(TelemetringPenyulang, pk=int(item['id_trans_tm_penyulang']))
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='telemetring_penyulang.update_failed')

        return response_basic(_status=True, results=instances, msg='telemetring_penyulang.update')

    @extend_schema(
        summary="Generate OPSISDIS - Telemetring - Penyulang",
        description="Generate OPSISDIS - Telemetring - Penyulang",
        request=generate_serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['POST'], url_path='generate', url_name='generate_telemetring_penyulang')
    def generate_data(self, request):
        serializer = self.generate_serializer_class(data=request.data, many=False)
        if serializer.is_valid():  
            # if 'id_lokasi' in request.data: 
            #     ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_lokasi'],id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            # elif 'id_gardu_induk' in request.data: 
            #     # ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_parent_lokasi'],id_parent_lokasi=request.data['id_gardu_induk'],).order_by('no_urut')
            #     ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            # else:
            #     ref_lokasi = []
            if 'id_lokasi' in request.data: 
                ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_lokasi'],id_gardu_induk=request.data['id_gardu_induk']).order_by('no_urut')
            elif 'id_gardu_induk' in request.data: 
                # ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_parent_lokasi'],id_parent_lokasi=request.data['id_gardu_induk'],).order_by('no_urut')
                ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_jenis_lokasi=6,id_gardu_induk=request.data['id_gardu_induk']).order_by('no_urut')
            else:
                ref_lokasi = []
            if not ref_lokasi:
                return not_found('telemetring_penyulang.not_child')  
      
            ref_lokasi_serializer = RefLokasiSerializer(ref_lokasi, many=True) 
            # print(ref_lokasi_serializer)
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
                        tm_penyulang_hour = TelemetringPenyulang.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_penyulang') 
                        if not tm_penyulang_hour:
                            jenis_layanan = ['KTT','NON KTT']
                            if data_raw['parent_lokasi'].get('jenis_layanan') in jenis_layanan:
                                #get jenis_layanan, def_pengukuran_teg_primer, def_pengukuran_teg_sekunder, def_nilai_cosq dari parent penyulang/ trafo_gi
                                jenis = data_raw['parent_lokasi'].get('jenis_layanan')
                                def_nilai_cosq = data_raw['parent_lokasi'].get('def_nilai_cosq')
                                def_pengukuran_teg_primer = data_raw['parent_lokasi'].get('def_pengukuran_teg_primer')
                                def_pengukuran_teg_sekunder = data_raw['parent_lokasi'].get('def_pengukuran_teg_sekunder') 
                                
                                if jenis == 'KTT':
                                    pengukuran = def_pengukuran_teg_primer
                                elif jenis == 'NON KTT':
                                    pengukuran = def_pengukuran_teg_sekunder
                                else :
                                    v = None
                                #get default Pengukuran (v) dari trafo berdasarkan jenis_layanan
                                v = formula(jenis=jenis,value=pengukuran) 
                                cosq = formula(jenis='cosq',value=def_nilai_cosq)
                                #get sinkron_data dari trafo apa penyulang
                                sinkron_data =  data_raw['sinkron_data']
                                data_mapper = dict({'id_lokasi': data_raw['id_ref_lokasi'], 
                                                        'id_parent_lokasi': data_raw['id_parent_lokasi'],
                                                        'datum':date_t,
                                                        'id_user_entri' : request.data['id_user_entri'],
                                                        'id_user_update' : request.data['id_user_entri'], 
                                                        'sinkron_data':sinkron_data ,
                                                        'v':v,
                                                        'cosq':cosq
                                                        }) 
                                data.append(data_mapper) 
 
                    serializer = self.serializer_class(data=data, many=True)
                    if serializer.is_valid():
                        serializer.save()
                    
                      # dt = date_converter_dt(date=request.data['datum'],time='00:30:00')  
                    # tm_penyulang = TelemetringPenyulang.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum=dt).order_by('-id_trans_tm_penyulang')
                    # if not tm_penyulang: 
                    #     dsave +=1 
                    #     data = []
                    #     for date_t in datetext:  
                    #         data_mapper = self.mapper.data_mapping(id_lokasi=data_raw['id_ref_lokasi'],
                    #                                             id_user=request.data['id_user_entri'],
                    #                                             id_parent_lokasi=request.data['id_parent_lokasi'],
                    #                                             datum=date_t
                    #                                             )
                    #         data.append(data_mapper)
             
            if(dsave == 0):
                raw_response = {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": ', tidak ada data yang tergenerate.',
                    "results": []
                }   
                return response.Response(data=raw_response, status=status.HTTP_404_NOT_FOUND)

            raw_response = {
                "status": status.HTTP_200_OK,
                "message": message('telemetring_penyulang.create'),
                "results": []
            } 

            return response.Response(data=raw_response, status=status.HTTP_200_OK)
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)
        
        # data = []
        # for data_raw in ref_lokasi_serializer.data:
        #     data_mapper = self.mapper.data_mapping(id_lokasi=data_raw['id_ref_lokasi'],
        #                                            id_user=request.data['id_user_entri'],
        #                                            id_parent_lokasi=request.data['id_parent_lokasi'],
        #                                            datum=request.data['datum']
        #                                            )
        #     data.append(data_mapper)
        # serializer = self.serializer_class(data=data, many=True)  

        # return post_update_response(serializer, 'telemetring_penyulang.create')

class TelemetringGetCountPenyulangViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringPenyulang.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringPenyulangSerializers 
 
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringPenyulangFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_penyulang']

    @extend_schema(
        summary="Get OPSISDIS - Telemetring - Penyulang Count i,v,p (null)",
        description="Get OPSISDIS - Telemetring - Penyulang Count i,v,p (null)", 
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
            "message": 'Berhasi mendapatkan data total telemetring Penyulang',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

    def get_filter(self, request, field=None): 
        datum            =  request.GET.get('datum', None)
        datum_date            =  request.GET.get('datum_date', None)

        id_gardu_induk        =  request.GET.get('id_gardu_induk', None) 
        id_lokasi        =  request.GET.get('id_lokasi', None) 
        id_parent_lokasi = request.GET.get('id_parent_lokasi')
        keyword = request.GET.get('keyword')  
 
        queryset = self.filter_queryset(TelemetringPenyulang.objects.all())
 

        if id_gardu_induk:
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(id_parent_lokasi__id_gardu_induk__exact=id_gardu_induk))
        if id_parent_lokasi:
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(id_parent_lokasi__exact=id_parent_lokasi))

        
        if id_lokasi:
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(id_lokasi__exact=id_lokasi))

        if datum:
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(datum__exact=datum))
        
        if datum_date: 
            start_date = date_converter_dt(date=datum_date,time='00:00:00')
            end_date = date_converter_dt(date=datum_date,time='23:59:00')   
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(datum__range=(start_date,end_date))) 

        if field == "i":
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(Q(i__isnull=True)))
        if field == "v":
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(Q(v__isnull=True)))
        if field == "p":
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(Q(p__isnull=True)))

        if keyword:
            queryset = self.filter_queryset(TelemetringPenyulang.objects.filter(
                ( 
                    Q(datum__contains=keyword)  | Q(i__contains=keyword) | Q(v__contains=keyword) | Q(p__contains=keyword) | Q(q__contains=keyword) | Q(f__contains=keyword) 
                )
            )) 


        data = queryset.count()
        return data 