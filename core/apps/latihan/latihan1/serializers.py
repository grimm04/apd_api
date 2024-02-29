from unicodedata import name
from rest_framework import serializers
from .models import LATIHAN 
from apps.users.models import Users
 


class LATIHANSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)  
    class Meta:
        model = LATIHAN
        fields = '__all__'


# class CRLATIHANCSerializers(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)  


#     class Meta:
#         model = LATIHAN
#         fields = '__all__'


# class UDLATIHANSerializers(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)   

#     class Meta:
#         model = LATIHAN
#         fields = '__all__'
