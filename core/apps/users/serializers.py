from email.policy import default
from rest_framework import serializers
from apps.users.models import Users
from rest_framework.validators import UniqueValidator
from apps.master.pegawai.departemen.models import Departemen
from apps.master.pegawai.jabatan.models import Jabatan
from apps.master.pegawai.perusahaan.models import Perusahaan
from apps.master.pegawai.ref_regu_petugas.models import REF_REGU_PETUGAS_MODELS 
from apps.roles.models import Roles


class GetDepartemen(serializers.ModelSerializer):
    class Meta:
        model = Departemen
        fields = '__all__'


class GetJabatan(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = '__all__'


class GetPerusahaan(serializers.ModelSerializer):
    class Meta:
        model = Perusahaan
        fields = '__all__'

class GetReguPetugas(serializers.ModelSerializer):
    class Meta:
        model = REF_REGU_PETUGAS_MODELS
        fields = '__all__' 

class GetRole(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id','name','level']
        # extra_kwargs = {'name': {'write_only': True}}


class UserListSerializer(serializers.ModelSerializer):
    departemen = GetDepartemen(read_only=True, source='id_departemen')
    jabatan = GetJabatan(read_only=True, source='id_jabatan')
    perusahaan = GetPerusahaan(read_only=True, source='id_perusahaan')
    regu_petugas = GetReguPetugas(read_only=True, source='id_ref_regu_petugas')
    role = GetRole(read_only=True, source='roleId')

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id_user', 'fullname']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    roleId = serializers.SlugRelatedField(
        queryset=Roles.objects.all(),
        slug_field='id',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    # roleId = serializers.IntegerField(default=None, allow_null=True, required=False)
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message="Email Already Taken",
        )]) 
    username = serializers.CharField(allow_null=True, min_length=8 ,required=False, validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message="Username Already Taken",
        )])
        
    # username = serializers.CharField(allow_null=True, required=False)
    password = serializers.CharField(write_only=True, default=None, min_length=8,allow_null=True, required=False)
    is_active = serializers.BooleanField(default=True)
    akses_login = serializers.BooleanField(default=True) 
    id_perusahaan = serializers.SlugRelatedField(
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_jabatan = serializers.SlugRelatedField(
        queryset=Jabatan.objects.all(),
        slug_field='id_jabatan',
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
    id_ref_regu_petugas = serializers.SlugRelatedField(
        queryset=REF_REGU_PETUGAS_MODELS.objects.all(),
        slug_field='id_ref_regu_petugas',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    last_change_pwd = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = Users
        fields = (
            'id_user', 'is_active', 'roleId', 'nip', 'status', 'fullname', 'username', 'sap', 'email', 'phone',
            'gender',
            'avatar', 'password', 'signature', 'akses_login', 'id_perusahaan', 'id_jabatan', 'id_departemen','last_change_pwd','id_ref_regu_petugas')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     # as long as the fields are the same, we can just use this
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message="Email Already Taken",
        )])
    username = serializers.CharField(required=False, allow_null=True, validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message="Username Already Taken",
        )])
    is_active = serializers.BooleanField(default=True)

    akses_login = serializers.BooleanField(default=True)

    id_jabatan = serializers.SlugRelatedField(
        queryset=Jabatan.objects.all(),
        slug_field='id_jabatan',
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
    id_perusahaan = serializers.SlugRelatedField(
        queryset=Perusahaan.objects.all(),
        slug_field='id_perusahaan',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_regu_petugas = serializers.SlugRelatedField(
        queryset=REF_REGU_PETUGAS_MODELS.objects.all(),
        slug_field='id_ref_regu_petugas',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    roleId = serializers.SlugRelatedField(
        queryset=Roles.objects.all(),
        slug_field='id',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = Users
        fields = (
            'id_user', 'is_active', 'roleId', 'nip', 'status', 'fullname', 'username', 'sap', 'email', 'phone',
            'gender',
            'avatar', 'signature', 'akses_login', 'id_perusahaan', 'id_jabatan', 'id_departemen','id_ref_regu_petugas')


class UpdateReguPetugasSerializer(serializers.ModelSerializer):
    id_ref_regu_petugas = serializers.SlugRelatedField(
        queryset=REF_REGU_PETUGAS_MODELS.objects.all(),
        slug_field='id_ref_regu_petugas',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    regu_petugas = GetReguPetugas(read_only=True, source='id_ref_regu_petugas')

    class Meta:
        model = Users
        fields = ['id_ref_regu_petugas','regu_petugas']

class UpdatePasswordUser(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=100, required=False)
    new_password = serializers.CharField(max_length=100, required=False)
    retype_new_password = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Users
        fields = ['old_password', 'new_password', 'retype_new_password']


class ResetPasswordUser(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Users
        fields = ['new_password']
