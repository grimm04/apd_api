import re

from rest_framework import serializers
from .models import Menu


class CRMenuSerializers(serializers.ModelSerializer):
    # queryset = Menu.objects.all()
    # idParent = serializers.RelatedField(source='menu.id', read_only=True, allow_null=True)
    # idParent = serializers.RelatedField(queryset=queryset, source='menu.id', allow_null=True)
    idParent = serializers.SlugRelatedField(
        queryset=Menu.objects.all(),
        slug_field='id',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    display = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    path = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    icon = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    privileges = serializers.CharField(allow_blank=True, allow_null=True)
    hidden = serializers.BooleanField(default=False)
    search = serializers.BooleanField(default=False)
    divider = serializers.BooleanField(default=False)
    no = serializers.IntegerField(default=0)
    updatedAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'

    # def get_roles(self, obj):
    #     _roles = obj.roles
    #     stripped = _roles.strip('][').split(', ')
    #     stripped = [re.sub('\'', '', x) for x in stripped]
    #     return stripped


class UDMenuSerializers(serializers.ModelSerializer):
    queryset = Menu.objects.all()
    # idParent = serializers.RelatedField(queryset=queryset, source='menu.id', allow_null=True)
    idParent = serializers.SlugRelatedField(
        queryset=Menu.objects.all(),
        slug_field='id',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    display = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    path = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    icon = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    hidden = serializers.BooleanField(default=False)
    search = serializers.BooleanField(default=False)
    divider = serializers.BooleanField(default=False)
    no = serializers.IntegerField(default=0)

    class Meta:
        model = Menu
        fields = '__all__'


class UDBatchMenuSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(default=None)
    no = serializers.IntegerField(default=None)

    class Meta:
        model = Menu
        fields = ['id', 'no']
