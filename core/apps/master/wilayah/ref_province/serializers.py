from rest_framework import serializers

from apps.users.models import Users
from .models import RefProvince


class RefProvincSerializers(serializers.ModelSerializer):
    class Meta:
        model = RefProvince
        fields = '__all__'


class CRRefProvinceSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
   

    class Meta:
        model = RefProvince
        fields = '__all__'


class UDRefProvinceSerializers(serializers.ModelSerializer):
    queryset = RefProvince.objects.all()

    name = serializers.CharField(max_length=100)  

    class Meta:
        model = RefProvince
        fields = '__all__'
