from rest_framework import serializers
from .models import PertanyaanQRC

class PertanyaanQRCSerializers(serializers.ModelSerializer):
    id_pertanyaan_qrc = serializers.IntegerField(default=0)
    pertanyaan_qrc = serializers.CharField(max_length=255)
    pertanyaan_qrc_point = serializers.IntegerField()

    class Meta:
        model = PertanyaanQRC
        fields = '__all__'

class CRPertanyaanQRCSerializers(serializers.ModelSerializer):
    pertanyaan_qrc = serializers.CharField(max_length=255)
    pertanyaan_qrc_point = serializers.IntegerField()

    class Meta:
        model = PertanyaanQRC
        fields = '__all__'

class UDPertanyaanQRCSerializers(serializers.ModelSerializer):
    pertanyaan_qrc = serializers.CharField(max_length=255)
    pertanyaan_qrc_point = serializers.IntegerField()

    class Meta:
        model = PertanyaanQRC
        fields = '__all__'