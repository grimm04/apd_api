from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransPMDetail
from .filters import TransPMDetailFilter, SearchFilter, TransPMDetail

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransPMDetailViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransPMDetail.objects.all()
    serializer_class = serializers.GetTransPMDetailSerializers
    create_serializer_class = serializers.CRTransPMDetailSerializers
    update_serializer_class = serializers.UDTransPMDetailSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransPMDetailFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama','nilai_acuan','nilai_pemeriksaan','satuan','kesimpulan']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_pm_detail']

    @extend_schema(
        methods=["GET"],
        summary="Get Trans PM Detail",
        description="Get Trans PM Detail",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_pm_detail.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Trans PM Detail.",
        description="Create Trans PM Detail.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'trans_pm_detail.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Trans PM Detail (Specified).",
        description="Get Trans PM Detail (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_pm_detail = self.queryset.filter(id_wo=pk)
        if not trans_pm_detail:
            return not_found('trans_pm_detail.not_found')

        serializer = self.serializer_class(trans_pm_detail, many=True)
        return response__(request, serializer, 'trans_pm_detail.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Trans PM Detail",
        description="Update Trans PM Detail",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_pm_detail = get_object_or_404(TransPMDetail, pk=pk)
        serializer = self.update_serializer_class(instance=trans_pm_detail, data=request.data)

        return post_update_response(serializer, 'trans_pm_detail.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete trans.",
        description="Delete trans.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_pm_detail = get_object_or_404(TransPMDetail, pk=pk)
        self.perform_destroy(trans_pm_detail)
        return response__(request, trans_pm_detail, 'trans_pm_detail.delete')

    def perform_destroy(self, instance):
        instance.delete()
 