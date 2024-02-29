from rest_framework import serializers

from apps.master.fasop.c_point.models import CPoint
from apps.master.fasop.point_type.models import PointType 

from .filters import filters_childs
from apps.master.fasop.path1.models import FASOPPATH1
from rest_framework import serializers 
from apps.master.fasop.c_point.models import CPoint  

#analog & digital
from apps.fasop.realtime.scd_analog_rtl.serializers import SCD_ANALOG_RTLSerializers
from apps.fasop.realtime.scd_digital_rtl.serializers import SCD_DIGITAL_RTLSerializers
from apps.fasop.realtime.scd_analog_rtl.filters import SCD_ANALOG_RTLFilter
from apps.fasop.realtime.scd_digital_rtl.filters import SCD_DIGITAL_RTLFilter

class SubPointTypeSerializer(serializers.ModelSerializer):
    pointtype_name = serializers.CharField(source='name')
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna','pointtype_name']


class Path1Serializer(serializers.ModelSerializer):

    class Meta:
        model = FASOPPATH1
        fields = ['path1', 'status', 'id_ref_lokasi']


class CPointAnalogSerializers(serializers.ModelSerializer):
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    pointtype_name = serializers.ReadOnlyField()
 
    point_name = serializers.CharField(max_length=100)
    point_text = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    point_type = serializers.CharField(max_length=100)
    active = serializers.CharField(max_length=100) 
    collection_delay = serializers.IntegerField()
    value = serializers.IntegerField()
    status_network = serializers.CharField(max_length=100)
    update_network = serializers.CharField(max_length=100)
    kinerja = serializers.IntegerField()
    point_class = serializers.CharField(max_length=100) 
    capture_telemetring = serializers.IntegerField()
    format_pesan = serializers.CharField(max_length=100)
    durasi_perubahan = serializers.IntegerField() 
    path1 = serializers.CharField(max_length=100)
    path2 = serializers.CharField(max_length=100)
    path3 = serializers.CharField(max_length=100)
    path4 = serializers.CharField(max_length=100)
    path5 = serializers.CharField(max_length=100)

    path1text = serializers.CharField(max_length=100)
    path2text = serializers.CharField(max_length=100)
    path3text = serializers.CharField(max_length=100)
    path4text = serializers.CharField(max_length=100)
    path5text = serializers.CharField(max_length=100)

    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    total_rtl = serializers.SerializerMethodField(source='analog',read_only=True)
    realtime = serializers.SerializerMethodField(source='get_realtime',read_only=True)

    class Meta:
        model = CPoint
        fields = '__all__'

    
    def get_realtime(self,obj): 
        queryset = obj.analog.all()
        filter = SCD_ANALOG_RTLFilter
        filter_q = 'rtl__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCD_ANALOG_RTLSerializers,context={'query_params':self.context.get('query_params')})
         

        
     
    def get_total_rtl(self, obj):
        return obj.analog.count() 

        
            

class CPointDigitalSerializers(serializers.ModelSerializer):
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    pointtype_name = serializers.ReadOnlyField()
 
    point_name = serializers.CharField(max_length=100)
    point_text = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    point_type = serializers.CharField(max_length=100)
    active = serializers.CharField(max_length=100) 
    collection_delay = serializers.IntegerField()
    value = serializers.IntegerField()
    status_network = serializers.CharField(max_length=100)
    update_network = serializers.CharField(max_length=100)
    kinerja = serializers.IntegerField()
    point_class = serializers.CharField(max_length=100) 
    capture_telemetring = serializers.IntegerField()
    format_pesan = serializers.CharField(max_length=100)
    durasi_perubahan = serializers.IntegerField() 
    path1 = serializers.CharField(max_length=100)
    path2 = serializers.CharField(max_length=100)
    path3 = serializers.CharField(max_length=100)
    path4 = serializers.CharField(max_length=100)
    path5 = serializers.CharField(max_length=100)

    path1text = serializers.CharField(max_length=100)
    path2text = serializers.CharField(max_length=100)
    path3text = serializers.CharField(max_length=100)
    path4text = serializers.CharField(max_length=100)
    path5text = serializers.CharField(max_length=100)

    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    total_rtl = serializers.SerializerMethodField(source='digital',read_only=True)
    realtime = serializers.SerializerMethodField(source='get_realtime',read_only=True)

    class Meta:
        model = CPoint
        fields = '__all__'

    
    def get_realtime(self,obj):  
        queryset = obj.digital.all()
        filter = SCD_DIGITAL_RTLFilter
        filter_q = 'rtl__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCD_DIGITAL_RTLSerializers,context={'query_params':self.context.get('query_params')})
        

        
     
    def get_total_rtl(self, obj):
        return obj.digital.count()  

