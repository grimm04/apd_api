from statistics import mode
from django.db import models
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.users.models import Users

EXPORT_HEADERS = [ 'Gardu Induk', 'Trafo GI', 'NO Ururt Cell','Tanggal','Jam', 'Arus (A)', 'Tegangan (kV)', 'Cosq','Daya Aktif (MW)']
EXPORT_FIELDS = ['nama_parent_lokasi',  'nama_lokasi', 'no_urut_cell', 'date_hari','jam', 'i', 'v','cosq', 'p',]
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi': [
            'nama_lokasi'
        ]
    },
    {
        'ref_parent_lokasi': [
            'nama_parent_lokasi'
        ]
    },
]


EXPORT_HEADERS_CAPTION_KTT = [{
    'row_start': 7,
    'header_row_start': 6,
    'data': [
        {'name': 'Laporan Pengukuran Trafo GI KTT', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        {'name': 'Trafo GI', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'nama_parent_lokasi', 'relation':'ref_parent_lokasi', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'nama_lokasi','relation':'ref_lokasi', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'},  
        {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]
EXPORT_HEADERS_CAPTION_NON_KTT = [{
    'row_start': 7,
    'header_row_start': 6,
    'data': [
        {'name': 'Laporan Pengukuran Trafo GI NON KTT', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        {'name': 'Trafo GI', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'nama_parent_lokasi', 'relation':'ref_parent_lokasi', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'nama_lokasi','relation':'ref_lokasi', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'},  
        {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]


class TelemetringTrafoGI(models.Model):
    id_trans_tm_trafo_gi = models.AutoField(primary_key=True)
    datum = models.DateTimeField(default=None, blank=True, null=True)
    i = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    v = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    p = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    q = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    f = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True)
    cosq = models.DecimalField(default=None,max_digits=5, decimal_places=2,blank=True, null=True) 
    no_urut_cell = models.IntegerField(default=None,null=True,blank=True) 
    id_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_lokasi',
        related_name='%(class)s_id_lokasi'
    )
    id_parent_lokasi = models.ForeignKey(
        RefLokasi, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_parent_lokasi',
        related_name='%(class)s_id_parent_lokasi'
    )
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    )
    id_user_update = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_update',
        db_column='id_user_update'
    )
    sinkron_data = models.CharField(default=None,max_length=30, null=True,blank=True) 
    id_ref_lokasi_area = models.IntegerField(default=None, null=True,blank=True)
    class Meta:
        managed = True
        db_table = 'trans_tm_trafo_gi'

    def __str__(self):
        return self.id_trans_tm_trafo_gi