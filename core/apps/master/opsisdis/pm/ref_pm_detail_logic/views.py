from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefPMDetailLogic
from .filters import RefPMDetailLogicFilter, SearchFilter, RefPMDetailLogic

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class RefPMDetailLogicViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefPMDetailLogic.objects.all()
    serializer_class = serializers.CRRefPMDetailLogicSerializers
    update_serializer_class = serializers.UDRefPMDetailLogicSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefPMDetailLogicFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_pm_detail_logic']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - PM - Ref PM Detail Logic.",
        description="Get Master Data - PM - Ref PM Detail Logic.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_pm_detail_logic.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Master Data - PM - Ref PM Detail Logic.",
        description="Create Master Data - PM - Ref PM Detail Logic.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'ref_pm_detail_logic.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - PM - Ref PM Detail Logic (Specified).",
        description="Get Master Data - PM - Ref PM Detail Logic (Specified).",
        tags=['master_opsisdis']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_pm_detail_logic = self.queryset.filter(id_ref_pm_detail_logic=pk)
        if not ref_pm_detail_logic:
            return not_found('ref_pm_detail_logic.not_found')

        serializer = self.serializer_class(ref_pm_detail_logic, many=True)
        return response__(request, serializer, 'ref_pm_detail_logic.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - PM - Ref Jenis Lokasi.",
        description="Update Master Data - PM - Ref Jenis Lokasi.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_opsisdis']
    )
    def update(self, request, pk):
        ref_pm_detail_logic = get_object_or_404(RefPMDetailLogic, pk=pk)
        serializer = self.update_serializer_class(instance=ref_pm_detail_logic, data=request.data)

        return post_update_response(serializer, 'ref_pm_detail_logic.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - PM - Ref PM Detail Logic.",
        description="Delete Master Data - PM - Ref PM Detail Logic.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_opsisdis']
    )
    def destroy(self, request, pk):
        ref_pm_detail_logic = get_object_or_404(RefPMDetailLogic, pk=pk)
        self.perform_destroy(ref_pm_detail_logic)
        return response__(request, ref_pm_detail_logic, 'ref_pm_detail_logic.delete')

    def perform_destroy(self, instance):
        instance.delete()