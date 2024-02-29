from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import ApprovalManagementWP ,EXPORT_HEADERS, EXPORT_RELATION_FIELD, EXPORT_FIELDS
from . import serializers
from .filters import SearchFilter, ApprovalManagementWPFilter
from base.response import response__, get_response, post_update_response, not_found
from base.custom_pagination import CustomPagination
from apps.master.pegawai.jabatan.models import Jabatan
from apps.master.pegawai.jabatan.serializers import CRJabatanSerializers
from apps.master.pegawai.departemen.models import Departemen
from apps.master.pegawai.departemen.serializers import CRDepartemenSerializers
from apps.users.models import Users
from apps.users.serializers import UserListSerializer

class ApprovalManagementWPView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = ApprovalManagementWP.objects.all()
    users = Users.objects.all()
    user_serializer_class = UserListSerializer
    jabatan = Jabatan.objects.all()
    jabatan_serializer_class = CRJabatanSerializers
    departemen = Departemen.objects.all()
    departemen_serializer_class = CRDepartemenSerializers
    serializer_class = serializers.ApprovalManagementWPSerializers
    create_serializer_class = serializers.CRApprovalManagementWPSerializers
    update_serializer_class = serializers.UDApprovalManagementWPSerializers
    insert_serializer_class = serializers.IApprovalManagementWPSerializers

    pagination_class = CustomPagination

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ApprovalManagementWPFilter
    filterset_fields = ['keyword']
    search_fields = ['nama_pegawai', 'nama_jabatan']
    ordering_fields = '__all__'
    ordering = ['id_approval_management_wp']

    @extend_schema(
        methods=["GET"],
        summary="Get Data Approval Management WP",
        description="Get Data Approval Management WP",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='export', description='True=1', required=False, type=bool, default=False),
            OpenApiParameter(name='export_type', description='Type = xlsx,csv', required=False, type=str, default=None),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def list(self, request): 
        header      = EXPORT_HEADERS
        relation    = EXPORT_RELATION_FIELD
        fields      = EXPORT_FIELDS
        title        = 'Approval Management WP'

        queryset = self.filter_queryset(self.get_queryset())  
        return get_response(self, request, queryset, 'approval_management_wp.view',headers=header, relation=relation, fields=fields,title=title) 

    @extend_schema(
        methods=["POST"],
        summary="Create Data Approval Management WP",
        description="Create Data Approval Management WP",
        request=create_serializer_class,
        responses=create_serializer_class,
        tags=['master_working_permit']
    )
    def create(self, request):
        data = request.data
        id_user = data['id_user']
        nama_pegawai = self.users.filter(pk=data['id_user'])
        if not nama_pegawai:
            return not_found('users.not_found')
        nama_pegawai = self.user_serializer_class(nama_pegawai, many=True)
        id_jabatan = data['id_jabatan']
        nama_jabatan = self.jabatan.filter(pk=data['id_jabatan'])
        if not nama_jabatan:
            return not_found('jabatan.not_found')
        nama_jabatan = self.jabatan_serializer_class(nama_jabatan, many=True)
        id_departemen = data['id_departemen']
        nama_bagian = self.departemen.filter(pk=data['id_departemen'])
        if not nama_bagian:
            return not_found('departemen.not_found')
        nama_bagian = self.jabatan_serializer_class(nama_bagian, many=True)
        data = {
            'id_user': id_user,
            'nama_pegawai': nama_pegawai.data[0]['fullname'],
            'id_jabatan': id_jabatan,
            'nama_jabatan': nama_jabatan.data[0]['nama'],
            'id_departemen': id_departemen,
            'nama_bagian': nama_bagian.data[0]['nama']
        }
        serializer = self.insert_serializer_class(data=data)

        return post_update_response(serializer, 'approval_management_wp.create')

    @extend_schema(
        methods=["GET"],
        summary="Display speciffied Approval Management WP",
        description="Get Details Approval Management WP",
        tags=['master_working_permit']
    )
    def retrieve(self, request, pk, *args, **kwargs):
        approval_management_wp = self.queryset.filter(pk=pk)
        if not approval_management_wp:
            return not_found('approval_management_wp.not_found')

        serializer = self.serializer_class(approval_management_wp, many=True)
        return response__(request, serializer, 'approval_management_wp.view')

    @extend_schema(
        methods=["PUT"],
        summary="Update Data Approval Management WP",
        description="Update Data Approval Management WP",
        request=update_serializer_class,
        responses=insert_serializer_class,
        tags=['master_working_permit']
    )
    def update(self, request, pk):
        approval_management_wp = get_object_or_404(ApprovalManagementWP, pk=pk)
        id_user = request.data['id_user']
        nama_pegawai = self.users.filter(pk=request.data['id_user'])
        if not nama_pegawai:
            return not_found('users.not_found')
        nama_pegawai = self.user_serializer_class(nama_pegawai, many=True)
        id_jabatan = request.data['id_jabatan']
        nama_jabatan = self.jabatan.filter(pk=request.data['id_jabatan'])
        if not nama_jabatan:
            return not_found('jabatan.not_found')
        nama_jabatan = self.jabatan_serializer_class(nama_jabatan, many=True)
        id_departemen = request.data['id_departemen']
        nama_bagian = self.departemen.filter(pk=request.data['id_departemen'])
        if not nama_bagian:
            return not_found('departemen.not_found')
        nama_bagian = self.jabatan_serializer_class(nama_bagian, many=True)
        data = {
            'id_user': id_user,
            'nama_pegawai': nama_pegawai.data[0]['fullname'],
            'id_jabatan': id_jabatan,
            'nama_jabatan': nama_jabatan.data[0]['nama'],
            'id_departemen': id_departemen,
            'nama_bagian': nama_bagian.data[0]['nama']
        }
        serializer = self.insert_serializer_class(instance=approval_management_wp, data=data)
        return post_update_response(serializer, 'approval_management_wp.update')

    @extend_schema(
        methods=["DELETE"],
        summary="Delete Data Approval Management WP",
        description="Delete Data Approval Management WP",
        request=serializer_class,
        responses=serializer_class,
        tags=['master_working_permit']
    )
    def destroy(self, request, pk):
        approval_management_wp = get_object_or_404(ApprovalManagementWP, pk=pk)
        self.perform_destroy(approval_management_wp)
        return response__(request, approval_management_wp, 'approval_management_wp.delete')

    def perform_destroy(self, instance):
        instance.delete()
