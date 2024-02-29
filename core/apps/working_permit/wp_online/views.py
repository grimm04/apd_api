 
from datetime import datetime
import roman 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, response ,status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN


from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import WP_ONLINE
from .filters import WP_ONLINEFilter, SearchFilter

from base.response import response__, get_response, post_update_response, not_found,response_basic
from base.custom_pagination import CustomPagination 

class WP_ONLINEViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = WP_ONLINE.objects.all()
    serializer_class = serializers.WP_ONLINESerializers 
    create_serializer_class = serializers.CDWP_ONLINESerializers 
    update_serializer_class = serializers.UDWP_ONLINESerializers 
    update_aproval_serializer_class = serializers.UDAPROVALWP_ONLINESerializers 
    reject_serializer_class = serializers.UDREJECTWP_ONLINESerializers 

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = WP_ONLINEFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_koordinator_vendor','lokasi_pekerjaan','pekerjaan_dilakukan','nama_pengawas','nama_pengawask3']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_wp_online']

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - online.",
        description="Get Working Permit - online.",
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

        return get_response(self, request, queryset, 'wp_online.view')


    @extend_schema(
        methods=["POST"],
        summary="Working Permit - online.",
        description="Working Permit - online Single or Batch, Can Be Multiple create.",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['working_permit']
    )
    # create
    def create(self, request):
        data = request.data
        nf = self.getNomorFormulir(req=request) 
        data['nomor_formulir'] = nf
        many = False
        if type(data) is list: 
            many = True   
        serializer = self.create_serializer_class(data=data, many=many) 
        return post_update_response(serializer, 'wp_online.create')

    @extend_schema(
        methods=["GET"],
        summary="Get Working Permit - online (Specified).",
        description="Get Working Permit - online (Specified).",
        tags=['working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        wp_online = self.queryset.filter(id_wp_online=pk)
        if not wp_online:
            return not_found('wp_online.not_found')

        serializer = self.serializer_class(wp_online, many=True)
        return response__(request, serializer, 'wp_online.view')
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - online",
        description="Update Working Permit - online",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    def update(self, request, pk):
        wp_online = get_object_or_404(WP_ONLINE, pk=pk)
        serializer = self.update_serializer_class(instance=wp_online, data=request.data)

        return post_update_response(serializer, 'wp_online.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Working Permit - online.",
        description="Delete Working Permit - online.",
        request=serializer_class,
        responses=serializer_class,
        tags=['working_permit']
    )
    def destroy(self, request, pk):
        wp_online = get_object_or_404(WP_ONLINE, pk=pk)
        self.perform_destroy(wp_online)
        return response__(request, wp_online, 'wp_online.delete')

    def perform_destroy(self, instance):
        instance.delete()  
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - online Batch.",
        description="update Working Permit - online Batch, Can Be Multiple update.",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='update-batch', url_name='update_batch_wp_online')
    def update_batch(self, request,*args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instances = [] 
        for item in request.data: 
            instance = get_object_or_404(WP_ONLINE, pk=int(item['id_wp_online'])) 
            serializer = self.update_serializer_class(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)
        if not instances:
            return response_basic(msg='wp_online.update_failed')
        
        return response_basic(_status=True, results=instances, msg='wp_online.update')  

    @extend_schema(
        methods=["GET"],
        summary=" Working Permit - online Get Count.",
        description=" Working Permit - online Get Count ",
        request=None,
        responses=None,
        tags=['working_permit']
    )
    @action(detail=False, methods=['GET'], url_path='online-dashboard', url_name='get_dashboard') 
    def get_count(self, request, *args, **kwargs): 
        total = WP_ONLINE.objects.count()
        disetujui = WP_ONLINE.objects.filter(status_persetujuan=1).count()
        belumdisetujui=WP_ONLINE.objects.filter(status_persetujuan=0).count()
        data = {
            "total": total,
            "disetujui": disetujui,
            "belumdisetujui": belumdisetujui,
        }
        # print(data)
        raw_response = {
            "status": status.HTTP_200_OK,
            "message": 'Berhasi mendapatkan data wp online dashboard',
            "results": data
        }  
        return response.Response(data=raw_response, status=status.HTTP_200_OK)

            
     
    def getNomorFormulir(self, req=None): 
        last_invoice = WP_ONLINE.objects.count()
        id_wp_master_bagian = req.data['id_wp_master_bagian'] 
        bag = WP_BAGIAN.objects.filter(id_wp_master_bagian=id_wp_master_bagian).values('ept')  
        if bag :
            if not last_invoice:
                nf = 1  
            new_invoice_int = last_invoice + 1
            # #nomor/bagian/bulan/UP2D/tahun  
            new_nf = str(new_invoice_int) + '/' + bag[0]['ept'] + '/' + str(roman.toRoman(datetime.now().month))+ '/UP2D/' + str(datetime.now().year)
            return new_nf 
    
    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Aproval WP",
        description="Update Working Permit - Aproval WP",
        request=update_aproval_serializer_class,
        responses=update_aproval_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='aproval-wp/(?P<id_wp_online>\d+)', url_name='update-approval-wp') 
    def update_aproval(self, request, id_wp_online):
        wp_online = get_object_or_404(WP_ONLINE, pk=id_wp_online)
        request.data['tgl_persetujuan'] = datetime.now() 
        serializer = self.update_aproval_serializer_class(instance=wp_online, data=request.data) 
        return post_update_response(serializer, 'wp_online.update')

    @extend_schema(
        methods=["PUT"],
        summary="Update Working Permit - Reject WP",
        description="Update Working Permit - Reject WP",
        request=reject_serializer_class,
        responses=reject_serializer_class,
        tags=['working_permit']
    )
    @action(detail=False, methods=['PUT'], url_path='reject-wp/(?P<id_wp_online>\d+)', url_name='reject-wp') 
    def reject_aproval(self, request, id_wp_online):
        wp_online = get_object_or_404(WP_ONLINE, pk=id_wp_online)
        serializer = self.reject_serializer_class(instance=wp_online, data=request.data) 
        return post_update_response(serializer, 'wp_online.reject')