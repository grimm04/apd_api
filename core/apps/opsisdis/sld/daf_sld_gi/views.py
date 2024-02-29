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
from .models import DAF_SLD_GI
from .filters import DAF_SLD_GIFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class DAF_SLD_GIViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = DAF_SLD_GI.objects.all()
    serializer_class = serializers.DAF_SLD_GISerializers 
    create_serializer_class = serializers.CDDAF_SLD_GISerializers 
    update_serializer_class = serializers.UDDAF_SLD_GISerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = DAF_SLD_GIFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['kelompok','nama_file','keterangan']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_daf_sld_gi']

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - SLD.",
        description="Get Opsisdis - SLD.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_sld']
    )
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'daf_sld_gi.view')


    @extend_schema(
        methods=["POST"],
        summary="Opsisdis - SLD.",
        description="Opsisdis - SLD create.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['opsisdis_sld']
    )
    # create
    def create(self, request):
        data = request.data
        many = False
        # if type(data) is list: 
        #     many = True   
        serializer = self.create_serializer_class(data=data, many=many) 
        return post_update_response(serializer, 'daf_sld_gi.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Opsisdis - SLD (Specified).",
        description="Get Opsisdis - SLD (Specified).",
        tags=['opsisdis_sld']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        daf_sld_gi = self.queryset.filter(pk=pk)
        if not daf_sld_gi:
            return not_found('daf_sld_gi.not_found')

        serializer = self.serializer_class(daf_sld_gi, many=True)
        return response__(request, serializer, 'daf_sld_gi.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Opsisdis - SLD",
        description="Update Opsisdis - SLD",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsisdis_sld']
    )
    def update(self, request, pk):
        daf_sld_gi = get_object_or_404(DAF_SLD_GI, pk=pk)
        serializer = self.update_serializer_class(instance=daf_sld_gi, data=request.data)

        return post_update_response(serializer, 'DAF_SLD_GI.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Opsisdis - SLD.",
        description="Delete Opsisdis - SLD.",
        request=serializer_class,
        responses=serializer_class,
        tags=['opsisdis_sld']
    )
    def destroy(self, request, pk):
        daf_sld_gi = get_object_or_404(DAF_SLD_GI, pk=pk)
        self.perform_destroy(daf_sld_gi)
        return response__(request, daf_sld_gi, 'DAF_SLD_GI.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update Opsisdis - SLD Batch.",
    #     description="update Opsisdis - SLD Batch, Can Be Multiple update.",
    #     request=update_serializer_class,
    #     responses=update_serializer_class,
    #     tags=['opsisdis_sld']
    # )
    # @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_hirarc')
    # def update_batch(self, request,*args, **kwargs): 
    #     partial = kwargs.pop('partial', False)
    #     instances = [] 
    #     for item in request.data: 
    #         instance = get_object_or_404(DAF_SLD_GI, pk=int(item['id_DAF_SLD_GI'])) 
    #         serializer = self.update_serializer_class(instance, data=item, partial=partial)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         instances.append(serializer.data)
    #     if not instances:
    #         return response_basic(msg='DAF_SLD_GI.update_failed')
        
    #     return response_basic(_status=True, results=instances, msg='DAF_SLD_GI.update')  
            
     
     