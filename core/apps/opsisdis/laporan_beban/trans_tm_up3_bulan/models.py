 
from django.db import models  
from apps.master.jaringan.ref_lokasi.models import RefLokasi 

class TransTmUp3Bulan(models.Model):
    id_trans_tm_up3_bulan = models.AutoField(primary_key=True)
    datum = models.DateTimeField(blank=True, null=True)
    p_min = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_max = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_avg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_tgl_min = models.DateTimeField(blank=True, null=True)
    p_tgl_max = models.DateTimeField(blank=True, null=True) 
    id_ref_lokasi_up3 = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_lokasi_up3'
    )
    tgl_entri = models.DateTimeField(blank=True, null=True)
    tgl_update = models.DateTimeField(blank=True, null=True)
    id_user_entri = models.IntegerField(blank=True, null=True)
    id_user_update = models.IntegerField(blank=True, null=True)
    i_min = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_max = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_avg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_max_siang = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_min_siang = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_avg_siang = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_tgl_max_siang = models.DateTimeField(blank=True, null=True)
    p_tgl_min_siang = models.DateTimeField(blank=True, null=True)
    p_max_malam = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_min_malam = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_avg_malam = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p_tgl_max_malam = models.DateTimeField(blank=True, null=True)
    p_tgl_min_malam = models.DateTimeField(blank=True, null=True)
    i_max_siang = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_min_siang = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_avg_siang = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_tgl_max_siang = models.DateTimeField(blank=True, null=True)
    i_tgl_min_siang = models.DateTimeField(blank=True, null=True)
    i_max_malam = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_min_malam = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_avg_malam = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    i_tgl_max_malam = models.DateTimeField(blank=True, null=True)
    i_tgl_min_malam = models.DateTimeField(blank=True, null=True)
    load_faktor = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_tm_up3_bulan'
    
    def __str__(self):
        return self.id_trans_tm_up3_bulan 

EXPORT_HEADERS = ['Tanggal','Gardu Induk','UP', 'Beban Max(MW)','Beban Rata-Rata(MW)','Beban Max Siang(MW)','Beban Max Malam(MW)','Ampere Max(A)','Ampere Rata-Rata(A)','Ampere Max Siang(A)','Ampere Max Malam(A)','Load Faktor']
EXPORT_FIELDS = ['date_hari', 'nama_gardu_induk', 'nama_lokasi','p_max', 'p_avg','p_max_siang','p_max_malam','i_max','i_avg','i_max_siang','i_max_malam','load_faktor']
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi_up3': [
            'nama_lokasi',
             'nama_gardu_induk', 
        ]
    }, 
]
EXPORT_HEADERS_HARIAN = [{
    'row_start': 7,
    'header_row_start': 6,
    'data': [
        {'name': 'Laporan Beban Tegangan UP PerBulan', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        {'name': 'UP', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # {'name': 'Area', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Bulan Tahun', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'nama_gardu_induk', 'relation':'ref_lokasi_up3', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'nama_lokasi','relation':'ref_lokasi_penyulang', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'nama_area','relation':'ref_lokasi', 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data','costum_label':True}, 
    ]
}]
