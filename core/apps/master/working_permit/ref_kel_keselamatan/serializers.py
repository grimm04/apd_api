from rest_framework import serializers
from .models import RefKelKeselamatan

class RefKelKeselamatanSerializers(serializers.ModelSerializer):  
    class Meta:
        model = RefKelKeselamatan
        fields = '__all__'

class CRRefKelKeselamatanSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, required=True)  
    alias = serializers.CharField(max_length=30, required=True) 
    kategori = serializers.CharField(max_length=20, required=True)  


    class Meta:
        model = RefKelKeselamatan
        fields = '__all__'

class UDRefKelKeselamatanSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, required=False)  
    alias = serializers.CharField(max_length=30, required=False) 
    kategori = serializers.CharField(max_length=20, required=False)   

    class Meta:
        model = RefKelKeselamatan
        fields = '__all__'