from django.db import models
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp 
from apps.users.models import Users
from apps.master.jaringan.ref_lokasi.models import RefLokasi


class TransEpPeralatan(models.Model):
    id_trans_ep_peralatan = models.BigAutoField(primary_key=True)
    id_trans_ep = models.ForeignKey(
        TransEp, default=None, on_delete=models.CASCADE, blank=True, null=True, db_column='id_trans_ep'
    )   
    peralatan_rc = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    rc_open = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    rc_close = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_rc_open = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status_rc_close = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_user_entri = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='%(class)s_user_entri',
        db_column='id_user_entri'
    ) 
    tgl_entri = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tgl_update = models.DateTimeField(auto_now=True, blank=True, null=True) 
    tgl = models.DateTimeField(blank=True, null=True) 
    id_peralatan = models.ForeignKey(
        RefLokasi, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='trans_ep_peralatan_peralatan',
        db_column='id_peralatan'
    )  

    class Meta:
        managed = False
        db_table = 'trans_ep_peralatan'
     
    def __str__(self):
        return self.id_trans_ep_peralatan
EXPORT_HEADERS = ['NO REKAP PADAM','JENIS PERALATAN','PERALATAN RC','RC OPEN','RC CLOSE', 'STATUS OPEN','STATUS CLOSE', 'TANGGAL','JAM']
EXPORT_FIELDS = ['no_event','jenis_keypoint','nama_lokasi','rc_open','rc_close','status_rc_open','status_rc_close','date_hari','jam']
EXPORT_RELATION_FIELD = [ 
    {
        'peralatan': [
            'nama_lokasi', 
        ],
        
    }, 
    {  
       'trans_ep': [
            'no_event', 
            'jenis_keypoint', 
        ]
    }
]
EXPORT_HEADERS_CAPTION = [{
    'row_start': 5,
    'header_row_start': 4,
    'data': [
        {'name': 'REKAP PELRALATAN RC', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        # {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # {'name': 'Penyulang', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # # {'name': 'Area', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A2:B2', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Status', 'column': 'A3:B3', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        # {'name': 'nama_gardu_induk', 'relation':'ref_parent_lokasi', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'nama_lokasi','relation':'ref_lokasi', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # # {'name': 'nama_area','relation':'ref_lokasi', 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'date_hari','relation':None, 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data','costum_label':True,'key_label':'date_range'},  
        {'name': 'status','relation':None, 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data','costum_label':True,'key_label':'status'},  
    ]
}]