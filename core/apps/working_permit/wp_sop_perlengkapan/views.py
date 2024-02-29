 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication 


from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import WPSOPPerlengkapan
from .filters import WPSOPPerlengkapanFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class WPSOPPerlengkapanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WPSOPPerlengkapan.objects.all()
    serializer_class = serializers.WPSOPPerlengkapanSerializers  
    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WPSOPPerlengkapanFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_sop_perlengkapan']

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - WP SOP Perlengkapan.",
        description="Get Working Permit - WP SOP Perlengkapan.",
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

        return get_response(self, request, queryset, 'wp_sop_perlengkapan.view')


    @extend_schema(
        methods=["POST"],
        summary="Working Permit - WP SOP Perlengkapan.",
        description="Working Permit - Hirarc Single or Batch, Can Be Multiple create.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    # create
    def create(self, request):
        data = request.data
        many = False
        # if type(data) is list: 
        #     many = True   
        serializer = self.serializer_class(data=data, many=many) 
        return post_update_response(serializer, 'wp_sop_perlengkapan.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - WP SOP Perlengkapan (Specified).",
        description="Get Working Permit - WP SOP Perlengkapan (Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_sop_perlengkapan = self.queryset.filter(id_wp_sop_perlengkapan=pk)
        if not wp_sop_perlengkapan:
            return not_found('wp_sop_perlengkapan.not_found')

        serializer = self.serializer_class(wp_sop_perlengkapan, many=True)
        return response__(request, serializer, 'wp_sop_perlengkapan.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - WP SOP Perlengkapan",
        description="Update Working Permit - WP SOP Perlengkapan",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_sop_perlengkapan = get_object_or_404(WPSOPPerlengkapan, pk=pk)
        serializer = self.serializer_class(instance=wp_sop_perlengkapan, data=request.data)

        return post_update_response(serializer, 'wp_sop_perlengkapan.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - WP SOP Perlengkapan.",
        description="Delete Working Permit - WP SOP Perlengkapan.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_sop_perlengkapan = get_object_or_404(WPSOPPerlengkapan, pk=pk)
        self.perform_destroy(wp_sop_perlengkapan)
        return response__(request, wp_sop_perlengkapan, 'wp_sop_perlengkapan.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Working Permit - WP SOP Perlengkapan Batch.",
    #     description="update Working Permit - WP SOP Perlengkapan Batch, Can Be Multiple update.",
    #     request=serializer_class,
    #     responses=serializer_class,
    #     tags=['working_permit']
    # )
    # @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_hirarc_detail')
    # def update_batch(self, request,*args, **kwargs): 
    #     partial = kwargs.pop('partial', False)
    #     instances = [] 
    #     for item in request.data: 
    #         instance = get_object_or_404(wp_sop_perlengkapan, pk=int(item['id_wp_sop_perlengkapan'])) 
    #         serializer = self.serializer_class(instance, data=item, partial=partial)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         instances.append(serializer.data)
    #     if not instances:
    #         return response_basic(msg='wp_sop_perlengkapan.update_failed')
        
    #     return response_basic(_status=True, results=instances, msg='wp_sop_perlengkapan.update')  
            
     
     