from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import JenisPenyebabGangguan
from . import serializers
from .filters import SearchFilter, JenisPenyebabGangguanFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


# Create your views here.
class JenisPenyebabGangguanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = JenisPenyebabGangguan.objects.all()
    serializer_class = serializers.CRJenisPenyebabGangguanSerializers
    # update_serializer_class = serializers.UDDepartemenSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = JenisPenyebabGangguanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_jenis_penyebab_gangguan']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Jenis Penyebab Gangguan.",
        description="Get Data Jenis Penyebab Gangguan.",
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

        return get_response(self, request, queryset, 'opsisdis_jenis_penyebab_gangguan.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Data Jenis Penyebab Gangguan.",
        description="Create Data Jenis Penyebab Gangguan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'opsisdis_jenis_penyebab_gangguan.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified Jenis Penyebab Gangguan",
        description="Get Details Jenis Penyebab Gangguan",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        departemen = self.queryset.filter(id_jenis_penyebab_gangguan=pk)
        if departemen is None:
            return not_found('opsisdis_jenis_penyebab_gangguan.not_found')

        serializer = self.serializer_class(departemen, many=True)
        return response__(request, serializer, 'opsisdis_jenis_penyebab_gangguan.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Jenis Penyebab Gangguan.",
        description="Update Data Jenis Penyebab Gangguan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        departemen = get_object_or_404(JenisPenyebabGangguan, pk=pk)
        serializer = self.serializer_class(instance=departemen, data=request.data)

        return post_update_response(serializer, 'opsisdis_jenis_penyebab_gangguan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Jenis Penyebab Gangguan.",
        description="Delete Data Jenis Penyebab Gangguan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        departemen = get_object_or_404(JenisPenyebabGangguan, pk=pk)
        self.perform_destroy(departemen)
        return response__(request, departemen, 'opsisdis_penyebab_gangguan.delete')

    def perform_destroy(self, instance):
        instance.delete()
