 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import SCD_HIS_TRIP , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, SCD_HIS_TRIPFilter

from base.response import  get_response
from base.custom_pagination import CustomPagination


# Create your views here.
class SCD_HIS_TRIPViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = SCD_HIS_TRIP.objects.all()
    serializer_class = serializers.SCD_HIS_TRIPSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SCD_HIS_TRIPFilter
    filterset_fields = ['keyword' ]  # multi filter param
    search_fields = ['path1','path2','path3','b1','b3','status_1','elem']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_his_trip']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - Spectrum - Histori TRIP",
        description="Get Data Fasop - Spectrum - Histori TRIP",
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
        title        = 'His TRIP'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'scd_his_trip.view',headers=header, relation=relation, fields=fields,title=title)  
  