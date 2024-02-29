from pickletools import optimize
from rest_framework import serializers 

from .models import WP_BAGIAN   
 
class WP_BAGIANSerializers(serializers.ModelSerializer): 
    name = serializers.CharField(max_length=50, allow_blank=True, allow_null=True, default=None) 
    ept = serializers.CharField(max_length=10, allow_blank=True, allow_null=True, default=None) 
    class Meta:
        model = WP_BAGIAN
        fields = '__all__'
