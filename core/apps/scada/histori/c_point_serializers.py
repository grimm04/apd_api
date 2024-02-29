from rest_framework import serializers

from apps.master.fasop.c_point.models import CPoint
from apps.master.fasop.point_type.models import PointType 

from .filters import filters_childs
from apps.master.fasop.path1.models import FASOPPATH1
from rest_framework import serializers 
from apps.master.fasop.c_point.models import CPoint   

#analog & digital histori
from apps.fasop.histori.scd_his_analog.models import SCD_HIS_ANALOG
from apps.fasop.histori.scd_his_digital.models import SCD_HIS_DIGITAL  
from apps.fasop.histori.scd_his_analog.filters import SCD_HIS_ANALOGFilter
from apps.fasop.histori.scd_his_digital.filters import SCD_HIS_DIGITALFilter


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
    total_his = serializers.SerializerMethodField(source='analog_his',read_only=True)
    histori = serializers.SerializerMethodField(source='get_histori',read_only=True)

    class Meta:
        model = CPoint
        fields = '__all__'

    
    def get_histori(self,obj): 
        queryset = obj.analog_his.all()
        filter = SCD_HIS_ANALOGFilter
        filter_q = 'his__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCD_HIS_ANALOGTreeSerializers,context={'query_params':self.context.get('query_params')})
       
     
    def get_total_his(self, obj):
        return obj.analog_his.count() 

        
            

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
    total_his = serializers.SerializerMethodField(source='digital_his',read_only=True)
    histori = serializers.SerializerMethodField(source='get_histori',read_only=True)

    class Meta:
        model = CPoint
        fields = '__all__'

    
    def get_histori(self,obj): 
        queryset = obj.digital_his.all()
        filter = SCD_HIS_DIGITALFilter
        filter_q = 'his__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCD_HIS_DIGITALTreeSerializers,context={'query_params':self.context.get('query_params')})
        
     
    def get_total_his(self, obj):
        return obj.digital_his.count()  


class SCD_HIS_ANALOGTreeSerializers(serializers.ModelSerializer): 
    status = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    statekey_1 = serializers.FloatField(default=0.0)
    statekey_2 = serializers.FloatField(default=0.0) 
    send_telegram = serializers.IntegerField(default=None) 
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_1 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_capture = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)

    kesimpulan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    value = serializers.FloatField(default=0.0) 
    path1 = serializers.ReadOnlyField()
    
    point_number = serializers.SlugRelatedField(
        queryset= CPoint.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    class Meta:
        model = SCD_HIS_ANALOG
        fields = '__all__'


class SCD_HIS_DIGITALTreeSerializers(serializers.ModelSerializer): 
    status = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_1 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status_2 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None) 
    statekey_1 = serializers.FloatField(default=0.0)
    statekey_2 = serializers.FloatField(default=0.0) 
    send_telegram = serializers.IntegerField(default=None) 
    datum = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_1 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)
    datum_capture = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" ,default=None)

    kesimpulan = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    value = serializers.FloatField(default=0.0) 
    
    point_number = serializers.SlugRelatedField(
        queryset= CPoint.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = SCD_HIS_DIGITAL
        fields = '__all__'
