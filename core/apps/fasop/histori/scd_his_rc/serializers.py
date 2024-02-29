 
from rest_framework import serializers 
from .models import SCD_HIS_RC   
 

class SCD_HIS_RCSerializers(serializers.ModelSerializer):  
    path1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path4 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path5 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    b1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    b2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    b3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    elem = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    info = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 

    datum_1 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    status_1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    status_2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    msgoperator = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 

    cek_remote = serializers.IntegerField(default=None) 
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)  

    class Meta:
        model = SCD_HIS_RC
        fields = '__all__'
