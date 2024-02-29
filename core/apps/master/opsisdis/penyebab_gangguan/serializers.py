from numpy import source
from rest_framework import serializers

from .models import PenyebabGangguan
from apps.master.opsisdis.jenis_penyebab_gangguan.models import JenisPenyebabGangguan


class JenisPenyebabGangguanSerializers(serializers.ModelSerializer):
    nama_jenis = serializers.CharField(source='nama')
    class Meta:
        model = JenisPenyebabGangguan
        fields = '__all__'


class CRPenyebabGangguanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=50)
    id_jenis_penyebab_gangguan = JenisPenyebabGangguanSerializers(read_only=True)

    class Meta:
        model = PenyebabGangguan
        fields = '__all__'


class RUPenyebabGangguanSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=50)
    id_jenis_penyebab_gangguan = serializers.SlugRelatedField(
        queryset=JenisPenyebabGangguan.objects.all(),
        slug_field='id_jenis_penyebab_gangguan',
        allow_null=True,
        style={'base_template': 'input.html'}
    )

    class Meta:
        model = PenyebabGangguan
        fields = '__all__'


# class UDDepartemenSerializers(serializers.ModelSerializer):
#     nama = serializers.CharField(max_length=100)
#
#     class Meta:
#         model = Departemen
#         fields = '__all__'
