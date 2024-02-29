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
from .models import REF_PEGAWAI
from .filters import REF_PEGAWAIFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class REF_PEGAWAIViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = REF_PEGAWAI.objects.all()
    serializer_class = serializers.REF_PEGAWAISerializers 
    create_serializer_class = serializers.CDREF_PEGAWAISerializers 
    update_serializer_class = serializers.UDREF_PEGAWAISerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = REF_PEGAWAIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['tanggal','lokasi_pekerjaan','pekerjaan']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_pegawai']

    @extend_schema(
        methods=["GET"],
        summary="Get Master Pegawai - User.",
        description="Get Master Pegawai - User.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'ref_pegawai.view')


    @extend_schema(
        methods=["POST"],
        summary="Master Pegawai - User.",
        description="Master Pegawai - User Single or Batch, Can Be Multiple create.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_pegawai']
    )
    # create
    def create(self, request):
        data = request.data
        many = False
        # if type(data) is list: 
        #     many = True   
        serializer = self.create_serializer_class(data=data, many=many) 
        return post_update_response(serializer, 'ref_pegawai.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Master Pegawai - User (Specified).",
        description="Get Master Pegawai - User (Specified).",
        tags=['master_pegawai']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        ref_pegawai = self.queryset.filter(pk=pk)
        if not ref_pegawai:
            return not_found('REF_PEGAWAI.not_found')

        serializer = self.serializer_class(ref_pegawai, many=True)
        return response__(request, serializer, 'ref_pegawai.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Master Pegawai - User",
        description="Update Master Pegawai - User",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['master_pegawai']
    )
    def update(self, request, pk):
        ref_pegawai = get_object_or_404(REF_PEGAWAI, pk=pk)
        serializer = self.update_serializer_class(instance=ref_pegawai, data=request.data)

        return post_update_response(serializer, 'REF_PEGAWAI.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Master Pegawai - User.",
        description="Delete Master Pegawai - User.",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_pegawai']
    )
    def destroy(self, request, pk):
        ref_pegawai = get_object_or_404(REF_PEGAWAI, pk=pk)
        self.perform_destroy(ref_pegawai)
        return response__(request, ref_pegawai, 'REF_PEGAWAI.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Master Pegawai - User Batch.",
    #     description="update Master Pegawai - User Batch, Can Be Multiple update.",
    #     request=update_serializer_class,
    #     responses=update_serializer_class,
    #     tags=['master_pegawai']
    # )
    # @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_hirarc')
    # def update_batch(self, request,*args, **kwargs): 
    #     partial = kwargs.pop('partial', False)
    #     instances = [] 
    #     for item in request.data: 
    #         instance = get_object_or_404(REF_PEGAWAI, pk=int(item['id_pegawai'])) 
    #         serializer = self.update_serializer_class(instance, data=item, partial=partial)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         instances.append(serializer.data)
    #     if not instances:
    #         return response_basic(msg='REF_PEGAWAI.update_failed')
        
    #     return response_basic(_status=True, results=instances, msg='REF_PEGAWAI.update')  
            
     
     