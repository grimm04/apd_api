from rest_framework import serializers
from .models import USER_HIS_PASSWORD 
from apps.users.models import Users
 


class USER_HIS_PASSWORDSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)  
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    class Meta:
        model = USER_HIS_PASSWORD
        fields = '__all__'


class CRUSER_HIS_PASSWORDCSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)  
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = USER_HIS_PASSWORD
        fields = '__all__'


class UDUSER_HIS_PASSWORDSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, default=None, allow_blank=True, allow_null=True)  
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = USER_HIS_PASSWORD
        fields = '__all__'
