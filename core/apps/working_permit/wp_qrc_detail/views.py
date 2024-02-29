 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action


from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import WP_QRC_DETAIL
from .filters import WP_QRC_DETAILFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class WP_QRC_DETAILViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_QRC_DETAIL.objects.all()
    serializer_class = serializers.WP_QRC_DETAILSerializers 
    create_serializer_class = serializers.CDWP_QRC_DETAILSerializers 
    update_serializer_class = serializers.UDWP_QRC_DETAILSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_QRC_DETAILFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['ada']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_qrc_detail']

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - QRC DETAIL.",
        description="Get Working Permit - QRC DETAIL.",
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

        return get_response(self, request, queryset, 'wp_qrc_detail.view')


    @extend_schema(
        methods=["POST"],
        summary="Working Permit - QRC DETAIL.",
        description="Working Permit - QRC Single or Batch, Can Be Multiple create.",
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
        return post_update_response(serializer, 'wp_qrc_detail.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - QRC Detail(Specified).",
        description="Get Working Permit - QRC Detail(Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_qrc_detail = self.queryset.filter(id_wp_qrc_detail=pk)
        if not wp_qrc_detail:
            return not_found('wp_qrc_detail.not_found')

        serializer = self.serializer_class(wp_qrc_detail, many=True)
        return response__(request, serializer, 'wp_qrc_detail.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - QRC DETAIL",
        description="Update Working Permit - QRC DETAIL",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_qrc_detail = get_object_or_404(WP_QRC_DETAIL, pk=pk)
        serializer = self.update_serializer_class(instance=wp_qrc_detail, data=request.data)

        return post_update_response(serializer, 'wp_qrc_detail.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - QRC DETAIL.",
        description="Delete Working Permit - QRC DETAIL.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_qrc_detail = get_object_or_404(WP_QRC_DETAIL, pk=pk)
        self.perform_destroy(wp_qrc_detail)
        return response__(request, wp_qrc_detail, 'wp_qrc_detail.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - QRC Detail Batch.",
        description="update Working Permit - QRC Detail Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_qrc_detail')
    def update_batch(self, request,*args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instances = [] 
        for item in request.data: 
            instance = get_object_or_404(WP_QRC_DETAIL, pk=int(item['id_wp_qrc_detail'])) 
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='wp_qrc_detail.update_failed')
        
        return response_basic(_status=True, results=instances, msg='wp_qrc_detail.update')  
            
     
     