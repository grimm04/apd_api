from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransEpPeralatan
from .filters import TransEpPeralatanFilter, SearchFilter, TransEpPeralatan

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransEpPeralatanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransEpPeralatan.objects.all()
    serializer_class = serializers.TransEpPeralatanSerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransEpPeralatanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['tegangan','status_s','status_g']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_ep_peralatan']

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Peralatan",
        description="Get Opsisdis - Rekap Padam - Trans Ep Peralatan",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'trans_ep_peralatan.view')


    @extend_schema(
        methods=["POST"],
        summary="Create Opsisdis - Rekap Padam - Trans Ep Peralatan",
        description="Create Opsisdis - Rekap Padam - Trans Ep Peralatan",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_ep_peralatan.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - Rekap Padam - Trans Ep Peralatan (Specified).",
        description="Get Opsisdis - Rekap Padam - Trans Ep Peralatan (Specified).",
        tags=['opsisdis_rekap_padam']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_ep_peralatan = self.queryset.filter(id_trans_ep_peralatan=pk)
        if not trans_ep_peralatan:
            return not_found('trans_ep_peralatan.not_found')

        serializer = self.serializer_class(trans_ep_peralatan, many=True)
        return response__(request, serializer, 'trans_ep_peralatan.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - Opsisdis -  Trans Ep Peralatan",
        description="Update Opsisdis - Opsisdis -  Trans Ep Peralatan",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def update(self, request, pk):
        trans_ep_peralatan = get_object_or_404(TransEpPeralatan, pk=pk)
        serializer = self.serializer_class(instance=trans_ep_peralatan, data=request.data)

        return post_update_response(serializer, 'trans_ep_peralatan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - Rekap Padam - Trans Ep Peralatan",
        description="Delete Opsisdis - Rekap Padam - Trans Ep Peralatan",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_rekap_padam']
    )
    def destroy(self, request, pk):
        trans_ep_peralatan = get_object_or_404(TransEpPeralatan, pk=pk)
        self.perform_destroy(trans_ep_peralatan)
        return response__(request, trans_ep_peralatan, 'trans_ep_peralatan.delete')

    def perform_destroy(self, instance):
        instance.delete()