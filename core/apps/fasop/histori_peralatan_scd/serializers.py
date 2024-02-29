
from rest_framework import serializers
from .models import HistoriPeralatanScd

class HistoriPeralatanScdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriPeralatanScd
        fields = ['id_his_scd', 'peralatan_scd', 'path1', 'path2', 'path3', 'tanggal_awal',  'status_awal',  'tanggal_akhir', 'status_akhir', 'durasi', 'kesimpulan']