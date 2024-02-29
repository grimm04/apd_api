from apps.master.fasop.c_point.models import CPoint 
from rest_framework import serializers

from .models import SCD_ANALOG_HIS_30M  
from apps.additional.serializers import CPointTypeSerializer 
 
class SCD_ANALOG_HIS_30MSerializers(serializers.ModelSerializer):  
    status_2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    value_2 = serializers.IntegerField(default=None) 
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None) 
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None) 
    
    point_number = serializers.SlugRelatedField(
        queryset= CPoint.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    c_point = CPointTypeSerializer(read_only=True, source='point_number')

    class Meta:
        model = SCD_ANALOG_HIS_30M
        fields = '__all__'
