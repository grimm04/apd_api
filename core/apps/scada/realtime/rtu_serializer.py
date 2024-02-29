 
from rest_framework import serializers 
from apps.master.fasop.rtu.models import RTU
from apps.master.fasop.point_type.models import PointType
from apps.master.jaringan.ref_lokasi.models import RefLokasi 
from apps.fasop.realtime.scd_rtu_rtl.serializers import SCD_RTU_RTLSerializers
from apps.fasop.realtime.scd_rtu_rtl.filters import SCD_RTU_RTLFilter

from .filters import filters_childs, filter_count
class SubPointTypeSerializer(serializers.ModelSerializer):
    nama_jenis = serializers.CharField(source='name')
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna','nama_jenis']


class SubRefLokasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi'] 


class RTUSerializers(serializers.ModelSerializer):
    pointtype_name = serializers.ReadOnlyField()
    path3text = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    path3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    status = serializers.IntegerField(default=None)
    faktor = serializers.FloatField(default=0.0)
    send_telegram = serializers.IntegerField(default=None)
    kinerja = serializers.IntegerField(default=None)
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype')
    id_ref_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_ref_lokasi')
 
    realtime = serializers.SerializerMethodField(source='get_realtime',read_only=True)
    total_rtl = serializers.SerializerMethodField(source='rtu_rtl',read_only=True)

    class Meta:
        model = RTU
        fields = '__all__'
    
    def get_realtime(self,obj):
        queryset = obj.rtu_rtl.all()
        filter = SCD_RTU_RTLFilter
        filter_q = 'rtl__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCD_RTU_RTLSerializers,context={'query_params':self.context.get('query_params')})
     
    def get_total_rtl(self, obj):
        return obj.rtu_rtl.count()
        queryset = obj.rtu_rtl.all()   
        filter = SCD_RTU_RTLFilter

        filter_q = 'rtl__'
        count = filter_count(queryset=queryset,filter_q=filter_q,filters=filter, context={'query_params':self.context.get('query_params')})
        return count