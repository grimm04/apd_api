from rest_framework import serializers
from .models import Perusahaan

class CRPerusahaanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)
    nama_direktur = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    alamat_kantor = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    email = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    no_hp = serializers.CharField(max_length=20, default=None, allow_blank=True, allow_null=True)

    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Perusahaan
        fields = '__all__'


class PerusahaanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100) 
    class Meta:
        model = Perusahaan
        fields = ['nama']