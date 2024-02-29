from numpy import source
from rest_framework import serializers

from .models import RTU
from apps.master.fasop.point_type.models import PointType
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.fasop.telegram_group.models import TelegramGroup
from apps.additional.serializers import SubTelegramGroupSerializer
 

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

    class Meta:
        model = RTU
        fields = '__all__'


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

    child_pointtype = serializers.SerializerMethodField(source='get_child_pointtype',read_only=True) 

    # rtu_master = RTUSerializers(many=True, read_only=True)

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
        if obj.jenispoint == 'RTU':
            return RTUSerializers(obj.rtu_master.filter(status=1), many=True, read_only=True).data
        
        return []
                

class RTUTreeSerializers(serializers.ModelSerializer):
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
        # You can do more complex filtering stuff here.
        return ChildPointtypeSerializer(obj.child_pointtype.filter(status=1), many=True, read_only=True).data
