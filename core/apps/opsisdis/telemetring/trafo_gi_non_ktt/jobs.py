from pyrsistent import v
from .models import TelemetringTrafoGI
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializerGeneratePengukuran 
from .serializers import TelemetringTrafoGISerializers
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
		# get ref-lokasi id_ref_jenis_lokasi=5 // Trafo GI Non KTT
		ref_lokasi = RefLokasi.objects.filter(id_ref_jenis_lokasi=5,status_listrik=1, jenis_layanan__isnull=False).order_by('no_urut')   
		# print(ref_lokasi)
		if not ref_lokasi:
			print('Gagal generate pengukuran beban - tidak ada data trafo gi')  
		for data_raw in ref_lokasi:  
			ref_lokasi_serializer = RefLokasiSerializerGeneratePengukuran(data_raw, many=False)  
			if ref_lokasi_serializer: 
				trafo_gi = ref_lokasi_serializer.data  
				data = []
				for date_t in datetext:     
					#check apakah jam ini sudah generate
					new_date = date_converter_str(date=date_t) 
					tm_trafo_gi_hour = TelemetringTrafoGI.objects.filter(id_lokasi=trafo_gi['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_trafo_gi') 
				 
					if not tm_trafo_gi_hour:  
						jenis = trafo_gi['jenis_layanan'] 
						def_pengukuran_teg_primer = trafo_gi['def_pengukuran_teg_primer']
						def_pengukuran_teg_sekunder = trafo_gi['def_pengukuran_teg_sekunder']
						if jenis == 'KTT':
							pengukuran = def_pengukuran_teg_primer
						elif jenis == 'NON KTT':
							pengukuran = def_pengukuran_teg_sekunder
						else :
							v = None
						# get data default cosq trafo_gi 
						def_nilai_cosq = trafo_gi['def_nilai_cosq']
						sinkron_data = trafo_gi['sinkron_data']

						v = formula(jenis=jenis,value=pengukuran)  
						cosq = formula(jenis='cosq',value=def_nilai_cosq)   
						data_mapper = dict({'id_lokasi': trafo_gi['id_ref_lokasi'], 
												'id_parent_lokasi': trafo_gi['id_parent_lokasi'],
												'datum':date_t,
												'v':v,
												'cosq':cosq,
												'sinkron_data':sinkron_data,
												'no_urut_cell':trafo_gi['no_urut'],
												}) 
						data.append(data_mapper)  
				serializer = TelemetringTrafoGISerializers(data=data, many=True)
				if serializer.is_valid():
					serializer.save()  
		print('Berhasil Generate pengukuran beban trafo gi')  
	except:
        	print('Gagal generate pengukuran beban trafo gi') 