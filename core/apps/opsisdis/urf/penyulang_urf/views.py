from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend 

from rest_framework import viewsets, response, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from apps.master.jaringan.ref_lokasi.models import RefLokasi  
from .filters import PenyulangUFRFilter, SearchFilter
from apps.master.jaringan.ref_lokasi.models import RefLokasi 

from base.response import get_response, response_basic ,validate_serializer, error_response,response_json
from base.custom_pagination import CustomPagination   
 
class PenyulangUFRViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasi.objects.filter(id_ref_jenis_lokasi=6)
    queryset_ref_lokasi = RefLokasi.objects.all()
    serializer_class = serializers.PenyulangUFRSerializer
    update_serializer_class = serializers.UpdatePenyulangUFRSerializer  
    pagination_class = CustomPagination 

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = PenyulangUFRFilter
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi','id_parent_lokasi_id__id_parent_lokasi_id__nama_lokasi']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_ref_lokasi']

    @extend_schema(
        methods=["GET"],
        summary="Get OPSIS - UFR - Penyulang",
        description="Get OPSIS - UFR - Penyulang",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            # OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            # OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['opsis_ufr']
    )
    def list(self, request): 
        queryset = self.filter_queryset(self.get_queryset())

        return get_response(self, request, queryset, 'penyulang_ufr.view')
  

    # @extend_schema(
    #     methods=["PUT"],
    #     summary="Update OPSIS - UFR - Penyulang",
    #     description="Update OPSIS - UFR - Penyulang",
    #     request=update_serializer_class,
    #     responses=update_serializer_class,
    #     tags=['opsis_ufr']
    # )
    # def update(self, request):
    #     # penyulang_ufr = get_object_or_404(RefLokasi, pk=pk) 
    #     # serializer = self.serializer_class(penyulang_ufr, many=False)  
    #     # penyulang = serializer.data  
    #     serializer = self.update_serializer_class(instance=penyulang_ufr, data=request.data)
    #     data_json = validate_serializer(serializer, s=True)  

    #     if data_json.get('error') == True: 
    #         return error_response(data_json.get('data'))  

        # if 'no_urut_cell' in request.data: 
        #     id_lokasi = penyulang['id_lokasi']
        #     #update no_urut_cell
        #     penyulang_no_urut =  RefLokasi.objects.filter(id_lokasi=id_lokasi)
        #     no_urut_cell = request.data['no_urut_cell']
        #     u_no_urut_cell = penyulang_no_urut.update(no_urut_cell=no_urut_cell)
        #     if u_no_urut_cell:
        #         ref_lokasi = RefLokasi.objects.filter(id_ref_lokasi=id_lokasi) 
        #         ref_lokasi.update(no_urut=no_urut_cell) 

        return response_json(data = data_json.get('data'), msg ='penyulang_ufr.update') 
    
    @extend_schema(
        methods=["POST"],
        summary="Update OPSIS - UFR - Penyulang",
        description="Update OPSIS - UFR - Penyulang",
        request=update_serializer_class,
        responses=update_serializer_class,
        tags=['opsis_ufr']
    )
    @action(detail=False, methods=['POST'], url_path='update', url_name='update_ufr')
    def update_batch(self, request, *args, **kwargs):

        data = request.data
        if data :
            id_ref_lokasi = data['id_ref_lokasi']
            ufr = data['ufr']
            u = RefLokasi.objects.filter(id_ref_lokasi__in=id_ref_lokasi)
            if u: 
                u.update(ufr=int(ufr)) 
        return response_basic(_status=True, msg='penyulang_ufr.update')
 