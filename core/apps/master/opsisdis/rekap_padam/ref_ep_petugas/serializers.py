from email.policy import default
from rest_framework import serializers
 
from .models import RefEpPetugas 

class RefEpPetugaserializer(serializers.ModelSerializer):
    class Meta:
        model = RefEpPetugas
        fields = '__all__'


class CRRefEpPetugasSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100, required=True)  
    jenis = serializers.CharField(max_length=100, required=True)  

    class Meta:
        model = RefEpPetugas
        fields = '__all__'


class UDRefEpPetugasSerializers(serializers.ModelSerializer):
    queryset = RefEpPetugas.objects.all()
    nama = serializers.CharField(max_length=100, required=False) 
    jenis = serializers.CharField(max_length=100, required=False)  
    class Meta:
        model = RefEpPetugas
        fields = '__all__'
