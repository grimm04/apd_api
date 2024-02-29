 
from django.db import models  
from apps.master.jaringan.ref_lokasi.models import RefLokasi
 
class TransTmUp3Jam(models.Model):
    id_trans_tm_up3 = models.AutoField(primary_key=True)
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
    id_ref_lokasi_up3 = models.IntegerField(blank=True, null=True)
    cosq = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    no_urut_cell = models.IntegerField(blank=True, null=True)
    id_parent_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_parent_lokasi' , related_name='up3_parent_lokasi'
    )
    id_ref_lokasi_up3 = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_ref_lokasi_up3' , related_name='up3_ref_lokasi'
    )

    id_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_lokasi' , related_name='up3_lokasi'
    )

    class Meta:
        managed = False
        db_table = 'trans_tm_up3'
    
    def __str__(self):
        return self.id_trans_tm_up3 

EXPORT_HEADERS = ['Tanggal','Jam', 'Gardu Induk','Up3', 'Arus (A)', 'Daya Aktif (MW)']
EXPORT_FIELDS = ['date_hari','jam', 'nama_gardu_induk', 'nama_lokasi', 'i','p']
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi_up3': [
            'nama_lokasi', 
        ]
    },
    {
        'ref_lokasi_up3': [ 
            'nama_gardu_induk',
        ], 
    },
]
EXPORT_HEADERS_HARIAN = [{
    'row_start': 7,
    'header_row_start': 6,
    'data': [
        {'name': 'Laporan Beban Tegangan Up3 PerJam', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        {'name': 'Up3', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # {'name': 'Area', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'nama_gardu_induk', 'relation':'ref_lokasi_up3', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'nama_lokasi','relation':'ref_lokasi_up3', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'nama_area','relation':'ref_lokasi', 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]