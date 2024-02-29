from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import FASOPPATH3 , EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, FASOPPATH3Filter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination


class Path3View(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = FASOPPATH3.objects.all()
    serializer_class = serializers.FASOPPATH3Serializers
    create_serializer_class = serializers.CRFASOPPATH3CSerializers
    update_serializer_class = serializers.UDFASOPPATH3Serializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = FASOPPATH3Filter
    filterset_fields = ['keyword']
    search_fields = ['path1','path2','path3']
    ordering_fields = '__all__'
    ordering = ['id']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Fasop Path 3",
        description="Get Data Fasop Path 3",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def list(self, request):
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Path 3'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'fasop_path_3.view',headers=header, relation=relation, fields=fields,title=title)  

    @extend_schema(
        methods=["POST"],
        summary="Create Data Fasop Path 3",
        description="Create Data Fasop Path 3",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_fasop']
    )
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'fasop_path_3.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Fasop Path 3",
        description="Get Details Fasop Path 3",
        tags=['master_fasop']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        fasop_path_3 = self.queryset.filter(pk=pk)
        if not fasop_path_3:
            return not_found('fasop_path_3.not_found')

        serializer = self.serializer_class(fasop_path_3, many=True)
        return response__(request, serializer, 'fasop_path_3.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Fasop Path 3",
        description="Update Data Fasop Path 3",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_fasop']
    )
    def update(self, request, pk):
        fasop_path_3 = get_object_or_404(FASOPPATH3, pk=pk)
        serializer = self.update_serializer_class(instance=fasop_path_3, data=request.data)
        return post_update_response(serializer, 'fasop_path_3.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Fasop Path 3",
        description="Delete Data Fasop Path 3",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_fasop']
    )
    def destroy(self, request, pk):
        fasop_path_3 = get_object_or_404(FASOPPATH3, pk=pk)
        self.perform_destroy(fasop_path_3)
        return response__(request, fasop_path_3, 'fasop_path_3.delete')

    def perform_destroy(self, instance):
        instance.delete()
