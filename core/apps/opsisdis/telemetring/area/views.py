from imp import PKG_DIRECTORY
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TelemetringArea, EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import TelemetringAreaFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found, response_basic
from base.custom_pagination import CustomPagination

class TelemetringAreaViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringArea.objects.all()
    serializer_class = serializers.TelemetringAreaSerializers
    update_serializer_class = serializers.UDTelemetringAreaSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringAreaFilter
    filterset_fields = ['keyword']
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_area']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Area",
        description="Get OPSISDIS - Telemetring - Area",
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
        title = 'Laporan Telemetring Area'
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'telemetring_area.view', headers=header, relation=relation,
                        fields=fields, title=title)

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Telemetring - Area - Specified.",
        description="Get OPSISDIS - Telemetring - Area - Specified.",
        tags=['opsisdis_telemetring']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        telemetring_area = self.queryset.filter(id_trans_tm_area=pk)
        if not telemetring_area:
            return not_found('telemetring_area.not_found')

        serializer = self.serializer_class(telemetring_area, many=True)
        return response__(request, serializer, 'telemetring_area.view')

class TelemetringGetCountAreaViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TelemetringArea.objects.all()
    serializer_class = serializers.TelemetringAreaSerializers
    update_serializer_class = serializers.UDTelemetringAreaSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TelemetringAreaFilter
    filterset_fields = ['keyword']
    search_fields = ['i', 'v', 'p', 'q', 'f', 'datum']
    ordering_fields = '__all__'
    ordering = ['id_trans_tm_area']

    @extend_schema(
        summary="Get OPSISDIS - Telemetring - Area Count i,v,p (null)",
        description="Get OPSISDIS - Telemetring - Area Count i,v,p (null)", 
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
            "message": 'Berhasi mendapatkan data total telemetring Area',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 

    def get_filter(self, request, field=None): 
        datum            =  request.GET.get('datum', None)
        datum_date            =  request.GET.get('datum_date', None)  
        id_lokasi        =  request.GET.get('id_lokasi', None) 
        id_parent_lokasi = request.GET.get('id_parent_lokasi')
        keyword = request.GET.get('keyword')  
 
        queryset = self.filter_queryset(TelemetringArea.objects.all())

        if id_lokasi:
            queryset = self.filter_queryset(TelemetringArea.objects.filter(id_lokasi__exact=id_lokasi))

        if id_parent_lokasi:
            queryset = self.filter_queryset(TelemetringArea.objects.filter(id_parent_lokasi__exact=id_parent_lokasi))

        if datum:
            queryset = self.filter_queryset(TelemetringArea.objects.filter(datum__exact=datum))
        
        if datum_date:
            queryset = self.filter_queryset(TelemetringArea.objects.filter(datum__date=datum_date)) 

        if field == "i":
            queryset = self.filter_queryset(TelemetringArea.objects.filter(i__isnull=True))
        if field == "v":
            queryset = self.filter_queryset(TelemetringArea.objects.filter(v__isnull=True))
        if field == "p":
            queryset = self.filter_queryset(TelemetringArea.objects.filter(p__isnull=True))

        if keyword:
            queryset = self.filter_queryset(TelemetringArea.objects.filter(
                ( 
                    Q(datum__contains=keyword)  | Q(i__contains=keyword) | Q(v__contains=keyword) | Q(p__contains=keyword) | Q(q__contains=keyword) | Q(f__contains=keyword) 
                )
            )) 


        data = queryset.count()
        return data 