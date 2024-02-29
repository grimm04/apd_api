from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefProvince
from .filters import SearchFilter, RefProvinceFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefProvinceViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefProvince.objects.all()
    serializer_class = serializers.RefProvincSerializers
    create_serializer_class = serializers.CRRefProvinceSerializers
    update_serializer_class = serializers.UDRefProvinceSerializers

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefProvinceFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_province']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Wilayah - Ref Province.",
        description="Create Master Data - Wilayah - Ref Province.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_wilayah']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'ref_province.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Wilayah - Ref Province.",
        description="Get Master Data - Wilayah - Ref Province.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_wilayah']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_province.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Wilayah - Ref Province (Specified).",
        description="Get Master Data - Wilayah - Ref Province (Specified).",
        tags=['master_wilayah']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_province = self.queryset.filter(pk=pk)
        if not ref_province :
            return not_found('ref_province.not_found')

        serializer = self.serializer_class(ref_province, many=True)
        return response__(request, serializer, 'ref_province.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Wilayah - Ref Province.",
        description="Update Master Data - Wilayah - Ref Province.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_wilayah']
    )
    def update(self, request, pk):
        ref_province = get_object_or_404(RefProvince, pk=pk)
        serializer = self.update_serializer_class(instance=ref_province, data=request.data)

        return post_update_response(serializer, 'ref_province.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Wilayah - Ref Province.",
        description="Delete Master Data - Wilayah - Ref Province.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_wilayah']
    )
    def destroy(self, request, pk):
        ref_province = get_object_or_404(RefProvince, pk=pk)
        self.perform_destroy(ref_province)
        return response__(request, ref_province, 'ref_province.delete')

    def perform_destroy(self, instance):
        instance.delete()
