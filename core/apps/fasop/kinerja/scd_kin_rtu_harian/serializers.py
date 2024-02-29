
from apps.master.fasop.rtu.models import RTU
from rest_framework import serializers
from .models import SCD_KIN_RTU_HARIAN, ChildRTU  
 
class ChildRTUSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ChildRTU
        fields = '__all__'
        
class SCD_KIN_RTU_HARIANSerializers(serializers.ModelSerializer):  
    child : ChildRTUSerializers(many=True)
    class Meta:
        model = SCD_KIN_RTU_HARIAN
        fields = '__all__'

