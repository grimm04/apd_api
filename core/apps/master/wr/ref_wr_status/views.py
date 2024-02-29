from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefWRStatus
from .filters import RefWRStatusFilter, SearchFilter, RefWRStatus

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class RefWRStatusViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefWRStatus.objects.all()
    serializer_class = serializers.CRRefWRStatusSerializers
    update_serializer_class = serializers.UDRefWRStatusSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefWRStatusFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wr_status']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - WR - Ref WR Status.",
        description="Get Master Data - WR - Ref WR Status.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_wr']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_wr_status.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - WR - Ref WR Status.",
        description="Create Master Data - WR - Ref WR Status.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_wr']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_wr_status.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - WO - Ref RO StatusR(Specified).",
        description="Get Master Data - WO - Ref RO StatusR(Specified).",
        tags=['master_wr']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_wr_status = self.queryset.filter(id_wr_status=pk)
        if not ref_wr_status:
            return not_found('ref_wr_status.not_found')

        serializer = self.serializer_class(ref_wr_status, many=True)
        return response__(request, serializer, 'ref_wr_status.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - PM - Ref Jenis Lokasi.",
        description="Update Master Data - PM - Ref Jenis Lokasi.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_wr']
    )
    def update(self, request, pk):
        ref_wr_status = get_object_or_404(RefWRStatus, pk=pk)
        serializer = self.update_serializer_class(instance=ref_wr_status, data=request.data)

        return post_update_response(serializer, 'ref_wr_status.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - WR - Ref WR Status.",
        description="Delete Master Data - WR - Ref WR Status.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_wr']
    )
    def destroy(self, request, pk):
        ref_wr_status = get_object_or_404(RefWRStatus, pk=pk)
        self.perform_destroy(ref_wr_status)
        return response__(request, ref_wr_status, 'ref_wr_status.delete')

    def perform_destroy(self, instance):
        instance.delete()