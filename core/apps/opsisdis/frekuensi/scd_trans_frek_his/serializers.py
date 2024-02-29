from rest_framework import serializers
from .models import FrekuensiHIS
from django.utils import timezone

class FrekuensiHISSerializers(serializers.ModelSerializer):
    id_meter = serializers.IntegerField(default=None, allow_null=True)
    value_2 = serializers.IntegerField(default=None, allow_null=True)
    statusdata_2 = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")

    class Meta:
        model = FrekuensiHIS
        fields = '__all__'