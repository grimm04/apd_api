from django.db import models 
from apps.master.working_permit.wm_bagian.models import WP_BAGIAN
from apps.working_permit.wp_master_sop_jsa.models import WP_MASTER_SOP_JSA
from apps.working_permit.wp_hirarc.models import WP_HIRARC
from apps.users.models import Users
from apps.master.pegawai.perusahaan.models import Perusahaan


class WP_ONLINE(models.Model):  
    id_wp_online = models.AutoField(primary_key=True) 
    nomor_formulir = models.CharField(blank=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    jenis_pekerjaan = models.CharField(blank=True,max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    pekerjaan_dilakukan = models.CharField(blank=True,max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    lokasi_pekerjaan = models.CharField(blank=True,max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    nama_pengawas = models.CharField(blank=True,max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    nama_pengawask3 = models.CharField(blank=True,max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    nama_koordinator_vendor = models.CharField(blank=True,max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    manuver = models.BooleanField(default=False)
    grounding = models.BooleanField(default=False) 
    petugas_zona1 = models.BooleanField(default=False) 
    petugas_zona2 = models.BooleanField(default=False) 
    petugas_zona3 = models.BooleanField(default=False)  
    klasifikasi1 = models.BooleanField(default=False) 
    klasifikasi2 = models.BooleanField(default=False) 
    klasifikasi3 = models.BooleanField(default=False) 
    klasifikasi4 = models.BooleanField(default=False) 
    klasifikasi5 = models.BooleanField(default=False) 
    klasifikasi6 = models.BooleanField(default=False) 
    klasifikasi7 = models.BooleanField(default=False) 
    klasifikasi8 = models.BooleanField(default=False) 
    klasifikasi9 = models.BooleanField(default=False)  
    klasifikasi10 = models.CharField(blank=True, max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    prosedur1 = models.BooleanField(default=False) 
    prosedur2 = models.BooleanField(default=False) 
    prosedur3 = models.BooleanField(default=False) 
    prosedur4 = models.BooleanField(default=False) 
    prosedur5 = models.BooleanField(default=False) 
    prosedur6 = models.BooleanField(default=False) 
    prosedur7 = models.BooleanField(default=False) 
    prosedur8 = models.BooleanField(default=False) 
    prosedur9 = models.BooleanField(default=False)  
    prosedur10 = models.CharField(blank=True, max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    lampiran1 = models.BooleanField(default=False) 
    lampiran2 = models.BooleanField(default=False) 
    lampiran3 = models.BooleanField(default=False) 
    lampiran4 = models.BooleanField(default=False) 

    status_pekerjaan = models.CharField(blank=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    status_persetujuan = models.IntegerField(default=None, null=True, blank=True)
    id_wp_on = models.CharField(blank=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    id_bidang = models.CharField(blank=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    qrcode = models.CharField(blank=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    telepon_pengawask3 = models.CharField(blank=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    telepon_pekerja = models.CharField(blank=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    keterangan_reject = models.CharField(blank=True, max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    jabatan_direksi = models.CharField(blank=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    file_dok = models.CharField(blank=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS') 
    
    nomor_sop = models.ForeignKey(
        WP_MASTER_SOP_JSA, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_sop',
        db_column='nomor_sop'
    )  
    vendor_pelaksana = models.ForeignKey(
        Perusahaan, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_sop',
        db_column='vendor_pelaksana'
    )  

    id_wp_master_bagian = models.ForeignKey(
        WP_BAGIAN, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wp_master_bagian',
        db_column='id_wp_master_bagian'
    )  

    id_user_direksi = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_direksi',
        db_column='id_user_direksi'
    )
    id_user_closing = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_closing',
        db_column='id_user_closing'
    )
    id_wp_hirarc = models.ForeignKey(
        WP_HIRARC, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_wp_hirarc',
        db_column='id_wp_hirarc'
    )
    # id_pengawas = models.ForeignKey(
    #     Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_pengawas',
    #     db_column='id_pengawas'
    # )
    # id_pengawask3 = models.ForeignKey(
    #     Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_pengawask3',
    #     db_column='id_pengawask3'
    # ) 
     
    id_user_persetujuan = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_persetujuan',
        db_column='id_user_persetujuan'
    ) 


    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )

    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    tgl_pekerjaan = models.DateTimeField(default=None, blank=True, null=True) 
    tgl_pekerjaan_selesai = models.DateTimeField(default=None, blank=True, null=True) 
    tgl_persetujuan = models.DateTimeField(default=None, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'wp_online'

    def __str__(self):
        return self.id_wp_online 

    
    # def save(self, *args, **kwargs):
    #     # today = datetime.date.today()
    #     bagian = self.id_wp_master_bagian
    #     # today_string = today.strftime('%y%m%d')
    #     # next_invoice_number = '01'
    #     print(bagian)
    #     last_invoice = WP_ONLINE.objects.count()
    #     if not last_invoice:
    #         nf = 1  
    #     new_invoice_int = last_invoice + 1
    #     #nomor/bagian/bulan/UP2D/tahun
    #     new_nf = new_invoice_int + '/'+ bagian
    #     self.nomor_formulir = new_invoice_int + '/'+ bagian

    #     super(WP_ONLINE, self).save(*args, **kwargs)

        # bagian = self.id_wp_master_bagian__ept
        # print(bagian)
        # nomor_formulir = WP_ONLINE.objects.all().order_by('id').last()
        # if not nomor_formulir:
        #     nf = 1
        # nf = nomor_formulir.id_wp_online 
        # new_invoice_int = nf + 1
        # #nomor/bagian/bulan/UP2D/tahun
        # new_nf = new_invoice_int + '/'+ bagian
        # return new_nf
