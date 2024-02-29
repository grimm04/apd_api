from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefDistrict
from .filters import SearchFilter, RefDistrictFilter

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from base.negotiation import CustomContentNegotiation


class RefDistrictViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefDistrict.objects.all()
    serializer_class = serializers.RefDistricterializer
    create_serializer_class = serializers.CRRefDistrictSerializers
    update_serializer_class = serializers.UDRefDistrictSerializers

    pagination_class = CustomPagination
    content_negotiation_class = CustomContentNegotiation

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefDistrictFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_district']

    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - Wilayah - Ref Districts.",
        description="Create Master Data - Wilayah - Ref Districts.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_wilayah']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'ref_district.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Wilayah - Ref Districts.",
        description="Get Master Data - Wilayah - Ref Districts.",
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

        return get_response(self, request, queryset, 'ref_district.view')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Wilayah - Ref Districts (Specified).",
        description="Get Master Data - Wilayah - Ref Districts (Specified).",
        tags=['master_wilayah']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_district = self.queryset.filter(pk=pk)
        if not ref_district :
            return not_found('ref_district.not_found')

        serializer = self.serializer_class(ref_district, many=True)
        return response__(request, serializer, 'ref_district.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Wilayah - Ref Districts.",
        description="Update Master Data - Wilayah - Ref Districts.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_wilayah']
    )
    def update(self, request, pk):
        ref_district = get_object_or_404(RefDistrict, pk=pk)
        serializer = self.update_serializer_class(instance=ref_district, data=request.data)

        return post_update_response(serializer, 'ref_province.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Wilayah - Ref Districts.",
        description="Delete Master Data - Wilayah - Ref Districts.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_wilayah']
    )
    def destroy(self, request, pk):
        ref_province = get_object_or_404(RefDistrict, pk=pk)
        self.perform_destroy(ref_province)
        return response__(request, ref_province, 'ref_province.delete')

    def perform_destroy(self, instance):
        instance.delete()
