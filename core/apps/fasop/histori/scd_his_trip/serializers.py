 
from rest_framework import serializers 
from .models import SCD_HIS_TRIP   
 

class SCD_HIS_TRIPSerializers(serializers.ModelSerializer):  
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

    trip = serializers.IntegerField(default=None)
    ocr = serializers.IntegerField(default=None)
    gfr = serializers.IntegerField(default=None)

    i = serializers.FloatField(default=None)
    ifr = serializers.FloatField(default=None)
    ifs = serializers.FloatField(default=None)
    ift = serializers.FloatField(default=None)
    ifn = serializers.FloatField(default=None)
    cek_trip = serializers.FloatField(default=None)

    jenis = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    cb_open = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    wilayah_padam = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
     
    datum_cb_open = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)  
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)  
    cbtr = serializers.IntegerField(default=None)

    class Meta:
        model = SCD_HIS_TRIP
        fields = '__all__'
