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
from .models import FrekuensiTH
from .filters import FrekuensiTHFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found, response_basic, exists
from base.custom_pagination import CustomPagination

class FrekuensiTHViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = FrekuensiTH.objects.all()
    serializer_class = serializers.FrekuensiTHSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = FrekuensiTHFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['id_meter', 'datum_2']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_meter']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Frekuensi Pembangkit - Eksekusi",
        description="Get OPSISDIS - Frekuensi Pembangkit - Eksekusi",
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

        return get_response(self, request, queryset, 'frekuensi_th.view')

    @extend_schema(
        methods=["GET"],
        summary="Display Specified OPSISDIS - Frekuensi Pembangkit - Eksekusi",
        description="Get Details OPSISDIS - Frekuensi Pembangkit - Eksekusi",
        tags=['opsisdis_frekuensi']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        frekuensi_th = self.queryset.filter(id_frek_th=pk)
        if frekuensi_th is None:
            return not_found('frekuensi_th.not_found')

        serializer = self.serializer_class(frekuensi_th, many=True)
        return response__(request, serializer, 'frekuensi_th.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update OPSISDIS - Frekuensi Pembangkit - Eksekusi",
        description="Update OPSISDIS - Frekuensi Pembangkit - Eksekusi",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_frekuensi']
    )
    def update(self, request, pk):
        frekuensi_th = get_object_or_404(FrekuensiTH, pk=pk)
        serializer = self.serializer_class(instance=frekuensi_th, data=request.data)

        return post_update_response(serializer, 'frekuensi_th.update')