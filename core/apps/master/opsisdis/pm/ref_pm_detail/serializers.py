from rest_framework import serializers

from apps.users.models import Users
from .models import RefPMDetail
from apps.master.opsisdis.pm.ref_pm.models import RefPM

from apps.additional.serializers import UserDetailSerializerDef, RefPMSerializers


class CRRefPMDetailSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100, allow_null=True, required=False)
    satuan = serializers.CharField(max_length=20, allow_null=True, required=False)
    id_induk_ref_pm_detail = serializers.IntegerField(default=None, allow_null=True, required=False) 
    induk = serializers.IntegerField(default=None, allow_null=True, required=False )
    nilai_acuan = serializers.CharField(max_length=20,allow_null=True, required=False)
    no_urut = serializers.IntegerField(default=None, allow_null=True, required=False)  
    tipe_data = serializers.CharField(max_length=30, allow_null=True, required=False)
    nilai_pemeriksaan = serializers.CharField(max_length=100, allow_null=True, required=False)

    id_ref_pm = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    ref_pm = RefPMSerializers(read_only=True, source='id_ref_pm')

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    # user_entri = UserDetailSerializerDef(read_only=True, source='id_user_entri')
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )
    # user_update = UserDetailSerializerDef(read_only=True, source='id_user_update')
    
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = RefPMDetail
        fields = '__all__'


class UDRefPMDetailSerializers(serializers.ModelSerializer):
    queryset = RefPMDetail.objects.all()

    nama = serializers.CharField(max_length=100, allow_null=True, required=False)
    satuan = serializers.CharField(max_length=20, allow_null=True, required=False)
    id_induk_ref_pm_detail = serializers.IntegerField(default=None, allow_null=True, required=False) 
    induk = serializers.IntegerField(default=None, allow_null=True, required=False )
    nilai_acuan = serializers.CharField(max_length=20,allow_null=True, required=False)
    no_urut = serializers.IntegerField(default=None, allow_null=True, required=False)  
    tipe_data = serializers.CharField(max_length=30, allow_null=True, required=False)
    nilai_pemeriksaan = serializers.CharField(max_length=100, allow_null=True, required=False)

    id_ref_pm = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=True,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = RefPMDetail
        fields = '__all__'

 