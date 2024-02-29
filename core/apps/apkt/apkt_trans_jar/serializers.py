from rest_framework import serializers
from .models import APKTTransJAR

class APKTTransJARSerializers(serializers.ModelSerializer):
    no_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    nama_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    tgl_laporan = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    no_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    status_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jenis_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jlh_gardu_nyala = serializers.IntegerField(default=None, allow_null=True)
    jlh_gardu_padam = serializers.IntegerField(default=None, allow_null=True)
    tgl_nyala_terakhir = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_close_laporan = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_padam = serializers.IntegerField(default=None, allow_null=True)
    tgl_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    server_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    res_apkt_kirim_padam = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    id_feeder = serializers.IntegerField(default=None, allow_null=True)
    feeder = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    status_data = serializers.IntegerField(default=None, allow_null=True)
    tgl_nyala_awal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_mulai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_nyala = serializers.IntegerField(default=None, allow_null=True)
    tgl_mulai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nama_switch = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    point_number_switch = serializers.IntegerField(default=None, allow_null=True)
    kode_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jenis_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    parent_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    res_apkt_kirim_nyala = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    tgl_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = APKTTransJAR
        fields = '__all__'

class UDAPKTTransJARSerializers(serializers.ModelSerializer):
    no_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    nama_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    tgl_laporan = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    no_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    status_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jenis_laporan = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jlh_gardu_nyala = serializers.IntegerField(default=None, allow_null=True)
    jlh_gardu_padam = serializers.IntegerField(default=None, allow_null=True)
    tgl_nyala_terakhir = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_close_laporan = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_padam = serializers.IntegerField(default=None, allow_null=True)
    tgl_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    server_apkt = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    res_apkt_kirim_padam = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    id_feeder = serializers.IntegerField(default=None, allow_null=True)
    feeder = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    status_data = serializers.IntegerField(default=None, allow_null=True)
    tgl_nyala_awal = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_mulai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_padam = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status_apkt_kirim_nyala = serializers.IntegerField(default=None, allow_null=True)
    tgl_mulai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tgl_selesai_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nama_switch = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    point_number_switch = serializers.IntegerField(default=None, allow_null=True)
    kode_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    jenis_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    parent_aset = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    res_apkt_kirim_nyala = serializers.CharField(max_length=100, default=None, allow_blank=True, allow_null=True)
    tgl_apkt_kirim_nyala = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = APKTTransJAR
        fields = '__all__'