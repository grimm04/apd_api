from rest_framework import serializers
from .models import LaranganTanggungJawabMitra

class LaranganTanggungJawabMitraSerializers(serializers.ModelSerializer):
    id_larangan_tanggung_jawab_mitra = serializers.IntegerField()
    uraian = serializers.CharField(max_length=500)

    class Meta:
        model = LaranganTanggungJawabMitra
        fields = '__all__'

class CRLaranganTanggungJawabMitraCSerializers(serializers.ModelSerializer):
    uraian = serializers.CharField(max_length=500)

    class Meta:
        model = LaranganTanggungJawabMitra
        fields = '__all__'

class UDLaranganTanggungJawabMitraSerializers(serializers.ModelSerializer):
    uraian = serializers.CharField(max_length=500)

    class Meta:
        model = LaranganTanggungJawabMitra
        fields = '__all__'