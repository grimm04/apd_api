from rest_framework import serializers
from apps.tests.multi_insert.trans_rekap_padam.models import TransRekapPadam
from .models import TransRekapPadamPeralatan
class RekapPadamPeralatanSerializer(serializers.serializerserializer): 
    id_trans_rekap_padam = serializers.SlugRelatedField(
        queryset=TransRekapPadam.objects.all(),
        slug_field='id_trans_rekap_padam',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 
    peralatan_rc = serializers.DecimalField(max_digits=18, decimal_places=0, required=False)
    rc_open = serializers.CharField(max_length=50, required=False)
    rc_close = serializers.CharField(max_length=50, required=False)
    status_rc_open = serializers.CharField(max_length=50, required=False)
    status_rc_close = serializers.CharField(max_length=50, required=False)
    inputer = serializers.CharField(max_length=20, required=False)
    inputer_at = serializers.DateTimeField(required=False)
    updater_at = serializers.DateTimeField(required=False)
    tgl = serializers.DateTimeField(required=False)
    id_peralatan = serializers.IntegerField(required=False)

    class Meta:
        model   = TransRekapPadamPeralatan
        fields  = '__all__'