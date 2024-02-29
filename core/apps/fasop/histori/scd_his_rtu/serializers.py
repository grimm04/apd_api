 
from rest_framework import serializers 
from .models import SCD_HIS_RTU 
from apps.master.fasop.rtu.models import RTU 
from apps.master.fasop.rtu.serializers import SubPointTypeSerializer 

from apps.additional.serializers import RTUTypeSerializer 

class SCD_HIS_RTUSerializers(serializers.ModelSerializer): 
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
    
    point_number = serializers.SlugRelatedField(
        queryset=RTU.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    rtu = RTUTypeSerializer(read_only=True, source='point_number')

    class Meta:
        model = SCD_HIS_RTU
        fields = '__all__'
