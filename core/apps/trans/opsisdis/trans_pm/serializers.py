from email.policy import default
from numpy import source
from rest_framework import serializers
import datetime
from apps.users.models import Users
from .models import TransPM
from apps.master.opsisdis.pm.ref_hi.models import RefHI
from apps.master.opsisdis.pm.ref_pm.models import RefPM
from apps.master.aset.ref_aset.models import RefAset
from apps.trans.opsisdis.trans_aset_mutasi.models import TransAsetMutasi
from apps.trans.opsisdis.trans_wo.models import TransWo
from apps.master.opsisdis.pm.ref_hi.serializers import CRRefHISerializers
from apps.master.opsisdis.pm.ref_pm.serializers import CRRefPMSerializers
from apps.master.aset.ref_aset.serializers import RefAsetSerializersList
from apps.trans.opsisdis.trans_aset_mutasi.serializers import GetTransAsetMutasiSerializers
from apps.trans.opsisdis.trans_wo.serializers import GetTransWoSerializers

class GetTransPMSerializers(serializers.ModelSerializer):
    ref_pm = CRRefPMSerializers(source='id_ref_pm')
    trans_aset_mutasi = GetTransAsetMutasiSerializers(source='id_trans_aset_mutasi') 
    ref_hi = CRRefHISerializers(source='id_ref_hi')
    ref_aset = RefAsetSerializersList(source='id_ref_aset')
    trans_wo = GetTransWoSerializers(source='id_trans_wo')
    class Meta:
        model = TransPM
        fields = '__all__'

class CRTransPMSerializers(serializers.ModelSerializer):  

    status = serializers.IntegerField(allow_null=True, required=True)
    bobot_total_standar = serializers.IntegerField(allow_null=True, required=True)   
    bobot_total_hasil = serializers.IntegerField(allow_null=True, required=True)   
    level_pm = serializers.IntegerField(allow_null=True, required=True)   
    kesimpulan = serializers.CharField(default=None, max_length=30, allow_null=True, allow_blank=True, required=False)

    id_ref_pm = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        required=True, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_trans_aset_mutasi = serializers.SlugRelatedField(
        queryset=TransAsetMutasi.objects.all(),
        slug_field='id_trans_aset_mutasi',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_trans_wo = serializers.SlugRelatedField(
        queryset=TransWo.objects.all(),
        slug_field='id_trans_wo',
        required=True, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_hi = serializers.SlugRelatedField(
        queryset=RefHI.objects.all(),
        slug_field='id_ref_hi',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_aset = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=False,
        required=True, 
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
        model = TransPM
        fields = '__all__'


class UDTransPMSerializers(serializers.ModelSerializer):
    queryset = TransPM.objects.all() 

    status = serializers.IntegerField(allow_null=True, required=False)
    bobot_total_standar = serializers.IntegerField(allow_null=True, required=False)   
    bobot_total_hasil = serializers.IntegerField(allow_null=True, required=False)   
    level_pm = serializers.IntegerField(default=1,allow_null=True, required=False)    
    kesimpulan = serializers.CharField(max_length=30, allow_null=True, allow_blank=True, required=False)

    id_ref_pm = serializers.SlugRelatedField(
        queryset=RefPM.objects.all(),
        slug_field='id_ref_pm',
        allow_null=False,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    id_trans_aset_mutasi = serializers.SlugRelatedField(
        queryset=TransAsetMutasi.objects.all(),
        slug_field='id_trans_aset_mutasi',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_trans_wo = serializers.SlugRelatedField(
        queryset=TransWo.objects.all(),
        slug_field='id_trans_wo',
        required=False,
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_hi = serializers.SlugRelatedField(
        queryset=RefHI.objects.all(),
        slug_field='id_ref_hi',
        allow_null=False,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    id_ref_aset = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=False,
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
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransPM
        fields = '__all__'

 