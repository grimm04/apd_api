 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action


from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import WP_QRC_TMP
from .filters import WP_QRC_TMPFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class WP_QRC_TMPViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_QRC_TMP.objects.all()
    serializer_class = serializers.WP_QRC_TMPSerializers 
    create_serializer_class = serializers.CDWP_QRC_TMPSerializers 
    update_serializer_class = serializers.UDWP_QRC_TMPSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_QRC_TMPFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['ada']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_qrc_tmp']

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - QRC TMP.",
        description="Get Working Permit - QRC TMP.",
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

        return get_response(self, request, queryset, 'wp_qrc_tmp.view')


    @extend_schema(
        methods=["POST"],
        summary="Working Permit - QRC TMP.",
        description="Working Permit - QRC TMP Single or Batch, Can Be Multiple create.",
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
        return post_update_response(serializer, 'wp_qrc_tmp.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - QRC TMP (Specified).",
        description="Get Working Permit - QRC TMP (Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_qrc_tmp = self.queryset.filter(id_wp_qrc_tmp=pk)
        if not wp_qrc_tmp:
            return not_found('wp_qrc_tmp.not_found')

        serializer = self.serializer_class(wp_qrc_tmp, many=True)
        return response__(request, serializer, 'wp_qrc_tmp.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - QRC TMP",
        description="Update Working Permit - QRC TMP",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_qrc_tmp = get_object_or_404(wp_qrc_tmp, pk=pk)
        serializer = self.update_serializer_class(instance=wp_qrc_tmp, data=request.data)

        return post_update_response(serializer, 'wp_qrc_tmp.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - QRC TMP.",
        description="Delete Working Permit - QRC TMP.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_qrc_tmp = get_object_or_404(WP_QRC_TMP, pk=pk)
        self.perform_destroy(wp_qrc_tmp)
        return response__(request, wp_qrc_tmp, 'wp_qrc_tmp.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - QRC TMP Batch.",
        description="update Working Permit - QRC TMP Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_qrc_tmp')
    def update_batch(self, request,*args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instances = [] 
        for item in request.data: 
            instance = get_object_or_404(WP_QRC_TMP, pk=int(item['id_wp_qrc_tmp'])) 
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='wp_qrc_tmp.update_failed')
        
        return response_basic(_status=True, results=instances, msg='wp_qrc_tmp.update')  
            
     
     