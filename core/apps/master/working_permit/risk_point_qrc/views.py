from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import RiskPointQRC ,EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, RiskPointQRCFilter
from base.response import get_response, post_update_response
from base.custom_pagination import CustomPagination

class RiskPointQRCView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RiskPointQRC.objects.all()
    serializer_class = serializers.RiskPointQRCSerializers
    create_serializer_class = serializers.CRRiskPointQRCSerializers
    update_serializer_class = serializers.UDRiskPointQRCSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RiskPointQRCFilter
    filterset_fields = ['keyword']
    ordering_fields = '__all__'
    ordering = ['id_risk_point_qrc']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Risk Point QRC.",
        description="Get Data Risk Point QRC.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title       = 'Risk Point QRC'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'risk_point_qrc.view',headers=header, relation=relation, fields=fields,title=title) 
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Risk Point QRC.",
        description="Create Data Risk Point QRC.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_working_permit']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'risk_point_qrc.create')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Risk Point QRC.",
        description="Update Data Risk Point QRC.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_working_permit']
    )
    def update(self, request, pk):
        pertanyaan_qrc = get_object_or_404(RiskPointQRC, pk=pk)
        serializer = self.update_serializer_class(instance=pertanyaan_qrc, data=request.data)
        return post_update_response(serializer, 'risk_point_qrc.update')