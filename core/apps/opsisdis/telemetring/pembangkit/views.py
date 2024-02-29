 
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
from .models import TelemetringPembangkit, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS, EXPORT_HEADERS_CAPTION
from .filters import TelemetringPembangkitFilter, SearchFilter
from apps.opsisdis.telemetring.models import TelemetringModel
from apps.opsisdis.telemetring.mapper import TelemetringMapper
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializer

from base.response import response__, get_response, not_found, response_basic, validate_serializer, error_response,response_json
from base.custom_pagination import CustomPagination
from base.response_message import message

#generator 24 hour
from library.date_generator24 import datetime_range
from library.date_converter import date_converter_dt ,date_converter_str
from base.response_message import message
from django.db.models import Q   

class TelemetringPembangkitViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringPembangkit.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringPembangkitSerializers
    generate_serializer_class = serializers.TelemetringPembangkitGenerateSerializers
    update_serializer_class = serializers.UDTelemetringPembangkitSerializers

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringPembangkitFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_pembangkit']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Pembangkit",
        description="Get OPSISDIS - Telemetring - Pembangkit",
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
        header_caption = EXPORT_HEADERS_CAPTION
        relation = EXPORT_RELATION_FIELD
        fields = EXPORT_FIELDS
        title = 'Laporan Telemetring Pembangkit'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_pembangkit.view', headers=header, relation=relation,
                        fields=fields, title=title, header_caption=header_caption)

    # @extend_schema(
    #     methods=["POST"],
    #     summary="OPSISDIS - Telemetring - Pembangkit",
    #     description="OPSISDIS - Telemetring - Pembangkit - Single or Batch, Can Be Multiple create.",
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
    #     return post_update_response(serializer, 'telemetring_pembangkit.create')

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Pembangkit - Specified.",
        description="Get OPSISDIS - Telemetring - Pembangkit - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_pembangkit = self.queryset.filter(id_trans_tm_pembangkit=pk)
        # telemetring_pembangkit = self.queryset.filter(id_lokasi=pk)
        # telemetring_pembangkit = telemetring_pembangkit.values('id_lokasi', 'i', 'v', 'p', 'q', 'f', 'datum')
        if not telemetring_pembangkit:
            return not_found('telemetring_pembangkit.not_found')

        serializer = self.serializer_class(telemetring_pembangkit, many=True)
        return response__(request, serializer, 'telemetring_pembangkit.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Pembangkit - Doc",
        description="Update OPSISDIS - Telemetring - Pembangkit - Doc",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    def update(self, request, pk):
        telemetring_pembangkit = get_object_or_404(TelemetringPembangkit, pk=pk)
        serializer = self.update_serializer_class(instance=telemetring_pembangkit, data=request.data)
        data_json = validate_serializer(serializer, s=True)   
        if data_json.get('error') == True: 
            return error_response(data_json.get('data'))  

        if 'no_urut_cell' in request.data: 
            s = self.serializer_class(telemetring_pembangkit, many=False)  
            pembangkit = s.data 
            id_lokasi = pembangkit['id_lokasi']
            #update no_urut_cell
            trafo_gi =  TelemetringPembangkit.objects.filter(id_lokasi=id_lokasi)
            no_urut_cell = request.data['no_urut_cell']
            u_no_urut_cell = trafo_gi.update(no_urut_cell=no_urut_cell)
            if u_no_urut_cell:
                ref_lokasi = RefLokasi.objects.filter(id_ref_lokasi=id_lokasi) 
                ref_lokasi.update(no_urut=no_urut_cell) 

        return response_json(data = data_json.get('data'), msg ='telemetring_pembangkit.update')  

    @extend_schema(
        methods=["DELETE"],
        summary="Delete OPSISDIS - Telemetring - Pembangkit",
        description="Delete OPSISDIS - Telemetring - Pembangkit",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def destroy(self, request, pk):
        telemetring_pembangkit = get_object_or_404(TelemetringPembangkit, pk=pk)
        self.perform_destroy(telemetring_pembangkit)
        return response__(request, telemetring_pembangkit, 'telemetring_pembangkit.delete')

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Pembangkit - Batch",
        description="update OPSISDIS - Telemetring - Pembangkit - Ext Atr Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_telemetring_pembangkit')
    def update_batch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instances = []
        for item in request.data:
            instance = get_object_or_404(TelemetringPembangkit, pk=int(item['id_trans_tm_pembangkit']))
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='telemetring_pembangkit.update_failed')

        return response_basic(_status=True, results=instances, msg='telemetring_pembangkit.update')

    
    @extend_schema(
        summary="Generate OPSISDIS - Telemetring - Pembangkit",
        description="Generate OPSISDIS - Telemetring - Pembangkit",
        request=generate_serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['POST'], url_path='generate', url_name='generate_telemetring_pembangkit')
    def generate_data(self, request):
        serializer = self.generate_serializer_class(data=request.data, many=False)
        if serializer.is_valid():  
            if 'id_lokasi' in request.data: 
                ref_lokasi = self.queryset_ref_lokasi.filter(id_ref_lokasi=request.data['id_lokasi'],id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            else:
                ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
             
            if not ref_lokasi:
                return not_found('telemetring_pembangkit.not_child')  
      
            
            ref_lokasi_serializer = RefLokasiSerializer(ref_lokasi, many=True) 
            # print(ref_lokasi)
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
                        tm_pembangkit_hour = TelemetringPembangkit.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_pembangkit') 
                        if not tm_pembangkit_hour:
                            data_mapper = dict({'id_lokasi': data_raw['id_ref_lokasi'], 
                                                    'id_parent_lokasi': data_raw['id_parent_lokasi'],
                                                    'datum':date_t,
                                                    'id_user_entri' : request.data['id_user_entri'],
                                                    'id_user_update' : request.data['id_user_entri'], 
                                                    }) 
                            data.append(data_mapper) 

                    serializer = self.serializer_class(data=data, many=True)
                    if serializer.is_valid():
                        serializer.save()
                    # tm_pembangkit = TelemetringPembangkit.objects.filter(id_lokasi=data_raw['id_ref_lokasi'],datum__date=request.data['datum']).order_by('-id_trans_tm_pembangkit')
                    # if not tm_pembangkit:
                    #     dsave +=1 
                    #     data = []
                    #     for date_t in datetext:  
                    #         data_mapper = self.mapper.data_mapping(id_lokasi=data_raw['id_ref_lokasi'],
                    #                                             id_user=request.data['id_user_entri'],
                    #                                             id_parent_lokasi=request.data['id_parent_lokasi'],
                    #                                             datum=date_t
                    #                                             )
                    #         data.append(data_mapper)
                    #     print(data)
                    #     serializer = self.serializer_class(data=data, many=True)
                    #     if serializer.is_valid():
                    #         serializer.save()
             
            if(dsave == 0):
                raw_response = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": ', tidak ada data yang tergenerate.',
                    "results": []
                }   
                return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)

            raw_response = {
                "status": status.HTTP_200_OK,
                "message": message('telemetring_pembangkit.create'),
                "results": []
            } 

            return response.Response(data=raw_response, status=status.HTTP_200_OK)
        raw_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": 'invalid data',
            "results": serializer.errors
        }
        return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)
         
    

class TelemetringGetCountPembangkitViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringPembangkit.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringPembangkitSerializers 
 
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringPembangkitFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_pembangkit']

    @extend_schema(
        summary="Get OPSISDIS - Telemetring - Pembangkit Count i,v,p (null)",
        description="Get OPSISDIS - Telemetring - Pembangkit Count i,v,p (null)",
        # parameters=[
        #     OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
        #                      type=str, default=1),
        #     OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10), 
        # ],
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
            "message": 'Berhasi mendapatkan data total telemetring pembangkit',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK)

        # return get_response(self, request, queryset, 'telemetring_pembangkit.view')
        # i = TelemetringPembangkit.objects.filter(i__isnull=True).count()
        # v = TelemetringPembangkit.objects.filter(v__isnull=True).count()
        # p = TelemetringPembangkit.objects.filter(p__isnull=True).count()
        # data = {
        #     "i": i,
        #     "v": v,
        #     "p": p,
        # }
        # # print(data)
        # raw_response = {
        #     "status": status.HTTP_200_OK,
        #     "message": 'Berhasi mendapatkan data total telemetring pembangkit',
        #     "results": data
        # }  
        # return response.Response(data=raw_response, status=status.HTTP_200_OK)
 
 
    def get_filter(self, request, field=None): 
        datum            =  request.GET.get('datum', None)
        datum_date            =  request.GET.get('datum_date', None)
        id_lokasi        =  request.GET.get('id_lokasi', None) 
        id_parent_lokasi = request.GET.get('id_parent_lokasi')
        keyword = request.GET.get('keyword')  
 
        queryset = self.filter_queryset(TelemetringPembangkit.objects.all())

        if id_lokasi:
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(id_lokasi__exact=id_lokasi))

        if id_parent_lokasi:
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(id_parent_lokasi__exact=id_parent_lokasi))

        if datum: 
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(datum__exact=datum)) 
            
        if datum_date:
            start_date = date_converter_dt(date=datum_date,time='00:00:00')
            end_date = date_converter_dt(date=datum_date,time='23:59:00')   
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(datum__range=(start_date,end_date))) 

        if field == "i":
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(Q(i__isnull=True)))
        if field == "v":
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(Q(v__isnull=True)))
        if field == "p":
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(Q(p__isnull=True)))

        if keyword:
            queryset = self.filter_queryset(TelemetringPembangkit.objects.filter(
                (
                    # Q(datum__contains=keyword) | Q(name__contains=keyword) | Q(path__contains=keyword)
                    Q(datum__contains=keyword)
                )
            )) 


        data = queryset.count()
        return data 
