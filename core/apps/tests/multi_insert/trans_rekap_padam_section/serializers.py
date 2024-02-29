from rest_framework import serializers
from apps.tests.multi_insert.trans_rekap_padam.models import TransRekapPadam
from .models import TransRekapPadamSection

class RekapPadamPeralatanSerializer(serializers.ModelSerializer): 
    id_trans_rekap_padam = serializers.SlugRelatedField(
        queryset=TransRekapPadam.objects.all(),
        slug_field='id_trans_rekap_padam',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )  
    section = serializers.CharField(max_length=100, required=False, allow_null=True,)
    beban_masuk = serializers.DecimalField(max_digits=8, decimal_places=3, required=False, allow_null=True,)
    jam_masuk = serializers.DateTimeField(required=False, allow_null=True,)
    inputer = serializers.CharField(max_length=20, required=False, allow_null=True,)
    inputer_at = serializers.DateTimeField(required=False, allow_null=True,)
    beban_sebelum = serializers.DecimalField(max_digits=8, decimal_places=3, required=False, allow_null=True,)
    jam_sebelum = serializers.DateTimeField(required=False, allow_null=True,)
    durasi = serializers.DecimalField(max_digits=8, decimal_places=2, required=False, allow_null=True,)
    ens = serializers.DecimalField(max_digits=8, decimal_places=3, required=False, allow_null=True,)

    class Meta:
        model   = TransRekapPadamSection 
        fields  = '__all__'