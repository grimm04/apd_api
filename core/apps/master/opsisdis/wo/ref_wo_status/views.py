from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefWOStatus
from .filters import RefWOStatusFilter, SearchFilter, RefWOStatus

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class RefWOStatusViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefWOStatus.objects.all()
    serializer_class = serializers.CRRefWOStatusSerializers
    update_serializer_class = serializers.UDRefWOStatusSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefWOStatusFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_wo_status']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - WO - Ref WO Status.",
        description="Get Master Data - WO - Ref WO Status.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_wo_status.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - WO - Ref WO Status.",
        description="Create Master Data - WO - Ref WO Status.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_wo_status.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - WO - Ref WO Status (Specified).",
        description="Get Master Data - WO - Ref WO Status (Specified).",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_wo_status = self.queryset.filter(id_ref_wo_status=pk)
        if not ref_wo_status:
            return not_found('ref_wo_status.not_found')

        serializer = self.serializer_class(ref_wo_status, many=True)
        return response__(request, serializer, 'ref_wo_status.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - PM - Ref Jenis Lokasi.",
        description="Update Master Data - PM - Ref Jenis Lokasi.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        ref_wo_status = get_object_or_404(RefWOStatus, pk=pk)
        serializer = self.update_serializer_class(instance=ref_wo_status, data=request.data)

        return post_update_response(serializer, 'ref_wo_status.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - WO - Ref WO Status.",
        description="Delete Master Data - WO - Ref WO Status.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        ref_wo_status = get_object_or_404(RefWOStatus, pk=pk)
        self.perform_destroy(ref_wo_status)
        return response__(request, ref_wo_status, 'ref_wo_status.delete')

    def perform_destroy(self, instance):
        instance.delete()