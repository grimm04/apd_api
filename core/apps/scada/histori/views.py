from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import response, status

from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from apps.master.fasop.point_type.models import PointType  
from base.response import get_response  
from base.custom_pagination import CustomPagination

# Pointtype
from apps.master.fasop.point_type.models import PointType  
from . import serializers  
from .filters import SearchFilter as PointypeSearch, PointTypeFilter,ChildPointtypeFilter
  
class SCD_HISTORITreeViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PointType.objects.filter(id_induk_pointtype=None)
    serializer_class = serializers.SCD_REALTIMETreeSerializers

    pagination_class = CustomPagination

    filter_backends = (PointypeSearch, DjangoFilterBackend, OrderingFilter)
    filter_class = PointTypeFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name','jenispoint']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_pointtype']

    def get_serializer_context(self):
        context = super(SCD_HISTORITreeViews, self).get_serializer_context()
        query_params = self.request.query_params 
        context.update({"query_params": query_params})
        return context
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs) 
    @extend_schema(
        methods=["GET"],
        summary="GET Histori SCADA - Histori Tree.",
        description="GET Histori SCADA - Histori Tree.",
        parameters=[
            OpenApiParameter(name='id_pointtype', description='id_pointtype', required=False, type=str, default=None),
            OpenApiParameter(name='id_ref_lokasi', description='id_ref_lokasi', required=False, type=str, default=None),
            OpenApiParameter(name='status_rtu', description='status rtu', required=False, type=str, default=None),
            OpenApiParameter(name='child__status' , description='status child', required=False, type=str, default=None),
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='his__statekey_1' , description='his statekey_1 [0 = INVALID, 1 = VALID]', required=False, type=int, default=0, ), 
            OpenApiParameter(name='his__statekey_2' , description='his statekey_2 [0 = INVALID, 1 = VALID]', required=False, type=int, default=0, ), 
            OpenApiParameter(name='his__kesimpulan' , description='his kesimpulan = [VALID, INVALID]', required=False, type=str, default='INVALID'), 
            OpenApiParameter(name='his__datum_after', description='datum_after', required=False, type=OpenApiTypes.DATETIME, default=None),
            OpenApiParameter(name='his__datum_before', description='datum_before', required=False, type=OpenApiTypes.DATETIME, default=None),
            OpenApiParameter(name='his__datum_1_after', description='datum_1_after', required=False, type=OpenApiTypes.DATETIME, default=None),
            OpenApiParameter(name='his__datum_1_before', description='datum_1_before', required=False, type=OpenApiTypes.DATETIME, default=None),
            OpenApiParameter(name='his__datum_2_after', description='datum_2_after', required=False, type=OpenApiTypes.DATETIME, default=None),
            OpenApiParameter(name='his__datum_2_before', description='datum_2_before', required=False, type=OpenApiTypes.DATETIME, default=None),
            # OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            # OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['laporan_scada']
    )
    def list(self, request,**kwargs):
        # header      = EXPORT_HEADERS
        # relation    = EXPORT_RELATION_FIELD
        # fields      = EXPORT_FIELDS
        # title        = 'RTU'
        # query_params = self.request.query_params
 
        queryset = self.filter_queryset(self.get_queryset())  
        data = self.paginate_queryset(queryset)
        serializer = self.get_serializer(instance=data, many=True)  

        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'Berhasil mendapatkan data Histori',
            "results": serializer.data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK) 
