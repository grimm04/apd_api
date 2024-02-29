from rest_framework import serializers

from apps.master.fasop.master.models import FASOPMASTER
from apps.master.fasop.point_type.models import PointType
from apps.master.jaringan.ref_lokasi.models import RefLokasi  

from apps.fasop.realtime.scd_master_rtl.models import SCD_MASTER_RTL  
 
from apps.fasop.realtime.scd_master_rtl.filters import SCD_MASTER_RTLFilter  
from apps.additional.serializers import FASOPMASTERTypeSerializer 
from .filters import filters_childs

class SubPointTypeSerializer(serializers.ModelSerializer):
    nama_jenis = serializers.CharField(source='name')
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna','nama_jenis']

class SubRefLokasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi']


class FASOPMASTERSerializers(serializers.ModelSerializer):
    path3text = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    path3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    status = serializers.IntegerField()
    faktor = serializers.CharField(max_length=18, allow_blank=True, allow_null=True) 
    send_telegram = serializers.IntegerField()
    kinerja = serializers.IntegerField()
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_ref_lokasi')

    total_rtl = serializers.SerializerMethodField(source='master_rtl',read_only=True)
    realtime = serializers.SerializerMethodField(source='get_realtime',read_only=True)

    class Meta:
        model = FASOPMASTER
        fields = '__all__'
    
    def get_realtime(self,obj):
        queryset = obj.master_rtl.all()
        filter = SCD_MASTER_RTLFilter
        filter_q = 'rtl__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCDMasterRTLTreeSerializers,context={'query_params':self.context.get('query_params')})
     
    def get_total_rtl(self, obj):
        queryset = obj.master_rtl.all()
        filter = SCD_MASTER_RTLFilter
        filter_q = 'rtl__'

        count = filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCDMasterRTLTreeSerializers,context={'query_params':self.context.get('query_params')})
        return count
 

class SCDMasterRTLTreeSerializers(serializers.ModelSerializer): 
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
        queryset= FASOPMASTER.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    class Meta:
        model = SCD_MASTER_RTL
        fields = '__all__'
