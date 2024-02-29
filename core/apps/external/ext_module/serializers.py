from rest_framework import serializers

from .models import ExtModule


class ExtModuleSerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=100)

    class Meta:
        model = ExtModule
        fields = '__all__'
