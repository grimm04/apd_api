from pickle import TRUE
from rest_framework import serializers

from apps.users.models import Users 
from apps.master.aset.ref_aset.models import RefAset
from apps.master.aset.ref_aset_jenis.models import RefAsetJenis


from .models import RefAsetExAtr 
 

class CDRefAsetExAtrSerializers(serializers.ModelSerializer):

    nama = serializers.CharField(max_length=100, default=None, allow_null=True) 
    satuan = serializers.CharField(max_length=100, default=None, allow_null=True)   
    status = serializers.IntegerField(default=1, allow_null=True) 

    id_ref_aset_jenis = serializers.SlugRelatedField(
        queryset=RefAsetJenis.objects.all(),
        slug_field='id_ref_aset_jenis',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=True,
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
        model = RefAsetExAtr
        fields = '__all__' 


class UDRefAsetExAtrSerializers(serializers.ModelSerializer):
    queryset = RefAsetExAtr.objects.all()

    nama = serializers.CharField(max_length=100, required=False)  
    satuan = serializers.CharField(max_length=100, required=False)  
    status = serializers.IntegerField(required=False) 
    
    id_ref_aset_jenis = serializers.SlugRelatedField(
        queryset=RefAsetJenis.objects.all(),
        slug_field='id_ref_aset_jenis',
        allow_null=True,
        required=False,
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
        model = RefAsetExAtr
        fields = '__all__'
