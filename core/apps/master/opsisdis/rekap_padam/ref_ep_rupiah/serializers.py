from email.policy import default
from rest_framework import serializers
 
from .models import RefEpRupiah 

class RefEpRupiaherializer(serializers.ModelSerializer):
    class Meta:
        model = RefEpRupiah
        fields = '__all__' 
