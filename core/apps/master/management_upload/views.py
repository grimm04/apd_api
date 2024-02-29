from array import array
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from drf_spectacular.utils import extend_schema, OpenApiParameter
 
from .models import managementUpload
from library.api_response import ApiResponse, build_response
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from rest_framework.decorators import action
from apps.master.jaringan.ref_lokasi.models import RefLokasiTemp, RefLokasiTempDelete
from apps.master.jaringan.ref_lokasi.filters import RefLokasiFilterTemp, SearchFilter
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializerTemp, CRRefLokasiSerializers, UDRefLokasiSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from datetime import datetime

class ManagemetUploadTempView(viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    model = managementUpload()

    queryset = RefLokasiTemp.objects.all()
    pagination_class = CustomPagination

    serializer_class = RefLokasiSerializerTemp
    create_serializer_class = CRRefLokasiSerializers
    update_serializer_class = UDRefLokasiSerializers

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = RefLokasiFilterTemp
    filterset_fields = ['keyword']  # multi filter param
    search_fields = ['nama_lokasi', 'alamat']  # multi filter field
    ordering_fields = '__all__'
    ordering = ['id_user_entri']

    @extend_schema(
        methods=['GET'],
        summary="Get List Data Temp.",
        description="Get List Menu Temp.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_management_upload']
    )
    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())

            return get_response(self, request, queryset, 'ref_lokasi.view')
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

    @extend_schema(
        methods=['POST'],
        summary="Post Data Temp to Production.",
        description="Post Data Temp to Production.",
        parameters=[
            OpenApiParameter(name='id_user', description='id_user', required=True, type=int), 
            OpenApiParameter(name='id_ref_jenis_lokasi', description='multiple, split by comma.',
                             required=False, type=str),
        ],
        tags=['master_management_upload'],
        request=serializer_class,
        responses=serializer_class
    )
    def create(self, request):
        try:
            id_user = request.GET.get('id_user')
            id_ref_jenis_lokasi = request.GET.get('id_ref_jenis_lokasi')
            # _, message = self.model.read_temp_all(id_ref_jenis_lokasi=id_ref_jenis_lokasi, id_user_entri=id_user)
            id_ref_jenis_lokasi = id_ref_jenis_lokasi.strip()
            id_ref_jenis_lokasi = id_ref_jenis_lokasi.split(',')  
            q_set = self.get_queryset().filter(id_ref_jenis_lokasi__in=id_ref_jenis_lokasi).filter(id_user_entri=id_user) 
            if not q_set:
                return build_response(ApiResponse(message=str(message))) 
            serializer = self.serializer_class(q_set, many=True).data
            for row in serializer:
                print(row['nama_lokasi'])
                data = dict(
                    kode_lokasi=row['kode_lokasi'],
                    nama_lokasi=row['nama_lokasi'],
                    id_parent_lokasi=row['id_parent_lokasi'],
                    tree_jaringan=row['tree_jaringan'],
                    alamat=row['alamat'],
                    coverage=row['coverage'],
                    kva=row['kva'],
                    phase=row['phase'],
                    id_user_entri=row['id_user_entri'],
                    id_user_update=row['id_user_update'],
                    lat=row['lat'],
                    lon=row['lon'],
                    id_ref_jenis_lokasi=row['id_ref_jenis_lokasi'],
                    status_listrik=row['status_listrik'],
                    no_tiang=row['no_tiang'],
                    jenis_jaringan=row['jenis_jaringan'],
                    no_urut=row['no_urut'],
                    status_penyulang=row['status_penyulang'],
                    pemilik=row['pemilik'], 
                    i_max=row['i_max'], 
                    dcc=row['dcc'], 
                    ratio_ct=row['ratio_ct'], 
                    ratio_vt=row['ratio_vt'], 
                    faktor_kali=row['faktor_kali'], 
                    jenis_gi=row['jenis_gi'],
                    fungsi_scada=row['fungsi_scada'], 
                    id_uid=row['id_uid'],
                    id_up3_1=row['id_up3_1'],
                    id_up2b=row['id_up2b'],
                    id_ulp_1=row['id_ulp_1'],
                    id_gardu_induk=row['id_gardu_induk'],
                    id_trafo_gi=row['id_trafo_gi'],
                    id_penyulang=row['id_penyulang'],
                    id_zone=row['id_zone'],
                    id_section=row['id_section'],
                    id_segment=row['id_segment'],
                )
                event = row['event_upload']
                if event == 'INSERT':
                    exist, message = self.model.read_data(nama_lokasi=row['nama_lokasi'], table='ref_lokasi')
                    if exist:
                        data['tgl_update'] = datetime.now().strftime('%Y-%m-%d')
                        _, message = self.model.update_data(data, row['nama_lokasi'], table='ref_lokasi')
                        if not _:
                            return build_response(ApiResponse(message=str(message)))
                    else:
                        data['tgl_entri'] = datetime.now().strftime('%Y-%m-%d')
                        _, message = self.model.create_data(data, table='ref_lokasi')
                        if not _:
                            return build_response(ApiResponse(message=str(message)))
                elif event == 'UPDATE':
                    data['tgl_update'] = datetime.now().strftime('%Y-%m-%d')
                    _, message = self.model.update_data(data, row['nama_lokasi'], table='ref_lokasi')
                    if not _:
                        return build_response(ApiResponse(message=str(message)))
                elif event == 'DELETE':
                    _, message = self.model.delete_data(row['nama_lokasi'], table='ref_lokasi')
                    if not _:
                        return build_response(ApiResponse(message=str(message)))

            q_set = q_set.delete()   
            # if not _:
            #     return build_response(ApiResponse(message=str(message)))

            return build_response(ApiResponse(status=True, message='Success insert to table production'))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))

class ManagemetUploadDataView(viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    model = managementUpload()

    queryset = RefLokasiTempDelete.objects.all()
    pagination_class = CustomPagination

    @extend_schema(
        methods=['DELETE'],
        summary="Delete temporary data.",
        description="Delete temporary by id_user and id_ref_jenis_lokasi.",
        tags=['master_management_upload'],
        parameters=[
            OpenApiParameter(name='id_ref_jenis_lokasi', description='id_ref_jenis_lokasi', required=True, type=int)
        ],
    )
    def destroy(self, request, pk):
        try:
            id_ref_jenis_lokasi = request.GET.get('id_ref_jenis_lokasi')
            _, message = self.model.delete_data_temp(id_user=pk, id_ref_jenis_lokasi=id_ref_jenis_lokasi, table='ref_lokasi_temp_upload')
            if not _:
                return build_response(ApiResponse(message=str(message)))

            return build_response(ApiResponse(status=True, message='Success data from table temprorary'))
        except Exception as e:
            return build_response(ApiResponse(message=str(e)))