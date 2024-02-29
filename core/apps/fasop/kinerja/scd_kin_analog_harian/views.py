from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import SCD_KIN_ANALOG_HARIAN , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, SCD_KIN_ANALOG_HARIANFilter

from base.response import get_response
from base.custom_pagination import CustomPagination


# Create your views here.
class SCD_KIN_ANALOG_HARIANViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = SCD_KIN_ANALOG_HARIAN.objects.all()
    serializer_class = serializers.SCD_KIN_ANALOG_HARIANSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = SCD_KIN_ANALOG_HARIANFilter
    filterset_fields = [  'keyword']   # multi filter param
    search_fields = [ 'up','down', 'downtime','uptime','performance','faktor']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_kin_analog_harian']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop - Spectrum - Kinerja Analog Harian",
        description="Get Data Fasop - Spectrum - Kinerja Analog Harian",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['fasop_spectrum_kin']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Kin Analog Harian'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'scd_kin_analog_harian.view',headers=header, relation=relation, fields=fields,title=title)  
  