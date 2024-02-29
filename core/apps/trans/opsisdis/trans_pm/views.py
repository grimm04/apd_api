from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import TransPM
from .filters import TransPMFilter, SearchFilter, TransPM

from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination 

class TransPMViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = TransPM.objects.all()
    serializer_class = serializers.GetTransPMSerializers
    create_serializer_class = serializers.CRTransPMSerializers
    update_serializer_class = serializers.UDTransPMSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = TransPMFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['bobot_total_standar','bobot_total_hasil','level_pm','kesimpulan','status']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_trans_pm']

    @extend_schema(
        methods=["GET"],
        summary="Get Trans PM",
        description="Get Trans PM",
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

        return get_response(self, request, queryset, 'trans_pm.view')

    @extend_schema(
        methods=["POST"],
        summary="Create Trans PM.",
        description="Create Trans PM.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    # create
    def create(self, request):
        data = request.data
        serializer = self.create_serializer_class(data=data)

        return post_update_response(serializer, 'trans_pm.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Trans PM (Specified).",
        description="Get Trans PM (Specified).",
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        trans_pm = self.queryset.filter(id_wo=pk)
        if not trans_pm:
            return not_found('trans_pm.not_found')

        serializer = self.serializer_class(trans_pm, many=True)
        return response__(request, serializer, 'trans_pm.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Trans PM",
        description="Update Trans PM",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def update(self, request, pk):
        trans_pm = get_object_or_404(TransPM, pk=pk)
        serializer = self.update_serializer_class(instance=trans_pm, data=request.data)

        return post_update_response(serializer, 'trans_pm.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete trans.",
        description="Delete trans.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_jadwal_pemeliharaan']
    )
    def destroy(self, request, pk):
        trans_pm = get_object_or_404(TransPM, pk=pk)
        self.perform_destroy(trans_pm)
        return response__(request, trans_pm, 'trans_pm.delete')

    def perform_destroy(self, instance):
        instance.delete()
 