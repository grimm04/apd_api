 
from django.db import models  
from apps.master.jaringan.ref_lokasi.models import RefLokasi

class TransTmSubsistem(models.Model):
    id_trans_tm_subsistem = models.AutoField(primary_key=True)
    datum = models.DateTimeField(blank=True, null=True)
    i = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    v = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    p = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    q = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    f = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True) 
    tgl_entri = models.DateTimeField(blank=True, null=True)
    tgl_update = models.DateTimeField(blank=True, null=True)
    id_user_entri = models.IntegerField(blank=True, null=True)
    id_user_update = models.IntegerField(blank=True, null=True) 
    sinkron_data = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) 
    cosq = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    no_urut_cell = models.IntegerField(blank=True, null=True)

    id_parent_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_parent_lokasi', related_name='subsistem_parent_lokasi'
    )
    id_ref_lokasi_subsistem = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_lokasi_subsistem', related_name='subsistem_ref_lokasi'
    )

    id_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_lokasi' , related_name='subsistem_lokasi'
    )
    class Meta:
        managed = False
        db_table = 'trans_tm_subsistem'
    
    def __str__(self):
        return self.id_trans_tm_subsistem 

EXPORT_HEADERS = ['Tanggal','Jam', 'Sub Sistem', 'Arus (A)', 'Daya Aktif (MW)']
EXPORT_FIELDS = ['date_hari','jam', 'nama_lokasi', 'i','p']
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi_subsistem': [
            'nama_lokasi', 
        ]
    }, 
]
EXPORT_HEADERS_HARIAN = [{
    'row_start': 6,
    'header_row_start': 5,
    'data': [
        {'name': 'Laporan Beban Tegangan Sub Sistem PerJam', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'}, 
        {'name': 'Sub Sistem', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A3:B3', 'width': 10, 'merge': True,'align':'left','type':'row'},  
        {'name': 'nama_lokasi','relation':'ref_lokasi_subsistem', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'},  
        {'name': 'date_hari','relation':None, 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]