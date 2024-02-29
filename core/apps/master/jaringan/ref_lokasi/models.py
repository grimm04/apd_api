from django.db import models  
from apps.users.models import Users
from apps.master.jaringan.ref_jenis_lokasi.models import RefJenisLokasi\

from apps.master.wilayah.ref_province.models import RefProvince
from apps.master.wilayah.ref_regency.models import RefRegency 
from apps.master.wilayah.ref_district.models import RefDistrict
from apps.master.jaringan.ref_jenis_pembangkit.models import RefJenisPembangkit

class RefLokasiChild(models.Model):
    id_parent_lokasi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_parent_lokasi',
        related_name='children'
    )
    nama_lokasi = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'ref_lokasi'


class RefLokasi(models.Model):

    class RFSTATUS(models.TextChoices):
        ACTIVE = '1'
        INACTIVE = '0'
 
    id_ref_lokasi = models.AutoField(primary_key=True)
    nama_lokasi = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kode_lokasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jumlah_pelanggan = models.IntegerField(default=None, blank=True, null=True)
    jumlah_jurusan = models.IntegerField(default=None, blank=True, null=True)
    jenis_trafo = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fungsi_scada = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kapasitas = models.IntegerField(default=None, blank=True, null=True)
    sub_sistem = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pemilik = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_trafo = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    i_max = models.IntegerField(default=None, blank=True, null=True)
    ratio_ct = models.IntegerField(default=None, blank=True, null=True)
    ratio_vt = models.IntegerField(default=None, blank=True, null=True)
    fk_meter_pembanding = models.IntegerField(default=None, blank=True, null=True)
    primer_tegangan_max = models.IntegerField(default=None, blank=True, null=True)
    primer_tegangan_min = models.IntegerField(default=None, blank=True, null=True)
    sekunder_tegangan_min = models.IntegerField(default=None, blank=True, null=True)
    sekunder_tegangan_max = models.IntegerField(default=None, blank=True, null=True)
    sinkron_data = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_layanan = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_i = models.IntegerField(default=None, blank=True, null=True)
    id_v = models.IntegerField(default=None, blank=True, null=True)
    id_p = models.IntegerField(default=None, blank=True, null=True)
    id_amr = models.IntegerField(default=None, blank=True, null=True)
    id_portal_ext = models.IntegerField(default=None, blank=True, null=True)
    url_webservice = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_gi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    faktor_meter = models.IntegerField(default=None, blank=True, null=True)
    faktor_kali = models.IntegerField(default=None, blank=True, null=True)
    dcc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  
    def_pengukuran_teg_primer = models.DecimalField(default=150,max_digits=5, decimal_places=2,blank=True, null=True)
    def_pengukuran_teg_sekunder = models.DecimalField(default=20.5,max_digits=5, decimal_places=2,blank=True, null=True)
    def_nilai_cosq = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)

    id_parent_lokasi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_parent_lokasi',
        related_name='children'
    )

    id_penyulang = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_penyulang',
        related_name='%(class)s_penyulang'
    )
    id_zone = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_zone',
        related_name='%(class)s_zone'
    )
    id_section = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_section',
        related_name='%(class)s_section'
    )
    id_segment = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_segment',
        related_name='%(class)s_segment'
    )

    id_uid = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_uid',
        related_name='%(class)s_uid'
    )
    id_up3_1 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_up3_1',
        related_name='%(class)s_up3_1'
    )
    id_up3_2 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_up3_2',
        related_name='%(class)s_up3_2'
    )
    id_ulp_1 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ulp_1',
        related_name='%(class)s_ulp_1'
    )
    id_ulp_2 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ulp_2',
        related_name='%(class)s_ulp_2'
    )
    id_unit_pembangkit = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_unit_pembangkit',
        related_name='%(class)s_unit_pembangkit'
    )
    id_pembangkit = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_pembangkit',
        related_name='%(class)s_pembangkit'
    )
    id_gardu_induk = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_gardu_induk',
        related_name='%(class)s_gardu_induk'
    )
    id_trafo_gi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_trafo_gi',
        related_name='%(class)s_trafo_gi'
    )
    id_gardu_distribusi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_gardu_distribusi',
        related_name='%(class)s_gardu_distribusi'
    )
    id_trafo_gd = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_trafo_gd',
        related_name='%(class)s_trafo_gd'
    )
    id_gardu_hubung = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_gardu_hubung',
        related_name='%(class)s_gardu_hubung'
    )
    id_up2b = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_up2b',
        related_name='%(class)s_up2b'
    )
    id_ref_province = models.ForeignKey(
        RefProvince, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_province',
        related_name='ref_province'
    ) 
    id_ref_regency = models.ForeignKey(
        RefRegency, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_regency',
        related_name='ref_regency'
    ) 
    id_ref_district = models.ForeignKey(
        RefDistrict, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_district',
        related_name='ref_district'
    ) 
    id_ref_jenis_pembangkit = models.ForeignKey(
        RefJenisPembangkit, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_jenis_pembangkit',
        related_name='ref_jeni_pembangkit'
    ) 

    tree_jaringan = models.IntegerField(default=None, blank=True, null=True)
    alamat = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    coverage = models.CharField(
        max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    kva = models.IntegerField(default=None, blank=True, null=True)
    phase = models.CharField(
        max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    lat = models.FloatField(default=None, blank=True, null=True)
    lon = models.FloatField(default=None, blank=True, null=True)
    id_ref_jenis_lokasi = models.ForeignKey(
        RefJenisLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_jenis_lokasi'
    )

    status_listrik = models.IntegerField(blank=True, null=True, choices=RFSTATUS.choices, default=RFSTATUS.ACTIVE)
    no_tiang = models.CharField(
        max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    jenis_jaringan = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    status_penyulang = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )

    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)
    no_urut = models.IntegerField(default=None,blank=True, null=True)
    pelanggan_tm = models.IntegerField(default=None,blank=True, null=True)
    pelanggan_vip = models.IntegerField(default=None,blank=True, null=True)
    ufr = models.IntegerField(default=None,blank=True, null=True)


    def nama_gardu_induk(self):
        return self.id_gardu_induk.nama_lokasi
 
        
    class Meta:
        managed = False
        db_table = 'ref_lokasi'

    # def get_children_filters(self, include_self=True):
    #     filters = Q(pk=0)
    #     if include_self:
    #         filters |= Q(pk=self.pk)
    #     for c in RefLokasi.objects.filter(id_parent_lokasi=self):
    #         _r = c.get_children_filters(include_self=True)
    #         if _r:
    #             filters |= _r
    #     return filters

    # def get_all_children(self, include_self=True, id_ref_lokasi=None):
    #     if not id_ref_lokasi:
    #         return RefLokasi.objects.filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')\
    #             .filter(self.get_children_filters(include_self))
    #     else:
    #         id_ref_lokasi = id_ref_lokasi.strip()
    #         id_ref_lokasi = id_ref_lokasi.split(',')
    #         return RefLokasi.objects.filter(id_ref_lokasi__in=id_ref_lokasi).filter(tree_jaringan=1)\
    #             .order_by('id_parent_lokasi', 'nama_lokasi').filter(self.get_children_filters(include_self))


class RefLokasiTemp(models.Model):

    class RFSTATUS(models.TextChoices):
        ACTIVE = '1'
        INACTIVE = '0'

    id_ref_lokasi = models.AutoField(primary_key=True)
    nama_lokasi = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kode_lokasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jumlah_pelanggan = models.IntegerField(default=None, blank=True, null=True)
    jumlah_jurusan = models.IntegerField(default=None, blank=True, null=True)
    jenis_trafo = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fungsi_scada = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kapasitas = models.IntegerField(default=None, blank=True, null=True)
    sub_sistem = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pemilik = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_trafo = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    i_max = models.IntegerField(default=None, blank=True, null=True)
    ratio_ct = models.IntegerField(default=None, blank=True, null=True)
    ratio_vt = models.IntegerField(default=None, blank=True, null=True)
    fk_meter_pembanding = models.IntegerField(default=None, blank=True, null=True)
    primer_tegangan_max = models.IntegerField(default=None, blank=True, null=True)
    primer_tegangan_min = models.IntegerField(default=None, blank=True, null=True)
    sekunder_tegangan_min = models.IntegerField(default=None, blank=True, null=True)
    sekunder_tegangan_max = models.IntegerField(default=None, blank=True, null=True)
    sinkron_data = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_layanan = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_i = models.IntegerField(default=None, blank=True, null=True)
    id_v = models.IntegerField(default=None, blank=True, null=True)
    id_p = models.IntegerField(default=None, blank=True, null=True)
    id_amr = models.IntegerField(default=None, blank=True, null=True)
    id_portal_ext = models.IntegerField(default=None, blank=True, null=True)
    url_webservice = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_gi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    faktor_meter = models.IntegerField(default=None, blank=True, null=True)
    faktor_kali = models.IntegerField(default=None, blank=True, null=True)
    dcc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  
    def_pengukuran_teg_primer = models.DecimalField(default=150,max_digits=5, decimal_places=2,blank=True, null=True)
    def_pengukuran_teg_sekunder = models.DecimalField(default=20.5,max_digits=5, decimal_places=2,blank=True, null=True)
    def_nilai_cosq = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    # childs = models.ManyToManyField("self", symmetrical=False, db_column='id_parent_lokasi')
    event_upload = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  


    id_parent_lokasi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_parent_lokasi',
        related_name='children'
    )

    id_penyulang = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_penyulang',
        related_name='%(class)s_penyulang'
    )
    id_zone = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_zone',
        related_name='%(class)s_zone'
    )
    id_section = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_section',
        related_name='%(class)s_section'
    )
    id_segment = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_segment',
        related_name='%(class)s_segment'
    )

    id_uid = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_uid',
        related_name='%(class)s_uid'
    )
    id_up3_1 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_up3_1',
        related_name='%(class)s_up3_1'
    )
    id_up3_2 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_up3_2',
        related_name='%(class)s_up3_2'
    )
    id_ulp_1 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ulp_1',
        related_name='%(class)s_ulp_1'
    )
    id_ulp_2 = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ulp_2',
        related_name='%(class)s_ulp_2'
    )
    id_unit_pembangkit = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_unit_pembangkit',
        related_name='%(class)s_unit_pembangkit'
    )
    id_pembangkit = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_pembangkit',
        related_name='%(class)s_pembangkit'
    )
    id_gardu_induk = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_gardu_induk',
        related_name='%(class)s_gardu_induk'
    )
    id_trafo_gi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_trafo_gi',
        related_name='%(class)s_trafo_gi'
    )
    id_gardu_distribusi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_gardu_distribusi',
        related_name='%(class)s_gardu_distribusi'
    )
    id_trafo_gd = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_trafo_gd',
        related_name='%(class)s_trafo_gd'
    )
    id_gardu_hubung = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_gardu_hubung',
        related_name='%(class)s_gardu_hubung'
    ) 
    id_up2b = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_up2b',
        related_name='%(class)s_up2b'
    )
    id_ref_province = models.ForeignKey(
        RefProvince, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_province',
        related_name='tmp_ref_province'
    ) 
    id_ref_regency = models.ForeignKey(
        RefRegency, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_regency',
        related_name='tmp_ref_regency'
    ) 
    id_ref_district = models.ForeignKey(
        RefDistrict, on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_district',
        related_name='tmp_ref_district'
    ) 

    tree_jaringan = models.IntegerField(default=None, blank=True, null=True)
    alamat = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    coverage = models.CharField(
        max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    kva = models.IntegerField(default=None, blank=True, null=True)
    phase = models.CharField(
        max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    lat = models.FloatField(default=None, blank=True, null=True)
    lon = models.FloatField(default=None, blank=True, null=True)
    id_ref_jenis_lokasi = models.ForeignKey(
        RefJenisLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_jenis_lokasi'
    )

    status_listrik = models.IntegerField(blank=True, null=True, choices=RFSTATUS.choices, default=RFSTATUS.ACTIVE)
    no_tiang = models.CharField(
        max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    jenis_jaringan = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    status_penyulang = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )

    tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)
    no_urut = models.IntegerField(default=None,blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'ref_lokasi_temp_upload'

    # def __str__(self):
    #     return self.id_ref_lokasi


class RefLokasiTempDelete(models.Model):
    id_user = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ref_lokasi_temp_upload'

    def __str__(self):
        return self.id_user
