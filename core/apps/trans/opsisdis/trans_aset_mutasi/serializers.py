from email.policy import default
from rest_framework import serializers 
from apps.users.models import Users
from .models import TransAsetMutasi
from apps.master.aset.ref_aset.models import RefAset
from apps.master.aset.ref_aset_lantai.models import RefAsetLantai
from apps.master.aset.ref_aset_kondisi.models import RefAsetKondisi
from apps.master.aset.ref_aset_ruangan.models import RefAsetRuangan
from apps.master.aset.ref_aset_rak.models import RefAsetRak
from apps.master.aset.ref_aset_jenis_mutasi.models import RefAsetJenisMutasi
from apps.trans.opsisdis.trans_wo.models import TransWo

from apps.trans.opsisdis.trans_wo.models import TransWo

class GetTransAsetMutasiSerializers(serializers.ModelSerializer):

    class Meta:
        model = TransAsetMutasi
        fields = '__all__'

class CRTransAsetMutasiSerializers(serializers.ModelSerializer):  

    id_station = serializers.IntegerField(default=None,allow_null=True, required=False)
    id_bay = serializers.IntegerField(default=None,allow_null=True, required=False)
    id_pelaksana = serializers.IntegerField(default=None,allow_null=True, required=False) 

    id_ref_aset_lantai = serializers.SlugRelatedField(
        queryset=RefAsetLantai.objects.all(),
        slug_field='id_ref_aset_lantai',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    )  
    id_ref_kondisi_aset = serializers.SlugRelatedField(
        queryset=RefAsetKondisi.objects.all(),
        slug_field='id_ref_kondisi_aset',
        required=True, 
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
    id_ref_aset_ruangan = serializers.SlugRelatedField(
        queryset=RefAsetRuangan.objects.all(),
        slug_field='id_ref_aset_ruangan',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_aset_rak = serializers.SlugRelatedField(
        queryset=RefAsetRak.objects.all(),
        slug_field='id_ref_aset_rak',
        required=True, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_jenis_aset_mutasi = serializers.SlugRelatedField(
        queryset=RefAsetJenisMutasi.objects.all(),
        slug_field='id_jenis_aset_mutasi',
        required=True, 
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
    tgl_mutasi = serializers.DateField(format="%Y-%m-%d", default=None, allow_null=True)
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransAsetMutasi
        fields = '__all__'


class UDTransAsetMutasiSerializers(serializers.ModelSerializer):
    queryset = TransAsetMutasi.objects.all() 

    id_station = serializers.IntegerField(allow_null=True , required=False)
    id_bay = serializers.IntegerField(allow_null=True , required=False)
    id_pelaksana = serializers.IntegerField(allow_null=True , required=False) 

    id_ref_aset_lantai = serializers.SlugRelatedField(
        queryset=RefAsetLantai.objects.all(),
        slug_field='id_ref_aset_lantai',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    )  
    id_ref_kondisi_aset = serializers.SlugRelatedField(
        queryset=RefAsetKondisi.objects.all(),
        slug_field='id_ref_kondisi_aset',
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
    id_ref_aset_ruangan = serializers.SlugRelatedField(
        queryset=RefAsetRuangan.objects.all(),
        slug_field='id_ref_aset_ruangan',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_aset_rak = serializers.SlugRelatedField(
        queryset=RefAsetRak.objects.all(),
        slug_field='id_ref_aset_rak',
        required=False, 
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_jenis_aset_mutasi = serializers.SlugRelatedField(
        queryset=RefAsetJenisMutasi.objects.all(),
        slug_field='id_jenis_aset_mutasi',
        required=False, 
        allow_null=False,
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
    tgl_mutasi = serializers.DateField(format="%Y-%m-%d",allow_null=True)
    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = TransAsetMutasi
        fields = '__all__'

 