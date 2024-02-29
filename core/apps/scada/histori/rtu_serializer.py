 
from rest_framework import serializers 
from apps.master.fasop.rtu.models import RTU
from apps.master.fasop.point_type.models import PointType
from apps.master.jaringan.ref_lokasi.models import RefLokasi 
from apps.fasop.realtime.scd_rtu_rtl.serializers import SCD_RTU_RTLSerializers
from apps.fasop.realtime.scd_rtu_rtl.filters import SCD_RTU_RTLFilter

#histori 
from apps.fasop.histori.scd_his_rtu.filters import SCD_HIS_RTUFilter
from apps.fasop.histori.scd_his_rtu.models import SCD_HIS_RTU

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

# class FilteredListSerializer(serializers.ListSerializer):

#     def to_representation(self, data):  
#         # if 'query_params' in self.context: 
#         #     print(self.context['query_params'].get('id_ref_lokasi')) 
#         #     data = data.filter(id_ref_lokasi=self.context['query_params'].get('id_ref_lokasi'))
#             # return [] 
#         return super(SCD_RTU_RTLSerializers, self).to_representation(data) 
#         return super(FilteredListSerializer, self).to_representation(data)


# class RTUTREESerializers(serializers.ModelSerializer):

#     class Meta:
#         list_serializer_class = FilteredListSerializer
#         model = RTU
#         fields = '__all__'



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

    # realtime = RTUTREESerializers(many=True, read_only=True) 
    total_his = serializers.SerializerMethodField(source='rtu_his',read_only=True)
    histori = serializers.SerializerMethodField(source='get_histori',read_only=True)

    class Meta:
        model = RTU
        fields = '__all__'
    
    def get_histori(self,obj):
        queryset = obj.rtu_his.all()
        filter = SCD_HIS_RTUFilter
        filter_q = 'his__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=SCD_HIS_RTUTreeSerializers,context={'query_params':self.context.get('query_params')})
     
    def get_total_his(self, obj):
        return obj.rtu_his.count() 

class SCD_HIS_RTUTreeSerializers(serializers.ModelSerializer): 
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
        queryset=RTU.objects.all(),
        slug_field='point_number',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )  

    class Meta:
        model = SCD_HIS_RTU
        fields = '__all__'
