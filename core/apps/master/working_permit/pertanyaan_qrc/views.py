from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import PertanyaanQRC,EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, PertanyaanQRCFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination

class PertanyaanQRCView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = PertanyaanQRC.objects.all()
    serializer_class = serializers.PertanyaanQRCSerializers
    create_serializer_class = serializers.CRPertanyaanQRCSerializers
    update_serializer_class = serializers.UDPertanyaanQRCSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PertanyaanQRCFilter
    filterset_fields = ['keyword']
    search_fields = ['pertanyaan_qrc', 'pertanyaan_qrc_point']
    ordering_fields = '__all__'
    ordering = ['id_pertanyaan_qrc']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Pertanyaan QRC.",
        description="Get Data Pertanyaan QRC.",
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
        title        = 'Pertanyaan QRC'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'pertanyaan_qrc.view',headers=header, relation=relation, fields=fields,title=title) 
 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Pertanyaan QRC.",
        description="Create Data Pertanyaan QRC.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_working_permit']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'pertanyaan_qrc.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Pertanyaan QRC",
        description="Get Details Pertanyaan QRC",
        tags=['master_working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        pertanyaan_qrc = self.queryset.filter(id_pertanyaan_qrc=pk)
        if not pertanyaan_qrc:
            return not_found('pertanyaan_qrc.not_found')

        serializer = self.serializer_class(pertanyaan_qrc, many=True)
        return response__(request, serializer, 'pertanyaan_qrc.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Pertanyaan QRC.",
        description="Update Data Pertanyaan QRC.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_working_permit']
    )
    def update(self, request, pk):
        pertanyaan_qrc = get_object_or_404(PertanyaanQRC, pk=pk)
        serializer = self.update_serializer_class(instance=pertanyaan_qrc, data=request.data)
        return post_update_response(serializer, 'pertanyaan_qrc.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Pertanyaan QRC.",
        description="Delete Data Pertanyaan QRC.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def destroy(self, request, pk):
        pertanyaan_qrc = get_object_or_404(PertanyaanQRC, pk=pk)
        self.perform_destroy(pertanyaan_qrc)
        return response__(request, pertanyaan_qrc, 'pertanyaan_qrc.delete')

    def perform_destroy(self, instance):
        instance.delete()
