from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefEpCuaca  
from .filters import SearchFilter, RefEpCuacaFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefEpCuacaViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefEpCuaca.objects.all()
    serializer_class = serializers.RefEpCuacaserializer 

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefEpCuacaFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_ep_cuaca']
 
    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Ep Cuaca.",
        description="Get Master Data - Opsisdis - Ref Ep Cuaca.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()) 
        
        return get_response(self, request, queryset, 'ref_ep_cuaca.view')
 