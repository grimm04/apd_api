from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransWo
from .filters import TransWoFilter, SearchFilter, TransWo

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransWoViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransWo.objects.all()
    serializer_class = serializers.CRTransWoSerializers
    update_serializer_class = serializers.UDTransWoSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransWoFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nomor','uraian']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_wo']

    @extend_schema(
        methods=["GET"],
        summary="Get Trans WO",
        description="Get Trans WO",
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

        return get_response(self, request, queryset, 'trans_wo.view')

    @extend_schema(
        methods=["POST"],
        summary="Create trans WO.",
        description="Create trans WO.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        return post_update_response(serializer, 'trans_wo.create')

    @extend_schema(
        methods=["GET"],
        summary="Get trans WO (Specified).",
        description="Get trans WO (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_wo = self.queryset.filter(id_trans_wo=pk)
        if not trans_wo:
            return not_found('trans_wo.not_found')

        serializer = self.serializer_class(trans_wo, many=True)
        return response__(request, serializer, 'trans_wo.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Trans WO",
        description="Update Trans WO",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_wo = get_object_or_404(TransWo, pk=pk)
        serializer = self.update_serializer_class(instance=trans_wo, data=request.data)

        return post_update_response(serializer, 'trans_wo.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete trans.",
        description="Delete trans.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_wo = get_object_or_404(TransWo, pk=pk)
        self.perform_destroy(trans_wo)
        return response__(request, trans_wo, 'trans_wo.delete')

    def perform_destroy(self, instance):
        instance.delete()
 