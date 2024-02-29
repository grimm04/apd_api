from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import FASOPPM , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, FASOPPMFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination

class PMView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = FASOPPM.objects.all()
    serializer_class = serializers.FASOPPMSerializers
    create_serializer_class = serializers.CRFASOPPMCSerializers
    update_serializer_class = serializers.UDFASOPPMSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = FASOPPMFilter
    filterset_fields = ['keyword']
    search_fields = ['nilai', 'status']
    ordering_fields = '__all__'
    ordering = ['id_sch_pm']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop PM",
        description="Get Data Fasop PM",
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
        title        = 'PM'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'fasop_pm.view',headers=header, relation=relation, fields=fields,title=title) 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Fasop PM",
        description="Create Data Fasop PM",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_fasop']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'fasop_pm.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Fasop PM",
        description="Get Details Fasop PM",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        fasop_pm = self.queryset.filter(pk=pk)
        if not fasop_pm:
            return not_found('fasop_pm.not_found')

        serializer = self.serializer_class(fasop_pm, many=True)
        return response__(request, serializer, 'fasop_pm.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Fasop PM",
        description="Update Data Fasop PM",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        fasop_pm = get_object_or_404(FASOPPM, pk=pk)
        serializer = self.update_serializer_class(instance=fasop_pm, data=request.data)
        return post_update_response(serializer, 'fasop_pm.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Fasop PM",
        description="Delete Data Fasop PM",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        fasop_pm = get_object_or_404(FASOPPM, pk=pk)
        self.perform_destroy(fasop_pm)
        return response__(request, fasop_pm, 'fasop_pm.delete')

    def perform_destroy(self, instance):
        instance.delete()
