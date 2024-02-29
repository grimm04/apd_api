from rest_framework import serializers

from apps.users.models import Users
from .models import TransEpLaporan
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp
from apps.master.jaringan.ref_lokasi.models import RefLokasi  
from apps.additional.serializers import IDSRef_LokasiSerializer 


class TransEpLaporanSerializers(serializers.ModelSerializer):   
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    # gardu_induk = IDSRef_LokasiSerializer(read_only=True, source='id_gardu')   

    class Meta:
        model = TransEpLaporan
        fields = '__all__'

class CRTransEpLaporanSerializers(serializers.ModelSerializer):    
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = TransEpLaporan
        fields = '__all__'

class CreateSaveTransEpLaporanSerializers(serializers.ModelSerializer):   
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = TransEpLaporan
        fields = '__all__'


class UDTransEpLaporanSerializers(serializers.ModelSerializer):
    queryset = TransEpLaporan.objects.all()
 
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = TransEpLaporan
        fields = '__all__'

 