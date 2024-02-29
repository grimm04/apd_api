from rest_framework import serializers
from .models import TelemetringAMREnergi
from apps.master.opsisdis.amr_customer.models import TelemetringAMRCustomer

class SubRefAMRCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelemetringAMRCustomer
        fields = ['id', 'customer_rid', 'nama']


class TelemetringAMREnergiSerializers(serializers.ModelSerializer):
    customer_rid = serializers.SlugRelatedField(
        queryset=TelemetringAMREnergi.objects.all(),
        slug_field='customer_rid',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    ref_customer = SubRefAMRCustomerSerializer(read_only=True, source='customer_rid')
    tgl = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    kwh = serializers.IntegerField(default=None, allow_null=True)
    kvarh = serializers.IntegerField(default=None, allow_null=True)
    kvah = serializers.IntegerField(default=None, allow_null=True)
    tgl_maxdem = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f", read_only=True)
    maxdem = serializers.IntegerField(default=None, allow_null=True)
    rate1 = serializers.IntegerField(default=None, allow_null=True)
    rate2 = serializers.IntegerField(default=None, allow_null=True)
    rate3 = serializers.IntegerField(default=None, allow_null=True)
    rate1_prev = serializers.IntegerField(default=None, allow_null=True)
    rate2_prev = serializers.IntegerField(default=None, allow_null=True)
    rate3_prev = serializers.IntegerField(default=None, allow_null=True)
    kwh_prev = serializers.IntegerField(default=None, allow_null=True)
    fk = serializers.IntegerField(default=None, allow_null=True)
    kvarh_prev = serializers.IntegerField(default=None, allow_null=True)
    tgl_capture = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    tgl_prev = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    kvah_prev = serializers.IntegerField(default=None, allow_null=True)

    class Meta:
        model = TelemetringAMREnergi
        fields = '__all__'