
from rest_framework import serializers
from .models import KinerjaPeralatanScd

class KinerjaPeralatanScdSerializer(serializers.ModelSerializer):
    class Meta:
        model = KinerjaPeralatanScd
        fields = ['id_kin_scd', 'peralatan_scd', 'path1text', 'path2text', 'path3text', 'down',  'downtime',  'durasi', 'avability']