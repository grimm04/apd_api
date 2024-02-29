 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action


from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import WP_ONLINE_PEKERJA
from .filters import WP_ONLINE_PEKERJAFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class WP_ONLINE_PEKERJAViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_ONLINE_PEKERJA.objects.all()
    serializer_class = serializers.WP_ONLINE_PEKERJASerializers 
    create_serializer_class = serializers.CDWP_ONLINE_PEKERJASerializers 
    update_serializer_class = serializers.UDWP_ONLINE_PEKERJASerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_ONLINE_PEKERJAFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = []  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_online_pekerja']

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - Online Pekerja.",
        description="Get Working Permit - Online Pekerja.",
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

        return get_response(self, request, queryset, 'wp_online_pekerja.view')


    @extend_schema(
        methods=["POST"],
        summary="Working Permit - Online Pekerja.",
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
        return post_update_response(serializer, 'wp_online_pekerja.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - Online Pekerja(Specified).",
        description="Get Working Permit - Online Pekerja(Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_online_pekerja = self.queryset.filter(id_wp_online_pekerja=pk)
        if not wp_online_pekerja:
            return not_found('wp_online_pekerja.not_found')

        serializer = self.serializer_class(wp_online_pekerja, many=True)
        return response__(request, serializer, 'wp_online_pekerja.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Online Pekerja",
        description="Update Working Permit - Online Pekerja",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_online_pekerja = get_object_or_404(WP_ONLINE_PEKERJA, pk=pk)
        serializer = self.update_serializer_class(instance=wp_online_pekerja, data=request.data)

        return post_update_response(serializer, 'wp_online_pekerja.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - Online Pekerja.",
        description="Delete Working Permit - Online Pekerja.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_online_pekerja = get_object_or_404(WP_ONLINE_PEKERJA, pk=pk)
        self.perform_destroy(wp_online_pekerja)
        return response__(request, wp_online_pekerja, 'wp_online_pekerja.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Online Pekerja Batch.",
        description="update Working Permit - Online Pekerja Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_online_pekerja')
    def update_batch(self, request,*args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instances = [] 
        for item in request.data: 
            instance = get_object_or_404(WP_ONLINE_PEKERJA, pk=int(item['id_wp_online_pekerja'])) 
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='wp_online_pekerja.update_failed')
        
        return response_basic(_status=True, results=instances, msg='wp_online_pekerja.update')  
            
     
     