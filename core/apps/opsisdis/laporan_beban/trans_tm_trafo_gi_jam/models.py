from django.db import models


EXPORT_HEADERS = ['Tanggal','Jam', 'Gardu Induk','Trafo', 'Daya Aktif (MW)','Arus (A)', ]
EXPORT_FIELDS = ['date_hari','jam', 'nama_gardu_induk', 'nama_lokasi','p', 'i']
EXPORT_RELATION_FIELD = [
    {
        'ref_lokasi': [
            'nama_lokasi', 
        ]
    },
    {
        'ref_parent_lokasi': [ 
            'nama_gardu_induk',
        ], 
    },
]
EXPORT_HEADERS_HARIAN_NON_KTT = [{
    'row_start': 7,
    'header_row_start': 6,
    'data': [
        {'name': 'Laporan Beban Tegangan Trafo GI NON KTT PerJam', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        {'name': 'Trafo', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # {'name': 'Area', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'nama_gardu_induk', 'relation':'ref_parent_lokasi', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'nama_lokasi','relation':'ref_lokasi', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'nama_area','relation':'ref_lokasi', 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]

EXPORT_HEADERS_HARIAN_KTT = [{
    'row_start': 7,
    'header_row_start': 6,
    'data': [
        {'name': 'Laporan Beban Tegangan Trafo GI KTT PerJam', 'column': 'A1:J1', 'width': 15, 'merge': True,'align':'center','type':'row'},
        {'name': 'Gardu Induk', 'column': 'A2:B2', 'width': 15, 'merge': True,'align':'left','type':'row'},
        {'name': 'Trafo', 'column': 'A3:B3', 'width': 15, 'merge': True,'align':'left','type':'row'},
        # {'name': 'Area', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'Tanggal', 'column': 'A4:B4', 'width': 10, 'merge': True,'align':'left','type':'row'}, 
        {'name': 'nama_gardu_induk', 'relation':'ref_parent_lokasi', 'column': 'C2:C2', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'nama_lokasi','relation':'ref_lokasi', 'column': 'C3:C3', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        # {'name': 'nama_area','relation':'ref_lokasi', 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
        {'name': 'date_hari','relation':None, 'column': 'C4:C4', 'width': 10, 'merge': False,'align':'left','type':'data'}, 
    ]
}]