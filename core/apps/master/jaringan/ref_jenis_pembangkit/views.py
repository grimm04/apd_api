from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefJenisPembangkit  , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import SearchFilter, RefJenisPembangkitFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefJenisPembangkitViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefJenisPembangkit.objects.all()
    serializer_class = serializers.CRRefJenisPembangkitSerializers
    update_serializer_class = serializers.UDRefJenisPembangkitSerializers

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefJenisPembangkitFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_jenis_pembangkit']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Jaringan - Ref Jenis Pembangkit.",
        description="Create Master Data - Jaringan - Ref Jenis Pembangkit.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        

        return post_update_response(serializer, 'ref_jenis_pembangkit.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Pembangkit.",
        description="Get Master Data - Jaringan - Ref Jenis Pembangkit.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default='xlsx'), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        action_serializer = self.serializer_class
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Ref Jenis Pembangkit'
        
        return get_response(self, request, queryset, 'ref_jenis_pembangkit.view', action_serializer=action_serializer,headers=header, relation=relation, fields=fields,title=title)

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Jaringan - Ref Jenis Lokasi (Specified).",
        description="Get Master Data - Jaringan - Ref Jenis Lokasi (Specified).",
        tags=['master_jaringan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_jenis_pembangkit = self.queryset.filter(pk=pk)
        if not ref_jenis_pembangkit :
            return not_found('ref_jenis_pembangkit.not_found')

        serializer = self.serializer_class(ref_jenis_pembangkit, many=True)
        return response__(request, serializer, 'ref_jenis_pembangkit.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Jaringan - Ref Jenis Pembangkit.",
        description="Update Master Data - Jaringan - Ref Jenis Pembangkit.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_jaringan']
    )
    def update(self, request, pk):
        ref_jenis_pembangkit = get_object_or_404(RefJenisPembangkit, pk=pk)
        serializer = self.update_serializer_class(instance=ref_jenis_pembangkit, data=request.data)

        return post_update_response(serializer, 'ref_jenis_pembangkit.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Jaringan - Ref Jenis Pembangkit.",
        description="Delete Master Data - Jaringan - Ref Jenis Pembangkit.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def destroy(self, request, pk):
        ref_jenis_pembangkit = get_object_or_404(RefJenisPembangkit, pk=pk)
        self.perform_destroy(ref_jenis_pembangkit)
        return response__(request, ref_jenis_pembangkit, 'ref_jenis_pembangkit.delete')

    def perform_destroy(self, instance):
        instance.delete()
