from rest_framework import serializers 
from apps.users.models import Users

from .models import WP_TTD_ONLINE   
 
class WP_TTD_ONLINESerializers(serializers.ModelSerializer): 
    nama = serializers.CharField(max_length=80, allow_blank=True, allow_null=True, default=None)   
    nama_file = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, default=None)   
    group_file = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, default=None)   
    
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None)  
    class Meta:
        model = WP_TTD_ONLINE
        fields = '__all__'


class CDWP_TTD_ONLINESerializers(serializers.ModelSerializer):

    nama = serializers.CharField(max_length=80, allow_blank=True, allow_null=True, default=None)   
    nama_file = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, default=None)   
    group_file = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, default=None)   
    
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )  
    
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None)  


    class Meta:
        model = WP_TTD_ONLINE
        fields = '__all__'  

class UDWP_TTD_ONLINESerializers(serializers.ModelSerializer):
    nama = serializers.CharField(max_length=80, allow_blank=True, allow_null=True, default=None)   
    nama_file = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, default=None)   
    group_file = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, default=None)   
    
    id_user = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    )  
    
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=False,
        style={'base_template': 'input.html'}
    ) 
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    tgl_entri = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None) 
    tgl_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S" , default=None)  

    class Meta:
        model = WP_TTD_ONLINE
        fields = '__all__'