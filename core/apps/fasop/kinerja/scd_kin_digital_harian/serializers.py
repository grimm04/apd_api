from apps.master.fasop.c_point.models import CPoint 
from rest_framework import serializers

from .models import SCD_KIN_DIGITAL_HARI  

from apps.additional.serializers import CPointTypeSerializer 
        
class SCD_KIN_DIGITAL_HARISerializers(serializers.ModelSerializer):  
    up = serializers.IntegerField(default=None) 
    down = serializers.IntegerField(default=None) 
    downtime = serializers.IntegerField(default=None) 
    uptime = serializers.IntegerField(default=None) 
    performance = serializers.IntegerField(default=None) 
    faktor = serializers.IntegerField(default=None) 
    alltime = serializers.IntegerField(default=None) 
    kinerja = serializers.IntegerField(default=None) 

    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,read_only=True) 
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,read_only=True)       

    point_number = serializers.SlugRelatedField(
        queryset= CPoint.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    c_point = CPointTypeSerializer(read_only=True, source='point_number')

    class Meta:
        model = SCD_KIN_DIGITAL_HARI
        fields = '__all__'
