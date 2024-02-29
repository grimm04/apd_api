
from rest_framework import serializers
from .models import PointtypeAnak, PointtypeInduk, RealtimeScada

class RealtimeScadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtimeScada
        fields = ['point_number', 'durasi', 'tgl_gangguan', 'value', 'point_name', 'jenis_point']
 
class PointtypeAnakSerializer(serializers.ModelSerializer):
    children = RealtimeScadaSerializer(many=True)
    class Meta:
        model = PointtypeAnak
        fields = ['id_pointtype', 'nama_pointtype', 'jenis_pointtype', 'id_pointtype_induk','jml_children', 'children']
        
class PointtypeIndukSerializer(serializers.ModelSerializer):  
    anak_pointtype = PointtypeAnakSerializer(many=True)
    class Meta:
        model = PointtypeInduk
        fields = ['id_pointtype', 'nama_pointtype', 'jenis_pointtype', 'id_pointtype_induk','jml_pointtype', 'anak_pointtype']

