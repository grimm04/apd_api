from rest_framework import serializers
from .models import ApprovalManagementWP
from apps.master.pegawai.jabatan.models import Jabatan
from apps.master.pegawai.departemen.models import Departemen
from apps.users.models import Users

class SubRefJabatanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jabatan
        fields = ['id_jabatan', 'nama']

class SubRefUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id_user', 'fullname']

class SubRefDepartemenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departemen
        fields = ['id_departemen', 'nama']

class ApprovalManagementWPSerializers(serializers.ModelSerializer):
    id_approval_management_wp = serializers.IntegerField()
    jabatan = SubRefJabatanSerializer(read_only=True, source='id_jabatan')
    user = SubRefUsersSerializer(read_only=True, source='id_user')
    departemen = SubRefDepartemenSerializer(read_only=True, source='id_departemen')
    nama_pegawai = serializers.CharField(max_length=500)
    nama_jabatan = serializers.CharField(max_length=500)
    nama_bagian = serializers.CharField(max_length=500)

    class Meta:
        model = ApprovalManagementWP
        fields = '__all__'

class CRApprovalManagementWPSerializers(serializers.ModelSerializer):
    id_jabatan = serializers.SlugRelatedField(
        queryset=Jabatan.objects.all(),
        slug_field='id_jabatan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_departemen = serializers.SlugRelatedField(
        queryset=Departemen.objects.all(),
        slug_field='id_departemen',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = ApprovalManagementWP
        fields = ['id_user', 'id_jabatan', 'id_departemen']

class UDApprovalManagementWPSerializers(serializers.ModelSerializer):
    id_jabatan = serializers.SlugRelatedField(
        queryset=Jabatan.objects.all(),
        slug_field='id_jabatan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_departemen = serializers.SlugRelatedField(
        queryset=Departemen.objects.all(),
        slug_field='id_departemen',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = ApprovalManagementWP
        fields = ['id_user', 'id_jabatan', 'id_departemen']


class IApprovalManagementWPSerializers(serializers.ModelSerializer):
    nama_pegawai = serializers.CharField(max_length=500)
    nama_jabatan = serializers.CharField(max_length=500)
    nama_bagian = serializers.CharField(max_length=500)
    id_jabatan = serializers.SlugRelatedField(
        queryset=Jabatan.objects.all(),
        slug_field='id_jabatan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_departemen = serializers.SlugRelatedField(
        queryset=Departemen.objects.all(),
        slug_field='id_departemen',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = ApprovalManagementWP
        fields = '__all__'