from .models import TelemetringPenyulang
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializerGeneratePengukuran 
from .serializers import TelemetringPenyulangSerializers
from datetime import date
#generator 24 hour
from library.date_generator24 import datetime_range
from library.date_converter import date_converter_str  
from ..def_formula import formula

def schedule_api(): 
	try:
		today = date.today() 
		datum =today.strftime("%Y-%m-%d") 
		datetext = datetime_range(datum)  
		# get ref-lokasi id_ref_jenis_lokasi=6 // Penyulang
		ref_lokasi = RefLokasi.objects.filter(id_ref_jenis_lokasi=6,status_listrik=1).order_by('no_urut')  

		# print(ref_lokasi) 
 
		if not ref_lokasi:
			print('Gagal generate pengukuran beban - tidak ada data penyulang')  
		for data_raw in ref_lokasi:  
			ref_lokasi_serializer = RefLokasiSerializerGeneratePengukuran(data_raw, many=False) 
			
			if ref_lokasi_serializer: 
				penyulang = ref_lokasi_serializer.data     
				data = []
				for date_t in datetext:     
					#check apakah jam ini sudah generate
					new_date = date_converter_str(date=date_t) 
					tm_penyulang_hour = TelemetringPenyulang.objects.filter(id_lokasi=penyulang['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_penyulang') 
					if not tm_penyulang_hour:  
						jenis_layanan = ['KTT','NON KTT']
						if penyulang['parent_lokasi'].get('jenis_layanan') in jenis_layanan:
							#get jenis_layanan, def_pengukuran_teg_primer, def_pengukuran_teg_sekunder, def_nilai_cosq dari parent penyulang/ trafo_gi
							jenis = penyulang['parent_lokasi'].get('jenis_layanan')
							def_nilai_cosq = penyulang['parent_lokasi'].get('def_nilai_cosq')
							def_pengukuran_teg_primer = penyulang['parent_lokasi'].get('def_pengukuran_teg_primer')
							def_pengukuran_teg_sekunder = penyulang['parent_lokasi'].get('def_pengukuran_teg_sekunder') 
							
							if jenis == 'KTT':
								pengukuran = def_pengukuran_teg_primer
							elif jenis == 'NON KTT':
								pengukuran = def_pengukuran_teg_sekunder
							else :
								v = None
							#get default Pengukuran (v) dari trafo berdasarkan jenis_layanan
							v = formula(jenis=jenis,value=pengukuran) 
							cosq = formula(jenis='cosq',value=def_nilai_cosq)
							#get sinkron_data dari trafo apa penyulang
							sinkron_data =  penyulang['sinkron_data']

							data_mapper = dict({'id_lokasi': penyulang['id_ref_lokasi'], 
													'id_parent_lokasi': penyulang['id_parent_lokasi'],
													'datum':date_t ,
													'sinkron_data':sinkron_data ,
													'v':v,
													'cosq':cosq
													}) 
							data.append(data_mapper) 
				
				# print(data)
				serializer = TelemetringPenyulangSerializers(data=data, many=True)
				if serializer.is_valid():
					serializer.save()  
		print('Berhasil Generate pengukuran beban penyulang')  
	except:
        	print('Gagal generate pengukuran beban penyulang') 