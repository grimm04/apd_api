# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TransEp(models.Model):
    id_trans_ep = models.BigAutoField()
    no_event = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    no_apkt = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam_padam = models.DateTimeField(blank=True, null=True)
    penyebab = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    beban_padam = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    indikasi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lbs_manual = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_keypoint = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_keypoint = models.BigIntegerField(blank=True, null=True)
    penyulang_gi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    up3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ulp = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jlh_gardu_padam = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pelanggan_tm = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pelanggan_vip = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    wilayah_padam = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cuaca = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    recloser = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gardu_induk = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    r = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    s = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    t = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    n = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jam_buka = models.DateTimeField(blank=True, null=True)
    jam_tutup = models.DateTimeField(blank=True, null=True)
    jam_trip = models.DateTimeField(blank=True, null=True)
    jam_normal = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gardu_hubung = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jenis_padam = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jml_ggn_tahun = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jml_ggn_bulan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    indikator_kerja = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sectionalizer_kerja = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_wrc = models.DateTimeField(blank=True, null=True)
    jam_isolasi = models.DateTimeField(blank=True, null=True)
    jam_pengusutan = models.DateTimeField(blank=True, null=True)
    penyebab_ggn = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    jenis_pemeliharaan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_proteksi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sepatetik_trip = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    koordinasi_proteksi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gagal_ar = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan_proteksi = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    penyulang_fdir = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    keterangan_penyulang_fdir = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fai_arus_ggn_hmi = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fai_mtrz_hmi = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    keterangan_fai_mtrz_hmi = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fai_fiohl_hmi = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    dispat_kalsel_1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalsel_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalteng_1 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalteng_2 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan_fai_fiohl_hmi = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ens = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    kategori_ggn = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    keterangan_ggn = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_penyulang_fdir = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_fai_mtrz_hmi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_fai_fiohl_hmi = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gangguan_ditemukan = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    motorized = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    posting = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    dispat_kalteng_3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dispat_kalsel_3 = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    aco_kerja = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    peralatan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    photo = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    id_up3 = models.BigIntegerField(blank=True, null=True)
    id_ulp = models.BigIntegerField(blank=True, null=True)
    tgl_entri = models.DateTimeField(blank=True, null=True)
    tgl_update = models.DateTimeField(blank=True, null=True)
    id_user_entri = models.IntegerField(blank=True, null=True)
    id_user_update = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_ep'


class TransEpLaporan(models.Model):
    id_trans_ep_laporan = models.BigAutoField()
    id_trans_ep = models.BigIntegerField(blank=True, null=True)
    tegangan = models.CharField(max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    piket = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    peralatan = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_buka = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    jam_tutup = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    arus_gangguan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    resume = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eksekusi_rc = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eksekusi_mc = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_s = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_g = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_ep_laporan'


class TransEpPeralatan(models.Model):
    id_trans_ep_peralatan = models.BigAutoField()
    id_trans_ep = models.BigIntegerField(blank=True, null=True)
    peralatan_rc = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    rc_open = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    rc_close = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_rc_open = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_rc_close = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_user_entri = models.IntegerField(blank=True, null=True)
    tgl_entri = models.DateTimeField(blank=True, null=True)
    tgl_update = models.DateTimeField(blank=True, null=True)
    tgl = models.DateTimeField(blank=True, null=True)
    id_peralatan = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_ep_peralatan'


class TransEpSection(models.Model):
    id_trans_ep_section = models.BigAutoField()
    id_trans_ep = models.BigIntegerField(blank=True, null=True)
    section = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    beban_masuk = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    jam_masuk = models.DateTimeField(blank=True, null=True)
    id_user_entri = models.IntegerField(blank=True, null=True)
    tg_entri = models.DateTimeField(blank=True, null=True)
    beban_sebelum = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    jam_sebelum = models.DateTimeField(blank=True, null=True)
    durasi = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ens = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_ep_section'
