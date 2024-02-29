from numpy import source
from rest_framework import serializers

from .models import PointType

from apps.master.fasop.telegram_group.models import TelegramGroup

from apps.additional.serializers import SubTelegramGroupSerializer


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
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_his = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_kin_hari = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_kin_bulan = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_ref = serializers.CharField(max_length=100, required=False, default=None)
 

    class Meta:
        model = PointType
        fields = '__all__' 



class PointTypeSerializers(serializers.ModelSerializer):
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
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_his = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_kin_hari = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_kin_bulan = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_ref = serializers.CharField(max_length=100, required=False, default=None)

    # induk_pointtype = serializers.SerializerMethodField(source='get_induk_pointtype',read_only=True)
    induk_pointtype = ChildPointtypeSerializer(read_only=True,source='id_induk_pointtype')

    class Meta:
        model = PointType
        fields = '__all__'
    
    # def get_induk_pointtype(self, obj):
    #     # You can do more complex filtering stuff here.
    #     return ChildPointtypeSerializer(many=False, read_only=True).data

class PointTypeTreeSerializers(serializers.ModelSerializer):
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
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_his = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_rtl = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_kin_hari = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_kin_bulan = serializers.CharField(max_length=100, required=False, default=None)
    nama_table_ref = serializers.CharField(max_length=100, required=False, default=None)

    # child_pointtype = serializers.SerializerMethodField(source='get_child_pointtype',read_only=True)
    child_pointtype = ChildPointtypeSerializer(many=True, read_only=True)

    class Meta:
        model = PointType
        fields = '__all__'
    
    # def get_child_pointtype(self, obj):
    #     # You can do more complex filtering stuff here.
    #     return ChildPointtypeSerializer(obj.child_pointtype.filter(status=1), many=True, read_only=True).data
