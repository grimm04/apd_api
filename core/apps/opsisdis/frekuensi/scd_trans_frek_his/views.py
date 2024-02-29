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
from .models import FrekuensiHIS
from .filters import FrekuensiHISFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found, response_basic
from base.custom_pagination import CustomPagination

class FrekuensiHISViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = FrekuensiHIS.objects.all()
    serializer_class = serializers.FrekuensiHISSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = FrekuensiHISFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['id_meter', 'datum_2']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_meter']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSISDIS - Frekuensi Pembangkit - HIS",
        description="Get OPSISDIS - Frekuensi Pembangkit - HIS",
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

        return get_response(self, request, queryset, 'frekuensi_his.view')