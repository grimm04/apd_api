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
from .models import TelemetringZona, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from apps.opsisdis.telemetring.models import TelemetringModel
from apps.opsisdis.telemetring.mapper import TelemetringMapper
from .filters import TelemetringZonaFilter, SearchFilter
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializer

from base.response import response__, get_response, post_update_response, not_found, response_basic
from base.custom_pagination import CustomPagination

#generator 24 hour
from library.date_generator24 import datetime_range
from base.response_message import message
from django.db.models import Q

class TelemetringZonaViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringZona.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringZonaSerializers
    generate_serializer_class = serializers.TelemetringZonaGenerateSerializers
    update_serializer_class = serializers.UDTelemetringZonaSerializers

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringZonaFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_zona']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Zona",
        description="Get OPSISDIS - Telemetring - Zona",
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
        title = 'Laporan Telemetring Trafo GI'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_zona.view', headers=header, relation=relation,
                        fields=fields, title=title)

    # @extend_schema(
    #     methods=["POST"],
    #     summary="OPSISDIS - Telemetring - Zona",
    #     description="OPSISDIS - Telemetring - Zona - Single or Batch, Can Be Multiple create.",
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
    #     return post_update_response(serializer, 'telemetring_zona.create')
    # 
    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Zona - Specified.",
        description="Get OPSISDIS - Telemetring - Zona - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_zona = self.queryset.filter(id_trans_tm_zona=pk)
        if not telemetring_zona:
            return not_found('telemetring_zona.not_found')

        serializer = self.serializer_class(telemetring_zona, many=True)
        return response__(request, serializer, 'telemetring_zona.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Zona - Doc",
        description="Update OPSISDIS - Telemetring - Zona - Doc",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    def update(self, request, pk):
        telemetring_zona = get_object_or_404(TelemetringZona, pk=pk)
        serializer = self.update_serializer_class(instance=telemetring_zona, data=request.data)

        return post_update_response(serializer, 'telemetring_zona.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete OPSISDIS - Telemetring - Zona",
        description="Delete OPSISDIS - Telemetring - Zona",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    def destroy(self, request, pk):
        telemetring_zona = get_object_or_404(TelemetringZona, pk=pk)
        self.perform_destroy(telemetring_zona)
        return response__(request, telemetring_zona, 'telemetring_zona.delete')

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Telemetring - Zona - Batch",
        description="update OPSISDIS - Telemetring - Zona - Ext Atr Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_telemetring_zona')
    def update_batch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instances = []
        for item in request.data:
            instance = get_object_or_404(TelemetringZona, pk=int(item['id_trans_tm_zona']))
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='telemetring_zona.update_failed')

        return response_basic(_status=True, results=instances, msg='telemetring_zona.update')
    
    @extend_schema(
        summary="Generate OPSISDIS - Telemetring - Zona",
        description="Generate OPSISDIS - Telemetring - Zona",
        request=generate_serializer_class,
        responses=serializer_class,
        tags=['opsisdis_telemetring']
    )
    @action(detail=False, methods=['POST'], url_path='generate', url_name='generate_telemetring_zona')
    def generate_data(self, request):
        serializer = self.generate_serializer_class(data=request.data, many=False)
        if serializer.is_valid():  
            ref_lokasi = self.queryset_ref_lokasi.filter(id_parent_lokasi=request.data['id_parent_lokasi']).order_by('no_urut')
            if not ref_lokasi:
                return not_found('telemetring_zona.not_child')  
      
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
                        data_mapper = self.mapper.data_mapping(id_lokasi=data_raw['id_ref_lokasi'],
                                                            id_user=request.data['id_user_entri'],
                                                            id_parent_lokasi=request.data['id_parent_lokasi'],
                                                            datum=date_t
                                                            )
                        data.append(data_mapper)

                    serializer = self.serializer_class(data=data, many=True)
                    if serializer.is_valid():
                        serializer.save()
            
            print(dsave)
            if(dsave == 0):
                raw_response = {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": 'Tidak ada data!',
                    "results": []
                }   
                return response.Response(data=raw_response, status=status.HTTP_404_NOT_FOUND)

            raw_response = {
                "status": status.HTTP_200_OK,
                "message": message('telemetring_zona.create'),
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
        # return post_update_response(serializer, 'telemetring_zona.create')

class TelemetringGetCountZonaViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringZona.objects.all()
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.TelemetringZonaSerializers 

    model = TelemetringModel()
    mapper = TelemetringMapper()

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringZonaFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_zona']

    @extend_schema(
        summary="Get OPSISDIS - Telemetring - Zona Count i,v,p (null)",
        description="Get OPSISDIS - Telemetring - Zona Count i,v,p (null)", 
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
            "message": 'Berhasi mendapatkan data total telemetring Zona',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

    def get_filter(self, request, field=None): 
        datum            =  request.GET.get('datum', None)
        id_lokasi        =  request.GET.get('id_lokasi', None) 
        datum_date            =  request.GET.get('datum_date', None)  
        id_parent_lokasi = request.GET.get('id_parent_lokasi')
        keyword = request.GET.get('keyword')  
 
        queryset = self.filter_queryset(TelemetringZona.objects.all())

        if id_lokasi:
            queryset = self.filter_queryset(TelemetringZona.objects.filter(id_lokasi__exact=id_lokasi))

        if id_parent_lokasi:
            queryset = self.filter_queryset(TelemetringZona.objects.filter(id_parent_lokasi__exact=id_parent_lokasi))

        if datum:
            queryset = self.filter_queryset(TelemetringZona.objects.filter(datum__exact=datum))
        
        if datum_date:
            queryset = self.filter_queryset(TelemetringZona.objects.filter(datum__date=datum_date)) 

        if field == "i":
            queryset = self.filter_queryset(TelemetringZona.objects.filter(Q(i__isnull=True) | Q(i__exact='0')))
        if field == "v":
            queryset = self.filter_queryset(TelemetringZona.objects.filter(Q(v__isnull=True) | Q(v__exact='0')))
        if field == "p":
            queryset = self.filter_queryset(TelemetringZona.objects.filter(Q(p__isnull=True) | Q(p__exact='0')))

        if keyword:
            queryset = self.filter_queryset(TelemetringZona.objects.filter(
                ( 
                    Q(datum__contains=keyword)  | Q(i__contains=keyword) | Q(v__contains=keyword) | Q(p__contains=keyword) | Q(q__contains=keyword) | Q(f__contains=keyword) 
                )
            )) 


        data = queryset.count()
        return data 