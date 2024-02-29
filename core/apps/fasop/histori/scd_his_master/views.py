from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import SCD_HIS_MASTER , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, SCD_HIS_MASTERFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class SCD_HIS_MASTERViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = SCD_HIS_MASTER.objects.all()
    serializer_class = serializers.SCD_HIS_MASTERSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SCD_HIS_MASTERFilter
    filterset_fields = [  'keyword']   # multi filter param
    search_fields = ['status','status_1','status_2']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - Spectrum - Histori Master",
        description="Get Data Fasop - Spectrum - Histori Master",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['fasop_spectrum_his']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'His Master'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'sch_his_master.view',headers=header, relation=relation, fields=fields,title=title)  
 
    # @extend_schema(
    #     methods=["GET"],
    #     summary="Display Specified Fasop - Spectrum - Histori Master",
    #     description="Get Details Fasop - Spectrum - Histori Master",
    #     tags=['fasop']
    # )
    # def retrieve(self, request, pk, *args, **kwargs):
    #     sch_his_master = self.queryset.filter(pk=pk)
    #     if sch_his_master is None:
    #         return not_found('sch_his_master.not_found')

    #     serializer = self.serializer_class(sch_his_master, many=True)
    #     return response__(request, serializer, 'sch_his_master.view')

    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Data Fasop - Spectrum - Histori Master",
    #     description="Update Data Fasop - Spectrum - Histori Master",
    #     request=serializer_class,
    #     responses=serializer_class,
    #     tags=['master_fasop']
    # )
    # def update(self, request, pk):
    #     sch_his_master = get_object_or_404(SCD_HIS_MASTER, pk=pk)
    #     serializer = self.serializer_class(instance=sch_his_master, data=request.data)

    #     return post_update_response(serializer, 'sch_his_master.update') 