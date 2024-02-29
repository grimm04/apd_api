
from rest_framework import serializers
from .models import KinerjaRC

class KinerjaRCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KinerjaRC
        fields = [ 'path1', 'path2', 'path3', 'path4', 'path5',  'jlm_rc', 'sukses', 'gagal','performance' ]

