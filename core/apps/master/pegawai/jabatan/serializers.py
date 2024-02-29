from rest_framework import serializers

from .models import Jabatan


class CRJabatanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)

    class Meta:
        model = Jabatan
        fields = '__all__'


# class UDJabatanSerializers(serializers.ModelSerializer):
#     nama_jabatan = serializers.CharField(max_length=100)
# 
#     class Meta:
#         model = Jabatan
#         fields = '__all__'
