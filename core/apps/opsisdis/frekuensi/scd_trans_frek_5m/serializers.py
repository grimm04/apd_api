from rest_framework import serializers
from .models import Frekuensi5M

class Frekuensi5MSerializers(serializers.ModelSerializer):
    id_meter = serializers.IntegerField(default=None, allow_null=True)
    value_2 = serializers.IntegerField(default=None, allow_null=True)
    statusdata_2 = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    datum_2 = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    datum_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")

    class Meta:
        model = Frekuensi5M
        fields = '__all__'