from rest_framework import serializers 
from apps.users.models import Users

from .models import WP_PERTANYAAN_QRC   
 
class WP_PERTANYAAN_QRCSerializers(serializers.ModelSerializer): 
    pertanyaan = serializers.CharField(max_length=300, allow_blank=True, allow_null=True, default=None) 
    point = serializers.IntegerField(default=None)
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
        model = WP_PERTANYAAN_QRC
        fields = '__all__'


class CDWP_PERTANYAAN_QRCSerializers(serializers.ModelSerializer):

    pertanyaan = serializers.CharField(max_length=300, allow_blank=True, allow_null=True, default=None) 
    point = serializers.IntegerField(default=None)
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
        model = WP_PERTANYAAN_QRC
        fields = '__all__'  

class UDWP_PERTANYAAN_QRCSerializers(serializers.ModelSerializer):
    pertanyaan = serializers.CharField(max_length=300, allow_blank=True, allow_null=True, default=None) 
    point = serializers.IntegerField(default=None)
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
        model = WP_PERTANYAAN_QRC
        fields = '__all__'