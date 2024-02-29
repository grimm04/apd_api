from django.db import models
from django.db.models import Q

from apps.users.models import Users
from apps.master.jaringan.ref_jenis_lokasi.models import RefJenisLokasi


class RefLokasiTree(models.Model):
    id_ref_lokasi = models.AutoField(primary_key=True)
    # nama_lokasi = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    # id_parent_lokasi = models.ForeignKey(
    #     'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_parent_lokasi',
    #     related_name='children'
    # )
    # tree_jaringan = models.IntegerField(default=None, blank=True, null=True)
    # alamat = models.CharField(
    #     max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    # )
    # coverage = models.CharField(
    #     max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    # )
    # kva = models.IntegerField(default=None, blank=True, null=True)
    # phase = models.CharField(
    #     max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    # )
    # lat = models.FloatField(default=None, blank=True, null=True)
    # lon = models.FloatField(default=None, blank=True, null=True)
    # id_ref_jenis_lokasi = models.ForeignKey(
    #     RefJenisLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_jenis_lokasi'
    # )
    # status_listrik = models.IntegerField(default=None, blank=True, null=True)
    # no_tiang = models.CharField(
    #     max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    # )
    # id_user_entri = models.ForeignKey(
    #     Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
    #     db_column='id_user_entri'
    # )
    # id_user_update = models.ForeignKey(
    #     Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
    #     db_column='id_user_update'
    # )
    # tgl_entri = models.DateField(auto_now_add=True, blank=True, null=True)
    # tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    nama_lokasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    kode_lokasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jumlah_pelanggan = models.IntegerField(default=None, blank=True, null=True)
    jumlah_jurusan = models.IntegerField(default=None, blank=True, null=True)
    jenis_trafo = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')

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
    id_parent_lokasi = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_parent_lokasi',
        related_name='children'
    )

    tree_jaringan = models.IntegerField(default=None, blank=True, null=True)
    alamat = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
    )
    coverage = models.CharField(
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', default=None, blank=True, null=True
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

    class TStatus(models.TextChoices): 
        ACTIVE = '1'
        INACTIVE = '0'

    status_listrik = models.IntegerField(blank=True, null=True, choices=TStatus.choices, default=TStatus.ACTIVE)
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
        related_name='children_gardu_induk'
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
    fungsi_scada = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    kapasitas = models.IntegerField(default=None, blank=True, null=True)
    sub_sistem = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pemilik = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status_trafo = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    i_max = models.IntegerField(default=None, blank=True, null=True)
    ratio_ct = models.IntegerField(default=None, blank=True, null=True)
    fk_meter_pembanding = models.IntegerField(default=None, blank=True, null=True)
    primer_tegangan_max = models.IntegerField(default=None, blank=True, null=True)
    primer_tegangan_min = models.IntegerField(default=None, blank=True, null=True)
    sekunder_tegangan_min = models.IntegerField(default=None, blank=True, null=True)
    sekunder_tegangan_max = models.IntegerField(default=None, blank=True, null=True)
    sinkron_data = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jenis_layanan = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id_i = models.IntegerField(default=None, blank=True, null=True)
    id_v = models.IntegerField(default=None, blank=True, null=True)
    id_p = models.IntegerField(default=None, blank=True, null=True)
    id_amr = models.IntegerField(default=None, blank=True, null=True)
    id_portal_ext = models.IntegerField(default=None, blank=True, null=True)
    url_webservice = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jenis_gi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    faktor_meter = models.IntegerField(default=None, blank=True, null=True)
    faktor_kali = models.IntegerField(default=None, blank=True, null=True)
    dcc = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    def_pengukuran_teg_primer = models.DecimalField(default=150,max_digits=5, decimal_places=2,blank=True, null=True)
    def_pengukuran_teg_sekunder = models.DecimalField(default=20.5,max_digits=5, decimal_places=2,blank=True, null=True)
    def_nilai_cosq = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)



    @property
    def nama_jenis_lokasi(self):
        return self.id_ref_jenis_lokasi.nama_jenis_lokasi 

    class Meta:
        managed = False
        db_table = 'ref_lokasi'

    # def get_all_children(self, include_self=True):
    #     r = []
    #     if include_self:
    #         r.append(self)
    #     for c in RefLokasiTree.objects.filter(id_parent_lokasi=self):
    #         _r = c.get_all_children(include_self=True)
    #         if 0 < len(_r):
    #             r.extend(_r)
    #     return r

    # def get_children_filters(self, include_self=True):
    #     filters = Q(pk=0)
    #     if include_self:
    #         filters |= Q(pk=self.pk)
    #     for c in RefLokasiTree.objects.filter(id_parent_lokasi=self):
    #         _r = c.get_children_filters(include_self=True)
    #         if _r:
    #             filters |= _r
    #     return filters

    # def get_all_children(self, include_self=True, id_ref_lokasi=None):
    #     if not id_ref_lokasi:
    #         return RefLokasiTree.objects.filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi') \
    #             .filter(self.get_children_filters(include_self))
    #     else:
    #         id_ref_lokasi = id_ref_lokasi.strip()
    #         id_ref_lokasi = id_ref_lokasi.split(',')
    #         return RefLokasiTree.objects.filter(id_ref_lokasi__in=id_ref_lokasi).filter(tree_jaringan=1) \
    #             .order_by('id_parent_lokasi', 'nama_lokasi').filter(self.get_children_filters(include_self))


class RefLokasiTreeUpdate(models.Model):
    id_ref_lokasi = models.AutoField(primary_key=True)
    id_parent_lokasi = models.IntegerField(default=None, blank=True, null=True)
    id_ref_jenis_lokasi = models.IntegerField(default=None, blank=True, null=True)
    id_gardu_induk = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_lokasi'
