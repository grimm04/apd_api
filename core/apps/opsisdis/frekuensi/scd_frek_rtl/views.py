import json
from imp import PKG_DIRECTORY
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import FrekuensiRTL
from .filters import FrekuensiRTLFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found, response_basic, exists
from base.custom_pagination import CustomPagination

class FrekuensiRTLViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = FrekuensiRTL.objects.all()
    serializer_class = serializers.FrekuensiRTLSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = FrekuensiRTLFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['id_meter', 'datum_2']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_meter']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Frekuensi Pembangkit - RTL",
        description="Get OPSISDIS - Frekuensi Pembangkit - RTL",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_frekuensi']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'frekuensi_rtl.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Data OPSISDIS - Frekuensi Pembangkit - RTL.",
        description="Create Data OPSISDIS - Frekuensi Pembangkit - RTL.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_frekuensi']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'frekuensi_rtl.create')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified OPSISDIS - Frekuensi Pembangkit - RTL",
        description="Get Details OPSISDIS - Frekuensi Pembangkit - RTL",
        tags=['opsisdis_frekuensi']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        frekuensi_rtl = self.queryset.filter(id_meter=pk)
        if frekuensi_rtl is None:
            return not_found('frekuensi_rtl.not_found')

        serializer = self.serializer_class(frekuensi_rtl, many=True)
        return response__(request, serializer, 'frekuensi_rtl.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data OPSISDIS - Frekuensi Pembangkit - RTL.",
        description="Update Data OPSISDIS - Frekuensi Pembangkit - RTL.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_frekuensi']
    )
    def update(self, request, pk):
        frekuensi_rtl = get_object_or_404(FrekuensiRTL, pk=pk)
        serializer = self.serializer_class(instance=frekuensi_rtl, data=request.data)

        return post_update_response(serializer, 'frekuensi_rtl.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data OPSISDIS - Frekuensi Pembangkit - RTL.",
        description="Delete Data OPSISDIS - Frekuensi Pembangkit - RTL.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_frekuensi']
    )
    def destroy(self, request, pk):
        frekuensi_rtl = get_object_or_404(FrekuensiRTL, pk=pk)
        self.perform_destroy(frekuensi_rtl)
        return response__(request, frekuensi_rtl, 'frekuensi_rtl.delete')

    def perform_destroy(self, instance):
        instance.delete()