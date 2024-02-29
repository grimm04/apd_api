from rest_framework import serializers
from .models import TelemetringAMRCustomer
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubRefLokasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi', 'nama_lokasi', 'kode_lokasi', 'id_parent_lokasi']

class TelemetringAMRCustomerSerializers(serializers.ModelSerializer):
    customer_rid = serializers.IntegerField(default=None, allow_null=True)
    meter_id = serializers.CharField(max_length=24, allow_null=True, allow_blank=True)
    meter_type = serializers.IntegerField(default=None, allow_null=True)
    rate = serializers.CharField(max_length=2, allow_null=True, allow_blank=True)
    modem_adr = serializers.IntegerField(default=None, allow_null=True)
    nama = serializers.CharField(max_length=40, allow_null=True, allow_blank=True)
    alamat = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    lok = serializers.CharField(max_length=70, allow_null=True, allow_blank=True)
    daya = serializers.IntegerField(default=None, allow_null=True)
    bapm = serializers.CharField(max_length=8, allow_null=True, allow_blank=True)
    faktor_kali = serializers.IntegerField(default=None, allow_null=True)
    nofa = serializers.CharField(max_length=8, allow_null=True, allow_blank=True)
    goltarif = serializers.CharField(max_length=8, allow_null=True, allow_blank=True)
    kodegardu = serializers.CharField(max_length=32, allow_null=True, allow_blank=True)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_lokasi')

    class Meta:
        model = TelemetringAMRCustomer
        fields = '__all__'

class UDTelemetringAMRCustomerSerializers(serializers.ModelSerializer):
    meter_id = serializers.CharField(max_length=24, allow_null=True, allow_blank=True)
    meter_type = serializers.IntegerField(default=None, allow_null=True, required=False)
    rate = serializers.CharField(max_length=2, allow_null=True, allow_blank=True , required=False)
    modem_adr = serializers.IntegerField(default=None, allow_null=True , required=False)
    nama = serializers.CharField(max_length=40, allow_null=True, allow_blank=True, required=False)
    alamat = serializers.CharField(max_length=100, allow_null=True, allow_blank=True, required=False)
    lok = serializers.CharField(max_length=70, allow_null=True, allow_blank=True, required=False)
    daya = serializers.IntegerField(default=None, allow_null=True, required=False)
    bapm = serializers.CharField(max_length=8, allow_null=True, allow_blank=True, required=False)
    faktor_kali = serializers.IntegerField(default=None, allow_null=True, required=False)
    nofa = serializers.CharField(max_length=8, allow_null=True, allow_blank=True, required=False)
    goltarif = serializers.CharField(max_length=8, allow_null=True, allow_blank=True, required=False)
    kodegardu = serializers.CharField(max_length=32, allow_null=True, allow_blank=True, required=False)
    id_lokasi = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_lokasi = SubRefLokasiSerializer(read_only=True, source='id_lokasi')

    class Meta:
        model = TelemetringAMRCustomer
        fields = '__all__'