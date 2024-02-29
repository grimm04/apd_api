from rest_framework import serializers
 
from .models import RefEpCuaca 
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp

class TransEpserializer(serializers.ModelSerializer):
    class Meta:
        model = TransEp
        fields = ['id_trans_ep']
        
class RefEpCuacaserializer(serializers.ModelSerializer):
    # trans_rekap_padam_cuaca = TransEpserializer(many=True,read_only=True)
    class Meta:
        model = RefEpCuaca
        fields = '__all__'
    
    def get_rekap_cuaca(self,obj):
        pass