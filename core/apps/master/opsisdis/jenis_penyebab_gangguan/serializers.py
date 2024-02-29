from rest_framework import serializers

from .models import JenisPenyebabGangguan


class CRJenisPenyebabGangguanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)

    class Meta:
        model = JenisPenyebabGangguan
        fields = '__all__'


# class UDDepartemenSerializers(serializers.ModelSerializer):
#     nama = serializers.CharField(max_length=100)
#
#     class Meta:
#         model = Departemen
#         fields = '__all__'
