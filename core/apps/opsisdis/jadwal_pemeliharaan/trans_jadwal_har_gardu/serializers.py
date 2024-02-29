from rest_framework import serializers

from apps.users.models import Users
from .models import TransJadwalHarGardu
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har.models import TransJadwalHar
from apps.master.jaringan.ref_lokasi.models import RefLokasi   
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har.serializers import TransJadwalHarSerializers  
from apps.additional.serializers import ReflokasiGI,ReflokasiPenyulang,ReflokasiUp3
class IDSRef_LokasiSerializer(serializers.ModelSerializer): 
    gardu_induk = ReflokasiGI(read_only=True, source='id_gardu_induk')  
    penyulang = ReflokasiPenyulang(read_only=True, source='id_penyulang')    
    up3 = ReflokasiUp3(read_only=True, source='id_up3_1')  

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi','id_gardu_induk','id_penyulang','id_up3_1','alamat','gardu_induk','penyulang','up3']  

class TransJadwalHarGarduSerializers(serializers.ModelSerializer):  
    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_trans_jadwal_har = serializers.SlugRelatedField(
        queryset=TransJadwalHar.objects.all(),
        slug_field='id_trans_jadwal_har',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    gardu = IDSRef_LokasiSerializer(read_only=True, source='id_gardu')  
    trans_jadwal_har = TransJadwalHarSerializers(read_only=True, source='id_id_trans_jadwal_har')  

    class Meta:
        model = TransJadwalHarGardu
        fields = '__all__'

class CRTransJadwalHarGarduSerializers(serializers.ModelSerializer):  
    id_gardu = serializers.ListField(child=serializers.CharField())
    # id_gardu = serializers.SlugRelatedField(
    #     queryset=RefLokasi.objects.all(),
    #     slug_field='id_ref_lokasi',
    #     allow_null=True,
    #     required=False,
    #     style={'base_template': 'input.html'}
    # )
    id_trans_jadwal_har = serializers.SlugRelatedField(
        queryset=TransJadwalHar.objects.all(),
        slug_field='id_trans_jadwal_har',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = TransJadwalHarGardu
        fields = '__all__'

class CreateSaveTransJadwalHarGarduSerializers(serializers.ModelSerializer):  
    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_trans_jadwal_har = serializers.SlugRelatedField(
        queryset=TransJadwalHar.objects.all(),
        slug_field='id_trans_jadwal_har',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = TransJadwalHarGardu
        fields = '__all__'


class UDTransJadwalHarGarduSerializers(serializers.ModelSerializer):
    queryset = TransJadwalHarGardu.objects.all()

    id_gardu = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_trans_jadwal_har = serializers.SlugRelatedField(
        queryset=TransJadwalHar.objects.all(),
        slug_field='id_trans_jadwal_har',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = TransJadwalHarGardu
        fields = '__all__'

 