from apps.master.fasop.c_point.models import CPoint 
from rest_framework import serializers 

from .models import SCD_ANALOG_RTL  
from apps.additional.serializers import CPointTypeSerializer 
 
class SCD_ANALOG_RTLSerializers(serializers.ModelSerializer): 
    status = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    statekey_1 = serializers.FloatField(default=0.0)
    statekey_2 = serializers.FloatField(default=0.0) 
    send_telegram = serializers.IntegerField(default=None) 
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_1 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_capture = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)

    kesimpulan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    value = serializers.FloatField(default=0.0) 
    path1 = serializers.ReadOnlyField()
    
    point_number = serializers.SlugRelatedField(
        queryset= CPoint.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    # c_point = CPointTypeSerializer(read_only=True, source='point_number')

    class Meta:
        model = SCD_ANALOG_RTL
        fields = '__all__'
