from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter
from apps.master.fasop.point_type.models import PointType 
from .models import RTU , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, RTUFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination

# Pointtype
from apps.master.fasop.point_type.models import PointType  
from apps.master.fasop.point_type.filters import SearchFilter as PointypeSearch, PointTypeFilter

# Create your views here.
class RTUViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RTU.objects.all()
    serializer_class = serializers.RTUSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RTUFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['path3text','path3']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['point_number']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - RTU.",
        description="Get Data Master - Fasop - RTU.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'RTU'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'fasop_rtu.view',headers=header, relation=relation, fields=fields,title=title) 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - Fasop - RTU.",
        description="Create Data Master - Fasop - RTU.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'fasop_rtu.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - Fasop - RTU.",
        description="Get Details Master - Fasop - RTU.",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        _rtu = self.queryset.filter(point_number=pk)
        if _rtu is None:
            return not_found('fasop_point_type.not_found')

        serializer = self.serializer_class(_rtu, many=True)
        return response__(request, serializer, 'fasop_rtu.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - Fasop - RTU.",
        description="Update Data Master - Fasop - RTU.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        _rtu = get_object_or_404(RTU, pk=pk)
        serializer = self.serializer_class(instance=_rtu, data=request.data)

        return post_update_response(serializer, 'fasop_rtu.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - Fasop - RTU.",
        description="Delete Data Master - Fasop - RTU.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        _rtu = get_object_or_404(RTU, pk=pk)
        self.perform_destroy(_rtu)
        return response__(request, _rtu, 'fasop_rtu.delete')

    def perform_destroy(self, instance):
        instance.delete()


# Create your views here.
class RTUTreeViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PointType.objects.filter(id_induk_pointtype=None,jenispoint='RTU')
    serializer_class = serializers.RTUTreeSerializers 

    pagination_class = CustomPagination

    filter_backends = (PointypeSearch, DjangoFilterBackend, OrderingFilter)
    filter_class = PointTypeFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name','jenispoint']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_pointtype']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - RTU Tree.",
        description="Get Data Master - Fasop - RTU Tree.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'RTU'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'fasop_rtu.view',headers=header, relation=relation, fields=fields,title=title) 
