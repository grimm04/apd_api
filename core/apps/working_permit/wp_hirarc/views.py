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
from .models import WP_HIRARC
from .filters import WP_HIRARCFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

#pdf
from .export import html_to_pdf 
# importing the necessary libraries
from django.http import HttpResponse 
from django.template.loader import render_to_string

class WP_HIRARCViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_HIRARC.objects.all()
    serializer_class = serializers.WP_HIRARCSerializers 
    create_serializer_class = serializers.CDWP_HIRARCSerializers 
    update_serializer_class = serializers.UDWP_HIRARCSerializers
    generate_serializer_class = serializers.Generate_HIRARCSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_HIRARCFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['tanggal','lokasi_pekerjaan','pekerjaan']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_hirarc']

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - Hirarc.",
        description="Get Working Permit - Hirarc.",
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

        return get_response(self, request, queryset, 'wp_hirarc.view')


    @extend_schema(
        methods=["POST"],
        summary="Working Permit - Hirarc.",
        description="Working Permit - Hirarc Single or Batch, Can Be Multiple create.",
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
        return post_update_response(serializer, 'wp_hirarc.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - Hirarc (Specified).",
        description="Get Working Permit - Hirarc (Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_hirarc = self.queryset.filter(id_wp_hirarc=pk)
        if not wp_hirarc:
            return not_found('wp_hirarc.not_found')

        serializer = self.serializer_class(wp_hirarc, many=True)
        return response__(request, serializer, 'wp_hirarc.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Hirarc",
        description="Update Working Permit - Hirarc",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_hirarc = get_object_or_404(WP_HIRARC, pk=pk)
        serializer = self.update_serializer_class(instance=wp_hirarc, data=request.data)

        return post_update_response(serializer, 'wp_hirarc.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - Hirarc.",
        description="Delete Working Permit - Hirarc.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_hirarc = get_object_or_404(WP_HIRARC, pk=pk)
        self.perform_destroy(wp_hirarc)
        return response__(request, wp_hirarc, 'wp_hirarc.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Hirarc Batch.",
        description="update Working Permit - Hirarc Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_hirarc')
    def update_batch(self, request,*args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instances = [] 
        for item in request.data: 
            instance = get_object_or_404(WP_HIRARC, pk=int(item['id_wp_hirarc'])) 
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='wp_hirarc.update_failed')
        
        return response_basic(_status=True, results=instances, msg='wp_hirarc.update')  


class GenerateHirarcViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_HIRARC.objects.all()
    serializer_class = serializers.Generate_HIRARCSerializers 

    @extend_schema(
        methods=["GET"],
        summary="Generate PDF Working Permit - Hirarc.",
        description="Generate PDF Working Permit - Hirarc, Generate PDF.", 
        tags=['working_permit']
    )
    def retrieve(self, request, pk):
        wp_hirarc = self.queryset.filter(id_wp_hirarc=pk)
        if not wp_hirarc:
            return not_found('wp_hirarc.not_found')

        serializer = self.serializer_class(wp_hirarc, many=True)
        # print(serializer.data[0])
        open('templates/export/hirarc_temp.html', "w").write(render_to_string('export/wp_hirarc.html', {'data': serializer.data[0]}))
        # getting the template
        pdf = html_to_pdf('export/hirarc_temp.html','hirarc')   
        response = HttpResponse(pdf, content_type='application/octet-stream') 
        response['Content-Disposition'] = 'attachment; filename={}.pdf'.format('hirarc') 
        return response
        
        return response__(request, serializer, 'wp_hirarc.view')
        
     
     