from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransWoLogStatus
from .filters import TransWoLogStatusFilter, SearchFilter, TransWoLogStatus

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransWoLogStatusViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransWoLogStatus.objects.all()
    serializer_class = serializers.CRTransWoLogStatusSerializers
    update_serializer_class = serializers.UDTransWoLogStatusSerializers

    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = TransWoLogStatusFilter
    # filterset_fields = ['keyword']  # multi filter param
    # search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wo_log_status']

    @extend_schema(
        methods=["GET"],
        summary="Get Trans WO Log Status",
        description="Get Trans WO Log Status",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_wo_log_status.view')

    @extend_schema(
        methods=["POST"],
        summary="Create trans wo log status.",
        description="Create trans wo log status.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_wo_log_status.create')

    @extend_schema(
        methods=["GET"],
        summary="Get trans wo log status(Specified).",
        description="Get trans wo log status (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_wo_log_status = self.queryset.filter(id_wo_log_status=pk)
        if not trans_wo_log_status:
            return not_found('trans_wo_log_status.not_found')

        serializer = self.serializer_class(trans_wo_log_status, many=True)
        return response__(request, serializer, 'trans_wo_log_status.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update trans wo log status",
        description="Update trans wo log status",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_wo_log_status = get_object_or_404(TransWoLogStatus, pk=pk)
        serializer = self.update_serializer_class(instance=trans_wo_log_status, data=request.data)

        return post_update_response(serializer, 'trans_wo_log_status.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete trans wo log status.",
        description="Delete trans wo log status.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_wo_log_status = get_object_or_404(TransWoLogStatus, pk=pk)
        self.perform_destroy(trans_wo_log_status)
        return response__(request, trans_wo_log_status, 'trans_wo_log_status.delete')

    def perform_destroy(self, instance):
        instance.delete()
 