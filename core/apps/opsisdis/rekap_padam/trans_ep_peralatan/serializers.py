from rest_framework import serializers

from apps.users.models import Users
from apps.additional.serializers import IDSRef_LokasiSerializer
from .models import TransEpPeralatan 
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp
from apps.master.jaringan.ref_lokasi.models import RefLokasi    
from apps.opsisdis.rekap_padam.trans_ep.serializers import ReflokasiKeypoint

class TransEpSerializers(serializers.ModelSerializer):    
    keypoint = ReflokasiKeypoint(read_only=True, source='id_keypoint')  
    # status = serializers.SerializerMethodField(source='get_status',read_only=True)
    
    class Meta:
        model = TransEp
        fields = ['id_trans_ep','jenis_keypoint','no_event','id_keypoint','keypoint']
    
    def get_status(self,obj):
        status = None
        if not obj.jam_tutup and not obj.jam_normal :
            status = "Padam"
        elif obj.jam_tutup and not obj.jam_normal:
            status = "Nyala Bertahap"
        elif obj.jam_tutup and obj.jam_normal:
            status = "Normal" 
        else:
            status = "-" 
        return status   

class ExportTransEpPeralatanSerializers(serializers.ModelSerializer):    
    trans_ep  = TransEpSerializers(read_only=True, source='id_trans_ep')   
    peralatan = IDSRef_LokasiSerializer(read_only=True, source='id_peralatan')    
    date_hari = serializers.DateTimeField(read_only=True, source='tgl', format="%Y-%m-%d")
    jam = serializers.DateTimeField(read_only=True, source='tgl', format="%H:%M:%S")
    class Meta:
        model = TransEpPeralatan
        fields = '__all__'

class TransEpPeralatanSerializers(serializers.ModelSerializer):   
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )    
    peralatan = IDSRef_LokasiSerializer(read_only=True, source='id_peralatan')   

    class Meta:
        model = TransEpPeralatan
        fields = '__all__'

class CRTransEpPeralatanSerializers(serializers.ModelSerializer):    
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )  
    id_peralatan = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )  

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = TransEpPeralatan
        fields = '__all__' 

class UDTransEpPeralatanSerializers(serializers.ModelSerializer):
    queryset = TransEpPeralatan.objects.all()
 
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_peralatan = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
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
        model = TransEpPeralatan
        fields = '__all__'

 