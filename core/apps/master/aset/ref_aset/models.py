from django.db import models
from apps.users.models import Users  
from apps.master.aset.ref_aset_status.models import RefAsetStatus 
from apps.master.aset.ref_aset_jenis.models import RefAsetJenis 
from apps.master.aset.ref_aset_manufaktur.models import RefAsetManufaktur 
from apps.master.aset.ref_aset_level.models import RefAsetLevel 
from apps.master.aset.ref_aset_lantai.models import RefAsetLantai
from apps.master.aset.ref_aset_ruangan.models import RefAsetRuangan
from apps.master.aset.ref_aset_kondisi.models import RefAsetKondisi
from apps.master.aset.ref_aset_rak.models import RefAsetRak
from apps.master.jaringan.ref_lokasi.models import RefLokasi

# Create your models here.
class RefAset(models.Model): 
    id_ref_aset = models.AutoField(primary_key=True, db_column='id_ref_aset')
    id_ref_aset_parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column='id_ref_aset_parent'
    )

    jenis_aset = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    lat = models.FloatField(default=None, blank=True, null=True , db_column='lat') 
    lon = models.FloatField(default=None, blank=True, null=True , db_column='lon') 
 
    #rl
    id_ref_aset_status = models.ForeignKey(
        RefAsetStatus, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_status',
        db_column='id_ref_aset_status'
    ) 
    id_ref_aset_jenis = models.ForeignKey(
        RefAsetJenis, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_jenis',
        db_column='id_ref_aset_jenis'
    ) 
    id_ref_aset_manufaktur = models.ForeignKey(
        RefAsetManufaktur, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_manufaktur',
        db_column='id_ref_aset_manufaktur'
    ) 
    id_ref_aset_level = models.ForeignKey(
        RefAsetLevel, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_level',
        db_column='id_ref_aset_level'
    ) 
    #blm dpt relasi
    #trans_pm
    id_trans_pm = models.IntegerField(default=None, blank=True, null=True) 

    #relsi kemana ?
    id_aset_mutasi = models.IntegerField(default=None, blank=True, null=True)

    id_ref_lokasi_1 = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_lokasi_1',
        db_column='id_ref_lokasi_1'
    )
    id_ref_lokasi_2 = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_lokasi_2',
        db_column='id_ref_lokasi_2'
    )
    id_ref_lokasi_3 = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_lokasi_3',
        db_column='id_ref_lokasi_3'
    )
    id_ref_lokasi_4 = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_lokasi_4',
        db_column='id_ref_lokasi_4'
    )

    tgl_buat = models.DateField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateField(auto_now=True, blank=True, null=True)

    no_aset_internal = models.IntegerField(default=None, blank=True, null=True)
    no_aset_external = models.IntegerField(default=None, blank=True, null=True)
    nama = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    no_seri = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tipe = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tahun = models.IntegerField(default=None, blank=True, null=True)
    dimensi_lebar = models.IntegerField(default=None, blank=True, null=True)
    dimensi_panjang = models.IntegerField(default=None, blank=True, null=True)
    dimensi_tinggi = models.IntegerField(default=None, blank=True, null=True)
    dimensi_satuan = models.IntegerField(default=None, blank=True, null=True) 
    massa_berat = models.IntegerField(default=None, blank=True, null=True)
    massa_satuan = models.IntegerField(default=None, blank=True, null=True)

    id_ref_aset_lantai = models.ForeignKey(
        RefAsetLantai, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_lantai',
        db_column='id_ref_aset_lantai'
    )
    id_ref_aset_ruangan = models.ForeignKey(
        RefAsetRuangan, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_ruangan',
        db_column='id_ref_aset_ruangan'
    )
    id_ref_aset_kondisi = models.ForeignKey(
        RefAsetKondisi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_kondisi',
        db_column='id_ref_kondisi_aset'
    )
    id_ref_aset_rak = models.ForeignKey(
        RefAsetRak, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_ref_aset_kondisi',
        db_column='id_ref_aset_rak'
    )

    class Meta:
        managed = False
        db_table = 'ref_aset'

    def __str__(self):
        return self.id_ref_aset

    
 
EXPORT_HEADERS = ['no_aset', 'kategori', 'nama_aset','station','penyulang','pengelola','no_seri','manufaktur','tipe','tahun','status_aset']
EXPORT_FIELDS = ['no_aset_internal', 'nama_aset_jenis', 'nama','nama_lokasi_1','nama_lokasi_3','nama_lokasi_4','no_seri','nama_manufaktur','tipe','tahun','nama_status']
EXPORT_RELATION_FIELD = [
            {'ref_aset_jenis':['nama_aset_jenis']},
            {'ref_lokasi_1':['nama_lokasi_1']},
            {'ref_lokasi_2':['nama_lokasi_2']},
            {'ref_lokasi_3':['nama_lokasi_3']},
            {'ref_lokasi_4':['nama_lokasi_4']},
            {'ref_lokasi_4':['nama_lokasi_4']},
            {'ref_aset_manufaktur':['nama_manufaktur']},
            {'ref_aset_status':['nama_status']},
        ] 