
from rest_framework import serializers
from .models import HistoriRC

class HistoriRCSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriRC
        fields = ['id_his_rc', 'path1', 'path2', 'path3', 'path4', 'path5',  'b1',  'b2', 'b3', 'elem', 'info', 'datum_1', 'datum_2', 'status_1', 'status_2', 'msg_operator', 'cek_remote', 'durasi']
 