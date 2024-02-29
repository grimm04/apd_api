from rest_framework import serializers
 
from .models import RefEpPenyebabGgn  
        
class RefEpPenyebabGgnserializer(serializers.ModelSerializer): 
    class Meta:
        model = RefEpPenyebabGgn
        fields = '__all__'
    
    def get_rekap_cuaca(self,obj):
        pass