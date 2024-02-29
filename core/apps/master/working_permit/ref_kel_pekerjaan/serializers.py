from rest_framework import serializers
from .models import RefKelPekerjaan

class RefKelPekerjaanSerializers(serializers.ModelSerializer): 

    class Meta:
        model = RefKelPekerjaan
        fields = '__all__'

class CRRefKelPekerjaanSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, required=True)
    alias = serializers.CharField(max_length=30, required=True) 
    kategori = serializers.CharField(max_length=20, required=True)  

    class Meta:
        model = RefKelPekerjaan
        fields = '__all__'

class UDRefKelPekerjaanSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, required=False)
    alias = serializers.CharField(max_length=30, required=False) 
    kategori = serializers.CharField(max_length=20, required=False)  

    class Meta:
        model = RefKelPekerjaan
        fields = '__all__'