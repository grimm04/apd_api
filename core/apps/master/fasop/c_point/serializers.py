
from rest_framework import serializers

from .models import CPoint
from apps.master.fasop.point_type.models import PointType
from apps.master.fasop.path1.models import FASOPPATH1


class SubPointTypeSerializer(serializers.ModelSerializer):
    pointtype_name = serializers.CharField(source='name')
    class Meta:
        model = PointType
        fields = ['id_pointtype', 'name', 'jenispoint', 'warna','pointtype_name']


class Path1Serializer(serializers.ModelSerializer):

    class Meta:
        model = FASOPPATH1
        fields = ['path1', 'status', 'id_ref_lokasi']


class CPointSerializers(serializers.ModelSerializer):
    id_pointtype = serializers.SlugRelatedField(
        queryset=PointType.objects.all(),
        slug_field='id_pointtype',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    pointtype_name = serializers.ReadOnlyField()

    pointtype = SubPointTypeSerializer(read_only=True, source='id_pointtype')
    point_name = serializers.CharField(max_length=100)
    point_text = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    point_type = serializers.CharField(max_length=100)
    active = serializers.CharField(max_length=100)
    aor_id = serializers.IntegerField()
    aor_id_dw = serializers.IntegerField()
    measurement_type = serializers.IntegerField()
    tariff_group_id = serializers.IntegerField()
    ctrl_area_int_id = serializers.IntegerField()
    ctrl_area_ext_id = serializers.IntegerField()
    meas_unit = serializers.CharField(max_length=100)
    state_set_id = serializers.IntegerField()
    collection_rate = serializers.IntegerField()
    absolute_error = serializers.IntegerField()
    significant_digits = serializers.IntegerField()
    energy_type = serializers.CharField(max_length=100)
    import_export = serializers.CharField(max_length=100)
    counter_type = serializers.CharField(max_length=100)
    scaling_facktor = serializers.IntegerField()
    rollover_limit = serializers.IntegerField()
    precision_processing = serializers.IntegerField()
    precision = serializers.CharField(max_length=100)
    ddc_trigger_report_flag = serializers.CharField(max_length=100)
    system_id = serializers.IntegerField()
    collection_delay = serializers.IntegerField()
    value = serializers.IntegerField()
    status_network = serializers.CharField(max_length=100)
    update_network = serializers.CharField(max_length=100)
    kinerja = serializers.IntegerField()
    point_class = serializers.CharField(max_length=100)
    send_telegram = serializers.IntegerField()
    capture_telemetring = serializers.IntegerField()
    format_pesan = serializers.CharField(max_length=100)
    durasi_perubahan = serializers.IntegerField()
    rc = serializers.IntegerField()
    trip = serializers.IntegerField()
    rc_telegram = serializers.IntegerField()
    trip_telegram = serializers.IntegerField()
    status = serializers.IntegerField()
    wilayah = serializers.CharField(max_length=100)

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

    class Meta:
        model = CPoint
        fields = '__all__'
