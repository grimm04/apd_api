from rest_framework import serializers
from .models import FASOPPM

class FASOPPMSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    status = serializers.IntegerField(default=None, allow_null=True)
    nilai = serializers.IntegerField(default=None, allow_null=True)
    tgl_aktif = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_berikut = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = FASOPPM
        fields = '__all__'

class CRFASOPPMCSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    status = serializers.IntegerField(default=None, allow_null=True)
    nilai = serializers.IntegerField(default=None, allow_null=True)
    tgl_aktif = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_berikut = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = FASOPPM
        fields = '__all__'

class UDFASOPPMSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)
    status = serializers.IntegerField(default=None, allow_null=True)
    nilai = serializers.IntegerField(default=None, allow_null=True)
    tgl_aktif = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_berikut = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = FASOPPM
        fields = '__all__'