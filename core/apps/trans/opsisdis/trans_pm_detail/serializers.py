from email.policy import default
from attr import field
from numpy import source
from rest_framework import serializers
import datetime
from apps.users.models import Users
from .models import TransPMDetail  
from apps.master.opsisdis.pm.ref_pm.models import RefPM  
from apps.trans.opsisdis.trans_pm.models import TransPM

from apps.master.opsisdis.pm.ref_pm.serializers import CRRefPMSerializers  
from apps.trans.opsisdis.trans_pm.serializers import GetTransPMSerializers

class GetTransPMDetailParentSerializers(serializers.ModelSerializer):
     class Meta:
        model = TransPMDetail
        fields = '__all__'
class GetTransPMDetailSerializers(serializers.ModelSerializer):
    trans_pm = GetTransPMSerializers(source='id_trans_pm')
    ref_pm = CRRefPMSerializers(source='id_ref_pm')
    induk_ref_pm_detail = GetTransPMDetailParentSerializers(source='id_induk_ref_pm_detail')
    induk = CRRefPMSerializers()
    class Meta:
        model = TransPMDetail
        fields = '__all__'

class CRTransPMDetailSerializers(serializers.ModelSerializer):    
    nama = serializers.CharField(default=None, max_length=100, allow_null=True, allow_blank=True, required=False)
    nilai_acuan = serializers.CharField(default=None, max_length=20, allow_null=True, allow_blank=True, required=False)
    nilai_pemeriksaan = serializers.CharField(default=None, max_length=20, allow_null=True, allow_blank=True, required=False)
    satuan = serializers.CharField(default=None, max_length=20, allow_null=True, allow_blank=True, required=False)
    kesimpulan = serializers.CharField(default=None, max_length=30, allow_null=True, allow_blank=True, required=False)

    id_trans_pm = serializers.SlugRelatedField(
        queryset=TransPM.objects.all(),
        slug_field='id_trans_pm',
        required=True, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_pm = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        allow_null=False,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    id_induk_ref_pm_detail = serializers.SlugRelatedField(
        queryset=TransPMDetail.objects.all(),
        slug_field='id_induk_ref_pm_detail',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    )  
    induk = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    )   
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True, 
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )  
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransPMDetail
        fields = '__all__'


class UDTransPMDetailSerializers(serializers.ModelSerializer):
    queryset = TransPMDetail.objects.all() 

    nama = serializers.CharField(default=None, max_length=100, allow_null=True, allow_blank=True, required=False)
    nilai_acuan = serializers.CharField(default=None, max_length=20, allow_null=True, allow_blank=True, required=False)
    nilai_pemeriksaan = serializers.CharField(default=None, max_length=20, allow_null=True, allow_blank=True, required=False)
    satuan = serializers.CharField(default=None, max_length=20, allow_null=True, allow_blank=True, required=False)
    kesimpulan = serializers.CharField(default=None, max_length=30, allow_null=True, allow_blank=True, required=False)

    id_trans_pm = serializers.SlugRelatedField(
        queryset=TransPM.objects.all(),
        slug_field='id_trans_pm',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_pm = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        allow_null=False,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    id_induk_ref_pm_detail = serializers.SlugRelatedField(
        queryset=TransPMDetail.objects.all(),
        slug_field='id_induk_ref_pm_detail',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    )  
    induk = serializers.SlugRelatedField(
        queryset=TransPMDetail.objects.all(),
        slug_field='id_ref_pm',
        required=False, 
        allow_null=False,
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
        required=False,
        style={'base_template': 'input.html'}
    )  
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransPMDetail
        fields = '__all__'

 