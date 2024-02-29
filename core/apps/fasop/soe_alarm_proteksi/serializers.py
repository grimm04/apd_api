
from rest_framework import serializers
from .models import SoeAlarmProteksi, PathText

class SoeAlarmProteksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoeAlarmProteksi
        fields = ['id_kin_digital_harian', 'tanggal', 'path1text', 'path2text', 'path3text', 'path4text',  'path5text',  'point_text']
 
class PathTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathText
        fields = ['path_text']
 