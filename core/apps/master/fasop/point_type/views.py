from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import PointType , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, PointTypeFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination


# Create your views here.
class PointTypeViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PointType.objects.all()
    serializer_class = serializers.PointTypeSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PointTypeFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name','jenispoint']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_pointtype']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - Point Type.",
        description="Get Data Master - Fasop - Point Type.",
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
        title        = 'Point Type State'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'fasop_point_type.view',headers=header, relation=relation, fields=fields,title=title) 
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Master - Fasop - Point Type.",
        description="Create Data Master - Fasop - Point Type.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'fasop_point_type.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Master - Fasop - Point Type.",
        description="Get Details Master - Fasop - Point Type.",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        point_type = self.queryset.filter(id_pointtype=pk)
        if point_type is None:
            return not_found('fasop_point_type.not_found')

        serializer = self.serializer_class(point_type, many=True)
        return response__(request, serializer, 'fasop_point_type.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Master - Fasop - Point Type.",
        description="Update Data Master - Fasop - Point Type.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        point_type = get_object_or_404(PointType, pk=pk)
        serializer = self.serializer_class(instance=point_type, data=request.data)

        return post_update_response(serializer, 'fasop_point_type.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Master - Fasop - Point Type.",
        description="Delete Data Master - Fasop - Point Type.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        point_type = get_object_or_404(PointType, pk=pk)
        self.perform_destroy(point_type)
        return response__(request, point_type, 'fasop_point_type.delete')

    def perform_destroy(self, instance):
        instance.delete()

class PointTypeTreeViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PointType.objects.filter(id_induk_pointtype=None)
    serializer_class = serializers.PointTypeTreeSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PointTypeFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name','jenispoint']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_pointtype']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Master - Fasop - Point Type Tree.",
        description="Get Data Master - Fasop - Point Type Tree.",
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
        title        = 'Point Type State'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'fasop_point_type.view',headers=header, relation=relation, fields=fields,title=title) 
 