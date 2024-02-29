from pickle import TRUE
from rest_framework import serializers

from apps.users.models import Users 
from apps.master.aset.ref_aset.models import RefAset

from .models import RefAsetDoc 
 
class RefAsetDocSerializersList(serializers.ModelSerializer):
    # user_entri = UserDetailSerializerDef(read_only=True, source='id_user_entri')
    class Meta:
        model = RefAsetDoc
        fields = '__all__'

class CDRefAsetDocSerializers(serializers.ModelSerializer):

    nama_file = serializers.CharField(max_length=100, default=None, allow_null=True) 
    status = serializers.IntegerField(default=None, allow_null=True) 
    tipe = serializers.CharField(max_length=50, default=None, allow_null=True) 
    jenis = serializers.CharField(max_length=50, default=None, allow_null=True) 
    deskripsi = serializers.CharField(max_length=50, default=None, allow_null=True) 
    
    id_ref_aset = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
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

    tgl_entri = serializers.DateField(format="%Y-%m-%d", read_only=True)
    tgl_update = serializers.DateField(format="%Y-%m-%d", read_only=TRUE) 

    class Meta:
        model = RefAsetDoc
        fields = '__all__' 


class UDRefAsetDocSerializers(serializers.ModelSerializer):
    queryset = RefAsetDoc.objects.all()

    nama_file = serializers.CharField(max_length=100, required=False) 
    status = serializers.IntegerField(required=False) 
    tipe = serializers.CharField(max_length=50, required=False) 
    jenis = serializers.CharField(max_length=50, required=False) 
    deskripsi = serializers.CharField(max_length=50, required=False) 
    
    id_ref_aset = serializers.SlugRelatedField(
        queryset=RefAset.objects.all(),
        slug_field='id_ref_aset',
        allow_null=True,
        style={'base_template': 'input.html'}
    )
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False, 
        style={'base_template': 'input.html'}
    )
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    ) 

    class Meta:
        model = RefAsetDoc
        fields = '__all__'
