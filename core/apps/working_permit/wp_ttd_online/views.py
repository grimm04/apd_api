from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import WP_TTD_ONLINE 
from . import serializers
from .filters import SearchFilter, WP_TTD_ONLINEFilter

from base.response import response__, get_response, post_update_response, not_found 
from base.custom_pagination import CustomPagination


# Create your views here.
class WP_TTD_ONLINEViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_TTD_ONLINE.objects.all()
    serializer_class = serializers.WP_TTD_ONLINESerializers 
    create_serializer_class = serializers.CDWP_TTD_ONLINESerializers 
    update_serializer_class = serializers.UDWP_TTD_ONLINESerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_TTD_ONLINEFilter
    filterset_fields = [  'keyword']   # multi filter param
    search_fields = ['nama','nama_file','group_file']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_ttd_online']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Working Permit - TTD Online",
        description="Get Data Working Permit - TTD Online",
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
        return get_response(self, request, queryset, 'wp_ttd_online.view')  

    

    @extend_schema(
        methods=["POST"],
        summary="Working Permit - TTD Online.",
        description="Working Permit - TTD Online Single or Batch, Can Be Multiple create.",
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
        return post_update_response(serializer, 'wp_ttd_online.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - TTD Online (Specified).",
        description="Get Working Permit - TTD Online (Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_ttd_online = self.queryset.filter(id_wp_ttd_online=pk)
        if not wp_ttd_online:
            return not_found('wp_ttd_online.not_found')

        serializer = self.serializer_class(wp_ttd_online, many=True)
        return response__(request, serializer, 'wp_ttd_online.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - TTD Online",
        description="Update Working Permit - TTD Online",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_ttd_online = get_object_or_404(WP_TTD_ONLINE, pk=pk)
        serializer = self.update_serializer_class(instance=wp_ttd_online, data=request.data)

        return post_update_response(serializer, 'wp_ttd_online.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - TTD Online.",
        description="Delete Working Permit - TTD Online.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_ttd_online = get_object_or_404(WP_TTD_ONLINE, pk=pk)
        self.perform_destroy(wp_ttd_online)
        return response__(request, wp_ttd_online, 'wp_ttd_online.delete')

    def perform_destroy(self, instance):
        instance.delete()  
  