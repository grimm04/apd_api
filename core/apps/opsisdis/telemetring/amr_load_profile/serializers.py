from rest_framework import serializers
from .models import TelemetringAMRLoadProfile
from apps.master.opsisdis.amr_customer.models import TelemetringAMRCustomer

class SubRefAMRCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelemetringAMRCustomer
        fields = ['id', 'customer_rid', 'nama']


class TelemetringAMRLoadProfileSerializers(serializers.ModelSerializer):
    customer_rid = serializers.SlugRelatedField(
        queryset=TelemetringAMRLoadProfile.objects.all(),
        slug_field='customer_rid',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_customer = SubRefAMRCustomerSerializer(read_only=True, source='customer_rid')
    tgl = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    amp_r = serializers.IntegerField(default=None, allow_null=True)
    amp_s = serializers.IntegerField(default=None, allow_null=True)
    amp_t = serializers.IntegerField(default=None, allow_null=True)
    volt_r = serializers.IntegerField(default=None, allow_null=True)
    volt_s = serializers.IntegerField(default=None, allow_null=True)
    volt_t = serializers.IntegerField(default=None, allow_null=True)
    power_active = serializers.IntegerField(default=None, allow_null=True)
    power_reactive = serializers.IntegerField(default=None, allow_null=True)
    power_apparent = serializers.IntegerField(default=None, allow_null=True)
    frequency = serializers.IntegerField(default=None, allow_null=True)
    phase_r = serializers.IntegerField(default=None, allow_null=True)
    phase_s = serializers.IntegerField(default=None, allow_null=True)
    phase_t = serializers.IntegerField(default=None, allow_null=True)

    class Meta:
        model = TelemetringAMRLoadProfile
        fields = '__all__'