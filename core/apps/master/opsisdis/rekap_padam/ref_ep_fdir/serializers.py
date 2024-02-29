from email.policy import default
from rest_framework import serializers
 
from .models import RefEpFdir 

class RefEpFdirerializer(serializers.ModelSerializer):
    class Meta:
        model = RefEpFdir
        fields = '__all__'


class CRRefEpFdirSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100, required=True)  

    class Meta:
        model = RefEpFdir
        fields = '__all__'


class UDRefEpFdirSerializers(serializers.ModelSerializer):
    queryset = RefEpFdir.objects.all()
    nama = serializers.CharField(max_length=100, required=False) 
    class Meta:
        model = RefEpFdir
        fields = '__all__'
