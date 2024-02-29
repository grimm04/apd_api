from base.global_conf import global_conf

def formula(jenis=None,value =None):
    gc = global_conf()    
    v = value
    if jenis and jenis == 'KTT':
        v = value if value != None else gc['def_pengukuran_teg_primer']
    elif jenis and jenis == 'NON KTT':
        v = value if value != None else gc['def_pengukuran_teg_sekunder'] 
    elif jenis and jenis == 'cosq':
        v = value if value != None else gc['def_nilai_cosq']
    else:
        v = None
    return v

def formula_daya(jenis_pengukuran=None,jenis_layanan=None, def_pengukuran=None,arus =None,tegangan=None,cosq=None):  
    if jenis_pengukuran == 'trafo_gi':
        # def_pengukuran = formula(jenis=jenis_layanan,value=def_pengukuran) 
        # arus*1.73205*150)/1000*0.95  
        daya =  (float(arus)*1.73205*float(tegangan))/1000*float(cosq)
    elif jenis_pengukuran =='penyulang':
        # DAYA AKTIF (MW) = (ARUS (A) x 1.73205 x Tegangan(KV) di entrikan x1000 x cosq) / 1000000
        daya =  (float(arus)*1.73205*float(tegangan)*1000 *float(cosq))/1000000
    else:
        daya = None
    return daya
