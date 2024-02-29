from rest_framework import serializers 

from .models import TransTmPenyulangBulan   
from apps.additional.serializers import IDSRef_LokasiSerializer
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class SubRefParentLokasiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RefLokasi
        fields = ['id_ref_lokasi','nama_lokasi', 'kode_lokasi', 'id_parent_lokasi','no_urut']

class SubRefParentLokasiGISerializer(serializers.ModelSerializer): 
    nama_gardu_induk = serializers.CharField(source='nama_lokasi')   
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'kode_lokasi', 'id_parent_lokasi','no_urut','nama_gardu_induk']

class TransTmPenyulangBulanSerializers(serializers.ModelSerializer): 
    datum = serializers.DateTimeField(allow_null=True, required=False)
    p_min = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_max = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_avg = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_tgl_min = serializers.DateTimeField(allow_null=True, required=False)
    p_tgl_max = serializers.DateTimeField(allow_null=True, required=False) 
    tgl_entri = serializers.DateTimeField(allow_null=True, required=False)
    tgl_update = serializers.DateTimeField(allow_null=True, required=False)
    id_user_entri = serializers.IntegerField(allow_null=True, required=False)
    id_user_update = serializers.IntegerField(allow_null=True, required=False)
    i_min = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_max = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_avg = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False) 
    p_max_siang = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_min_siang = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_avg_siang = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_tgl_max_siang = serializers.DateTimeField(allow_null=True, required=False)
    p_tgl_min_siang = serializers.DateTimeField(allow_null=True, required=False)
    p_max_malam = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_min_malam = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_avg_malam = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    p_tgl_max_malam = serializers.DateTimeField(allow_null=True, required=False)
    p_tgl_min_malam = serializers.DateTimeField(allow_null=True, required=False)
    i_max_siang = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_min_siang = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_avg_siang = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_tgl_max_siang = serializers.DateTimeField(allow_null=True, required=False)
    i_tgl_min_siang = serializers.DateTimeField(allow_null=True, required=False)
    i_max_malam = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_min_malam = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_avg_malam = serializers.DecimalField(max_digits=18, decimal_places=2, allow_null=True, required=False)
    i_tgl_max_malam = serializers.DateTimeField(allow_null=True, required=False)
    i_tgl_min_malam = serializers.DateTimeField(allow_null=True, required=False)
    id_ref_lokasi_area = serializers.IntegerField(allow_null=True, required=False)
    id_ref_lokasi_gi = serializers.SlugRelatedField(
        queryset= RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_lokasi_trafo_gi = serializers.SlugRelatedField(
        queryset= RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    id_ref_lokasi_penyulang = serializers.SlugRelatedField(
        queryset= RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    date_hari = serializers.DateTimeField(read_only=True, source='datum', format="%b %Y")  
    ref_lokasi_gi = SubRefParentLokasiGISerializer(read_only=True, source='id_ref_lokasi_gi')
    ref_lokasi_trafo_gi = SubRefParentLokasiSerializer(read_only=True, source='id_ref_lokasi_trafo_gi')
    ref_lokasi_penyulang = SubRefParentLokasiSerializer(read_only=True, source='id_ref_lokasi_penyulang')

    class Meta:
        model = TransTmPenyulangBulan
        fields = '__all__'

class LaporanBebanPenyulangBulanPDFSerializers(serializers.ModelSerializer):    
    datum  = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    ref_lokasi_gi = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi_gi') 
    ref_lokasi_penyulang = IDSRef_LokasiSerializer(read_only=True, source='id_ref_lokasi_penyulang')
    class Meta:
        model = TransTmPenyulangBulan
        fields = ['datum','i_avg','i_max','i_max_siang','i_max_malam','p_avg','p_max','p_max_siang','p_max_malam','ref_lokasi_gi','ref_lokasi_penyulang','load_faktor']