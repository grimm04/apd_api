from rest_framework import serializers
from .models import Roles


class CRRolesSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    level = serializers.IntegerField(default=0)
    privileges = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    updatedAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Roles
        fields = '__all__'


class UDRolesSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    level = serializers.IntegerField(default=0)
    privileges = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Roles
        fields = '__all__'
