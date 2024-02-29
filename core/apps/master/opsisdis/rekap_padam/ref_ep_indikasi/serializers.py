from email.policy import default
from rest_framework import serializers
 
from .models import RefEpIndikasi 

class RefEpIndikasierializer(serializers.ModelSerializer):
    class Meta:
        model = RefEpIndikasi
        fields = '__all__'


class CRRefEpIndikasiSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100, required=True)  
    jenis = serializers.CharField(max_length=100, required=True)  

    class Meta:
        model = RefEpIndikasi
        fields = '__all__'


class UDRefEpIndikasiSerializers(serializers.ModelSerializer):
    queryset = RefEpIndikasi.objects.all()
    nama = serializers.CharField(max_length=100, required=False) 
    jenis = serializers.CharField(max_length=100, required=False)  
    class Meta:
        model = RefEpIndikasi
        fields = '__all__'
