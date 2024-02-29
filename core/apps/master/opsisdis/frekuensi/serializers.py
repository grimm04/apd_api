from rest_framework import serializers
from .models import Frekuensi

class FrekuensiSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=50)
    status = serializers.IntegerField()
    lokasi = serializers.CharField(max_length=50)
    general_slaveid = serializers.IntegerField()
    general_address = serializers.IntegerField()
    general_scale = serializers.IntegerField()
    general_mode = serializers.CharField(max_length=50)
    general_koneksi = serializers.CharField(max_length=50)
    general_logging = serializers.IntegerField()
    general_interval_logging = serializers.IntegerField()
    serial_port = serializers.CharField(max_length=50)
    serial_baudrate = serializers.IntegerField()
    serial_bytesize = serializers.IntegerField()
    serial_parity = serializers.CharField(max_length=50)
    serial_stopbits = serializers.IntegerField()
    serial_xonxoff = serializers.IntegerField()
    ip_host = serializers.CharField(max_length=50)
    ip_port = serializers.IntegerField()
    # datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Frekuensi
        fields = '__all__'
