from rest_framework import serializers

from apps.users.models import Users
from .models import RefPM
from apps.master.aset.ref_aset_jenis.models import RefAsetJenis

from apps.additional.serializers import UserDetailSerializerDef, RefAsetJenisSerializers



class CRRefPMSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None, allow_null=True) 
    level_pm = serializers.IntegerField(default=None, allow_null=True)  

    id_ref_aset_jenis = serializers.SlugRelatedField(
        queryset=RefAsetJenis.objects.all(),
        slug_field='id_ref_aset_jenis',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    ref_aset_jenis = RefAsetJenisSerializers(read_only=True, source='id_ref_aset_jenis')

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    user_entri = UserDetailSerializerDef(read_only=True, source='id_user_entri')
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )
    user_update = UserDetailSerializerDef(read_only=True, source='id_user_update')
    
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)
    
    

    class Meta:
        model = RefPM
        fields = '__all__'


class UDRefPMSerializers(serializers.ModelSerializer):
    queryset = RefPM.objects.all()

    nama = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None, allow_null=True)
    level_pm = serializers.IntegerField(default=None, allow_null=True)  

    id_ref_aset_jenis = serializers.SlugRelatedField(
        queryset=RefAsetJenis.objects.all(),
        slug_field='id_ref_aset_jenis',
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
        model = RefPM
        fields = '__all__'

 