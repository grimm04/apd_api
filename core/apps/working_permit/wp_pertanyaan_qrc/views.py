from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import WP_PERTANYAAN_QRC 
from . import serializers
from .filters import SearchFilter, WP_PERTANYAAN_QRCFilter

from base.response import response__, get_response, post_update_response, not_found 
from base.custom_pagination import CustomPagination


# Create your views here.
class WP_PERTANYAAN_QRCViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_PERTANYAAN_QRC.objects.all()
    serializer_class = serializers.WP_PERTANYAAN_QRCSerializers 
    create_serializer_class = serializers.CDWP_PERTANYAAN_QRCSerializers 
    update_serializer_class = serializers.UDWP_PERTANYAAN_QRCSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_PERTANYAAN_QRCFilter
    filterset_fields = [  'keyword']   # multi filter param
    search_fields = ['name']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_pertanyaan_qrc']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Working Permit - Master - Bagian",
        description="Get Data Working Permit - Master - Bagian",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10), 
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def list(self, request):  
        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'wp_pertanyaan_qrc.view')  

    

    @extend_schema(
        methods=["POST"],
        summary="Working Permit - Pertanyaan QRC.",
        description="Working Permit - Pertanyaan QRC Single or Batch, Can Be Multiple create.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['working_permit']
    )
    # create
    def create(self, request):
        data = request.data
        many = False
        if type(data) is list: 
            many = True   
        serializer = self.create_serializer_class(data=data, many=many) 
        return post_update_response(serializer, 'wp_pertanyaan_qrc.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - Pertanyaan QRC (Specified).",
        description="Get Working Permit - Pertanyaan QRC (Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_pertanyaan_qrc = self.queryset.filter(id_wp_pertanyaan_qrc=pk)
        if not wp_pertanyaan_qrc:
            return not_found('wp_pertanyaan_qrc.not_found')

        serializer = self.serializer_class(wp_pertanyaan_qrc, many=True)
        return response__(request, serializer, 'wp_pertanyaan_qrc.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Pertanyaan QRC",
        description="Update Working Permit - Pertanyaan QRC",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_pertanyaan_qrc = get_object_or_404(WP_PERTANYAAN_QRC, pk=pk)
        serializer = self.update_serializer_class(instance=wp_pertanyaan_qrc, data=request.data)

        return post_update_response(serializer, 'wp_pertanyaan_qrc.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - Pertanyaan QRC.",
        description="Delete Working Permit - Pertanyaan QRC.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_pertanyaan_qrc = get_object_or_404(WP_PERTANYAAN_QRC, pk=pk)
        self.perform_destroy(wp_pertanyaan_qrc)
        return response__(request, wp_pertanyaan_qrc, 'wp_pertanyaan_qrc.delete')

    def perform_destroy(self, instance):
        instance.delete()  
  