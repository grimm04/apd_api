from .models import TelemetringPembangkit
from apps.master.jaringan.ref_lokasi.models import RefLokasi
from apps.master.jaringan.ref_lokasi.serializers import RefLokasiSerializerGeneratePengukuran 
from .serializers import TelemetringPembangkitSerializers
from datetime import date
#generator 24 hour
from library.date_generator24 import datetime_range
from library.date_converter import date_converter_str  
from base.global_conf import global_conf
def schedule_api(): 
	try:
		today = date.today() 
		datum =today.strftime("%Y-%m-%d") 
		datetext = datetime_range(datum)  
		# get ref-lokasi id_ref_jenis_lokasi=2 // Pembangkit
		ref_lokasi = RefLokasi.objects.filter(id_ref_jenis_lokasi=2,status_listrik=1).order_by('no_urut')  

		# print(ref_lokasi) 
 
		if not ref_lokasi:
			print('Gagal generate pengukuran beban - tidak ada data pembangkit')  
		for data_raw in ref_lokasi:  
			ref_lokasi_serializer = RefLokasiSerializerGeneratePengukuran(data_raw, many=False) 
			
			if ref_lokasi_serializer: 
				pembangkit = ref_lokasi_serializer.data   
				data = []
				for date_t in datetext:     
					#check apakah jam ini sudah generate
					new_date = date_converter_str(date=date_t) 
					tm_pembangkit_hour = TelemetringPembangkit.objects.filter(id_lokasi=pembangkit['id_ref_lokasi'],datum=new_date).order_by('-id_trans_tm_pembangkit') 
					if not tm_pembangkit_hour:  
						# sinkron_data =  pembangkit['sinkron_data'] 
						data_mapper = dict({'id_lokasi': pembangkit['id_ref_lokasi'], 
												'id_parent_lokasi': pembangkit['id_parent_lokasi'],
												'datum':date_t ,
												'no_urut_cell':pembangkit['no_urut'],
												# 'sinkron_data':sinkron_data , 
												}) 
						data.append(data_mapper) 
				
				# print(data)
				serializer = TelemetringPembangkitSerializers(data=data, many=True)
				if serializer.is_valid():
					serializer.save()  
		print('Berhasil Generate pengukuran beban pembangkit')  
	except:
        	print('Gagal generate pengukuran beban pembangkit') 