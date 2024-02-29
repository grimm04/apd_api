from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import WP_BAGIAN 
from . import serializers
from .filters import SearchFilter, WP_BAGIANFilter

from base.response import   get_response 
from base.custom_pagination import CustomPagination


# Create your views here.
class WP_BAGIANViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_BAGIAN.objects.all()
    serializer_class = serializers.WP_BAGIANSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_BAGIANFilter
    filterset_fields = [  'keyword']   # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_master_bagian']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Working Permit - Master - Bagian",
        description="Get Data Working Permit - Master - Bagian",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def list(self, request):  
        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'wp_bagian.view')  
  