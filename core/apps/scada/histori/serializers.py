 
from rest_framework import serializers
 
from apps.master.fasop.point_type.models import PointType 
from apps.master.fasop.telegram_group.models import TelegramGroup
from apps.additional.serializers import SubTelegramGroupSerializer
from .filters import filters_childs,ChildPointtypeFilter, RTUMasterypeFilter,CPointFilter
from .rtu_serializer import RTUSerializers
from .master_serializers import FASOPMASTERSerializers
from .c_point_serializers import CPointAnalogSerializers,CPointDigitalSerializers
from apps.master.fasop.master.filters import FASOPMASTERFilter
from apps.master.fasop.c_point.filters import CPointFilter
 

class ChildPointtypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None)
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    log_his = serializers.IntegerField(default=None)
    jenispoint = serializers.CharField(max_length=100, allow_null=True, default=None)
    show_grafik = serializers.IntegerField(default=None)
    no_urut = serializers.IntegerField(default=None)
    warna = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    send_telegram = serializers.IntegerField()
    format_pesan = serializers.CharField(max_length=999999999999, allow_blank=True, allow_null=True)
    durasi_perubahan = serializers.IntegerField(default=None)
    id_telegram_group = serializers.SlugRelatedField(
        queryset=TelegramGroup.objects.all(),
        slug_field='id_telegram_group',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    telegram_group = SubTelegramGroupSerializer(read_only=True, source='id_telegram_group') 
    id_induk_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    masters = serializers.SerializerMethodField(source='get_masters',read_only=True)  

    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_his = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_kin_hari = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_kin_bulan = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_ref = serializers.CharField(max_length=100, required=False, default=None, write_only=True)

    class Meta:
        model = PointType
        fields = '__all__' 
    
    def get_masters(self, obj): 
        if obj.jenispoint == 'RTU':
            queryset = obj.rtu.filter(status=1)
            filter = RTUMasterypeFilter
            filter_q = 'rtu__'

            return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=RTUSerializers,context={'query_params':self.context.get('query_params')})
        elif obj.jenispoint == 'MASTER':
            queryset = obj.masters.filter(status=1)
            filter = FASOPMASTERFilter
            filter_q = 'master__'
            # return []  
            return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=FASOPMASTERSerializers,context={'query_params':self.context.get('query_params')})
           
        elif obj.jenispoint == 'IED':
            return [] 
        elif obj.jenispoint == 'ANALOG':
            queryset = obj.c_point.filter(status=1)
            filter = CPointFilter
            filter_q = 'analog__' 
            return filters_childs(  queryset=queryset,
                                    filters=filter ,
                                    filter_q=filter_q ,
                                    jenispoint='ANALOG',
                                    serializer=CPointAnalogSerializers,
                                    context={'query_params':self.context.get('query_params')}
                                    )
        elif obj.jenispoint == 'DIGITAL':
            queryset = obj.c_point.filter(status=1)
            filter = CPointFilter
            filter_q = 'digital__' 
            return filters_childs(  queryset=queryset,
                                    filters=filter ,
                                    filter_q=filter_q ,
                                    jenispoint='DIGITAL',
                                    serializer=CPointDigitalSerializers,
                                    context={'query_params':self.context.get('query_params')}
                                    )
        else:
            return []  
                

class SCD_REALTIMETreeSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=None)
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    log_his = serializers.IntegerField(default=None)
    jenispoint = serializers.CharField(max_length=100, allow_null=True, default=None)
    show_grafik = serializers.IntegerField(default=None)
    no_urut = serializers.IntegerField(default=None)
    warna = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, default=None)
    send_telegram = serializers.IntegerField()
    format_pesan = serializers.CharField(max_length=999999999999, allow_blank=True, allow_null=True)
    durasi_perubahan = serializers.IntegerField(default=None)
    id_telegram_group = serializers.SlugRelatedField(
        queryset=TelegramGroup.objects.all(),
        slug_field='id_telegram_group',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    telegram_group = SubTelegramGroupSerializer(read_only=True, source='id_telegram_group')
    id_induk_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    child_pointtype = serializers.SerializerMethodField(source='get_child_pointtype',read_only=True) 
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_his = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_kin_hari = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_kin_bulan = serializers.CharField(max_length=100, required=False, default=None, write_only=True)
    nama_table_ref = serializers.CharField(max_length=100, required=False, default=None, write_only=True)

    class Meta:
        model = PointType
        fields = '__all__' 
    
    def get_child_pointtype(self, obj):
        queryset = obj.child_pointtype.filter(status=1)
        filter = CPointFilter
        filter_q = 'child__'

        return filters_childs(queryset=queryset,filters=filter ,filter_q=filter_q ,serializer=ChildPointtypeSerializer,context={'query_params':self.context.get('query_params')})