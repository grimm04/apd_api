from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefEpFiohl  
from .filters import SearchFilter, RefEpFiohlFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefEpFiohlViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefEpFiohl.objects.all()
    serializer_class = serializers.CRRefEpFiohlSerializers
    update_serializer_class = serializers.UDRefEpFiohlSerializers

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefEpFiohlFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_ep_fiohl']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Opsisdis - Ref Ep Fiohl.",
        description="Create Master Data - Opsisdis - Ref Ep Fiohl.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        

        return post_update_response(serializer, 'ref_ep_fiohl.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Ep Fiohl.",
        description="Get Master Data - Opsisdis - Ref Ep Fiohl.",
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
        
        return get_response(self, request, queryset, 'ref_ep_fiohl.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Opsisdis - Ref Ep Fiohl (Specified).",
        description="Get Master Data - Opsisdis - Ref Ep Fiohl (Specified).",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_ep_fiohl = self.queryset.filter(pk=pk)
        if not ref_ep_fiohl :
            return not_found('ref_ep_fiohl.not_found')

        serializer = self.serializer_class(ref_ep_fiohl, many=True)
        return response__(request, serializer, 'ref_ep_fiohl.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Opsisdis - Ref Ep Fiohl.",
        description="Update Master Data - Opsisdis - Ref Ep Fiohl.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        ref_ep_fiohl = get_object_or_404(RefEpFiohl, pk=pk)
        serializer = self.update_serializer_class(instance=ref_ep_fiohl, data=request.data)

        return post_update_response(serializer, 'ref_ep_fiohl.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Opsisdis - Ref Ep Fiohl.",
        description="Delete Master Data - Opsisdis - Ref Ep Fiohl.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        ref_ep_fiohl = get_object_or_404(RefEpFiohl, pk=pk)
        self.perform_destroy(ref_ep_fiohl)
        return response__(request, ref_ep_fiohl, 'ref_ep_fiohl.delete')

    def perform_destroy(self, instance):
        instance.delete()
