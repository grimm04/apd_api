from email.policy import default
from rest_framework import serializers
 
from .models import RefEpFiohl 

class RefEpFiohlerializer(serializers.ModelSerializer):
    class Meta:
        model = RefEpFiohl
        fields = '__all__'


class CRRefEpFiohlSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100, required=True)  

    class Meta:
        model = RefEpFiohl
        fields = '__all__'


class UDRefEpFiohlSerializers(serializers.ModelSerializer):
    queryset = RefEpFiohl.objects.all()
    nama = serializers.CharField(max_length=100, required=False) 
    class Meta:
        model = RefEpFiohl
        fields = '__all__'
