from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefAsetLevel  , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from .filters import RefAsetLevelFilter, SearchFilter, RefAsetLevel

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class RefAsetLevelViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefAsetLevel.objects.all()
    serializer_class = serializers.CRRefAsetLevelSerializers
    serializer_action_classes = {
        'list': serializers.RefAsetLevelSerializersList, 
    }
    update_serializer_class = serializers.UDRefAsetLevelSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefAsetLevelFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_aset_level']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Aset - Ref Aset Rak.",
        description="Get Master Data - Aset - Ref Aset Rak.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None), 
        ],
        request=serializer_action_classes['list'],
        responses=serializer_action_classes['list'],
        tags=['master_aset']
    )
    def list(self, request): 
        action_serializer = self.serializer_action_classes['list']
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Level Aset'

        queryset = self.filter_queryset(self.get_queryset())
        return get_response(self, request, queryset, 'ref_aset_level.view', action_serializer=action_serializer,headers=header, relation=relation, fields=fields,title=title)  


    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Aset - Ref Aset Rak.",
        description="Create Master Data - Aset - Ref Aset Rak.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_aset_level.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Aset - Ref Aset Rak (Specified).",
        description="Get Master Data - Aset - Ref Aset Rak (Specified).",
        tags=['master_aset']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_aset_level = self.queryset.filter(id_ref_aset_level=pk)
        if not ref_aset_level:
            return not_found('ref_aset_level.not_found')

        serializer = self.serializer_class(ref_aset_level, many=True)
        return response__(request, serializer, 'ref_aset_level.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Aset - Ref Jenis Lokasi.",
        description="Update Master Data - Aset - Ref Jenis Lokasi.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_aset']
    )
    def update(self, request, pk):
        ref_aset_level = get_object_or_404(RefAsetLevel, pk=pk)
        serializer = self.update_serializer_class(instance=ref_aset_level, data=request.data)

        return post_update_response(serializer, 'ref_aset_level.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Aset - Ref Aset Rak.",
        description="Delete Master Data - Aset - Ref Aset Rak.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    def destroy(self, request, pk):
        ref_aset_level = get_object_or_404(RefAsetLevel, pk=pk)
        self.perform_destroy(ref_aset_level)
        return response__(request, ref_aset_level, 'ref_aset_level.delete')

    def perform_destroy(self, instance):
        instance.delete()