from imp import PKG_DIRECTORY
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response ,status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action


from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefAsetExtAtr
from .filters import RefAsetExtAtrFilter, SearchFilter, RefAsetExtAtr

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class RefAsetExtAtrViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefAsetExtAtr.objects.all()
    serializer_class = serializers.CDRefAsetExtAtrSerializers 
    update_serializer_class = serializers.UDRefAsetExtAtrSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefAsetExtAtrFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_file','status','tipe','jenis']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_aset_ext_atr']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Aset - Ref Aset Ext Atr.",
        description="Get Master Data - Aset - Ref Aset Ext Atr.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_aset_ext_atr.view')


    @extend_schema(
        methods=["POST"],
        summary="Master Data - Aset - Ref Aset Ext Atr.",
        description="Master Data - Aset - Ref Aset Ext Atr Single or Batch, Can Be Multiple create.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    # create
    def create(self, request):
        data = request.data
        many = False
        if type(data) is list: 
            many = True   
        serializer = self.serializer_class(data=data, many=many) 
        return post_update_response(serializer, 'ref_aset_ext_atr.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Aset - Ref Aset Ext Atr (Specified).",
        description="Get Master Data - Aset - Ref Aset Ext Atr (Specified).",
        tags=['master_aset']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_aset_ext_atr = self.queryset.filter(id_ref_aset_ext_atr=pk)
        if not ref_aset_ext_atr:
            return not_found('ref_aset_ext_atr.not_found')

        serializer = self.serializer_class(ref_aset_ext_atr, many=True)
        return response__(request, serializer, 'ref_aset_ext_atr.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Aset - Ref Aset Doc",
        description="Update Master Data - Aset - Ref Aset Doc",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_aset']
    )
    def update(self, request, pk):
        ref_aset_ext_atr = get_object_or_404(RefAsetExtAtr, pk=pk)
        serializer = self.update_serializer_class(instance=ref_aset_ext_atr, data=request.data)

        return post_update_response(serializer, 'ref_aset_ext_atr.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Data - Aset - Ref Aset Ext Atr.",
        description="Delete Master Data - Aset - Ref Aset Ext Atr.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_aset']
    )
    def destroy(self, request, pk):
        ref_aset_ext_atr = get_object_or_404(RefAsetExtAtr, pk=pk)
        self.perform_destroy(ref_aset_ext_atr)
        return response__(request, ref_aset_ext_atr, 'ref_aset_ext_atr.delete')

    def perform_destroy(self, instance):
        instance.delete() 
    # @extend_schema(
    #     methods=["POST"],
    #     summary="Master Data - Aset - Ref Aset Ext Atr.",
    #     description="Master Data - Aset - Ref Aset Ext Atr Single or Batch, Can Be Multiple create.",
    #     request=serializer_class,
    #     responses=serializer_class,
    #     tags=['master_aset']
    # )
    # @action(detail=False, methods=['POST'], url_path='create-batch', url_name='create_batch_aset_ext_atr')
    # def insert_batch(self, request): 
    #     print(type(request.data) is list)
    #     serializer   =   self.serializer_class(data = request.data,many=True)  
    #     return post_update_response(serializer, 'ref_aset_ext_atr.create')  
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Data - Aset - Ref Aset Ext Atr Batch.",
        description="update Master Data - Aset - Ref Aset Ext Atr Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_aset']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_aset_ext_atr')
    def update_batch(self, request,*args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instances = [] 
        for item in request.data: 
            instance = get_object_or_404(RefAsetExtAtr, pk=int(item['id_ref_aset_ext_atr'])) 
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='ref_aset_ext_atr.update_failed')
        
        return response_basic(_status=True, results=instances, msg='ref_aset_ext_atr.update')  
            
     
     