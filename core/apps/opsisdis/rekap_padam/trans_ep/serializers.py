from rest_framework import serializers

from apps.users.models import Users
from apps.master.opsisdis.rekap_padam.ref_ep_penyebab_ggn.models import RefEpPenyebabGgn
from apps.master.opsisdis.rekap_padam.ref_ep_penyebab_ggn.serializers import RefEpPenyebabGgnserializer
from .models import TransEp
from apps.master.jaringan.ref_lokasi.models import RefLokasi   
from apps.additional.serializers import UserDetailSerializerDef ,RefJenisLokasierializer,ReflokasiZone,ReflokasiSection,ReflokasiPenyulang,ReflokasiUp3,ReflokasiUlp,ReflokasiGI,ReflokasiPenyulang,ReflokasiZone
import datetime
from apps.master.opsisdis.rekap_padam.ref_ep_indikasi.serializers import RefEpIndikasierializer
from apps.master.opsisdis.rekap_padam.ref_ep_cuaca.serializers import RefEpCuacaserializer
from apps.master.opsisdis.rekap_padam.ref_ep_indikasi.models import RefEpIndikasi
from apps.master.opsisdis.rekap_padam.ref_ep_cuaca.models import RefEpCuaca
from apps.opsisdis.rekap_padam.trans_ep_section.models import TransEpSection
from apps.master.opsisdis.rekap_padam.ref_ep_fdir.models import RefEpFdir
   

class ReflokasiKeypoint(serializers.ModelSerializer):  
    ref_jenis_lokasi = RefJenisLokasierializer(source='id_ref_jenis_lokasi')
    gardu_induk = ReflokasiGI(read_only=True, source='id_gardu_induk') 
    penyulang = ReflokasiPenyulang(read_only=True, source='id_penyulang') 
    section = ReflokasiSection(read_only=True, source='id_section') 
    zone = ReflokasiZone(read_only=True, source='id_zone')  
    # up3 = ReflokasiUp3(read_only=True, source='id_up3_1') 
    # ulp = ReflokasiUlp(read_only=True, source='id_ulp_1') 
    nama_gardu_induk = serializers.SerializerMethodField(source="get_nama_gardu_induk")
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'id_ref_jenis_lokasi','ref_jenis_lokasi','id_gardu_induk','id_penyulang','id_section','id_zone','gardu_induk',
        'penyulang','section','zone','nama_gardu_induk']
    
    def get_nama_gardu_induk(self,obj):
        if obj.id_gardu_induk:
            return obj.id_gardu_induk.nama_lokasi
class TransEpSectionSerializers(serializers.ModelSerializer):     
    jam_masuk = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')  
    class Meta:
        model = TransEpSection
        fields = '__all__' 

class TransEpSectionSerializers(serializers.ModelSerializer):     
    jam_masuk = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')  
    class Meta:
        model = TransEpSection
        fields = '__all__'
class AllNorelationTransEpSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransEp
        fields = '__all__'     

class TransEpSerializers(serializers.ModelSerializer):   
    id_keypoint = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_up3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
     
    id_ulp = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi', 
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
     
    keypoint = ReflokasiKeypoint(read_only=True, source='id_keypoint')  
    ref_ep_indikasi = RefEpIndikasierializer(read_only=True, source='id_ref_ep_indikasi') 
    ref_ep_penyebab_ggn = RefEpPenyebabGgnserializer(read_only=True, source='id_ref_ep_penyebab_ggn') 
    ref_ep_cuaca = RefEpCuacaserializer(read_only=True, source='id_ref_ep_cuaca') 
    up3 = ReflokasiUp3(read_only=True, source='id_up3') 
    ulp = ReflokasiUlp(read_only=True, source='id_ulp')  
    user_entri = UserDetailSerializerDef(read_only=True, source='id_user_entri') 
    user_update = UserDetailSerializerDef(read_only=True, source='id_user_update')   

    # trans_ep_section = TransEpSectionSerializers(many=False, read_only=True, source='id_trans_ep') 
    trans_ep_section = TransEpSectionSerializers(many=True,read_only=True)
    durasi = serializers.SerializerMethodField(source='get_durasi',read_only=True) 
    durasi_nyala_bertahap = serializers.SerializerMethodField(source='get_durasi_nyala_bertahap',read_only=True)
    ens = serializers.SerializerMethodField(source='get_ens',read_only=True)
    durasi_normal = serializers.SerializerMethodField(source='get_durasi_normal',read_only=True)
    durasi_isolasi = serializers.SerializerMethodField(source='get_durasi_isolasi',read_only=True)
    durasi_wrc = serializers.SerializerMethodField(source='get_durasi_wrc',read_only=True)
    durasi_pengusutan = serializers.SerializerMethodField(source='get_durasi_pengusutan',read_only=True)
    durasi_perbaikan = serializers.SerializerMethodField(source='get_durasi_perbaikan',read_only=True)
    durasi_recovery = serializers.SerializerMethodField(source='get_durasi_recovery',read_only=True)
    status = serializers.SerializerMethodField(source='get_status',read_only=True)
    total_gangguan_month = serializers.SerializerMethodField(source='get_total_gangguan_month',read_only=True) 
    total_gangguan_year = serializers.SerializerMethodField(source='get_total_gangguan_year',read_only=True) 


    class Meta:
        model = TransEp
        fields = '__all__' 

    def convert_null(self,value=None):
        if value:
            return float(value) if value != None or value != ""  else 0
        return 0

    def d_now(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
        date  = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f')   
        return date

    def to_minutes(self,minutes=None):
        if minutes:
            minutes = minutes.total_seconds() / 60
            return round(minutes,2)
        return 0
        

    def convert_datum(self, value=None):
        if value:
            value = value.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
            value = datetime.datetime.strptime(value,'%Y-%m-%d %H:%M:%S.%f') 
            return value
        return None
        
    def get_durasi(self,obj):
        durasi = None
        date = self.d_now()  
        if not obj.jam_buka  and not obj.jam_tutup: 
            if obj.jam_trip:
                durasi = date  - self.convert_datum(value=obj.jam_trip)
                durasi = '{} hari, {} jam, {} menit, {} detik'.format(durasi.days,durasi.seconds//3600,(durasi.seconds//60)%60,durasi.seconds % 60)  
        elif not obj.jam_trip  and obj.jam_tutup :
            if obj.jam_buka: 
                durasi = date  - self.convert_datum(value=obj.jam_buka)
                durasi = '{} hari, {} jam, {} menit, {} detik'.format(durasi.days,durasi.seconds//3600,(durasi.seconds//60)%60,durasi.seconds % 60)   
        elif  obj.jam_buka and obj.jam_tutup  :
            durasi = obj.jam_tutup  - obj.jam_buka
            durasi = '{} hari, {} jam, {} menit, {} detik'.format(durasi.days,durasi.seconds//3600,(durasi.seconds//60)%60,durasi.seconds % 60) 
        elif  obj.jam_tutup and obj.jam_trip:
            durasi = obj.jam_tutup   - obj.jam_trip 
            durasi = '{} hari, {} jam, {} menit, {} detik'.format(durasi.days,durasi.seconds//3600,(durasi.seconds//60)%60,durasi.seconds % 60)   
        else:
            durasi =  None
        return durasi
    
    def get_durasi_minute(self,obj):
        durasi = 0
        date = self.d_now()  
        if not obj.jam_buka  and not obj.jam_tutup: 
            if obj.jam_trip:  
                durasi = date  - self.convert_datum(value=obj.jam_trip)
                durasi = self.to_minutes(minutes=durasi)
        elif not obj.jam_trip  and obj.jam_tutup :
            if obj.jam_buka:   
                durasi = date  - self.convert_datum(value=obj.jam_buka)
                durasi = self.to_minutes(minutes=durasi)
        elif  obj.jam_buka and obj.jam_tutup  :
            durasi = obj.jam_tutup  - obj.jam_buka 
            durasi = self.to_minutes(minutes=durasi)
        elif  obj.jam_tutup and obj.jam_trip:
            durasi = obj.jam_tutup   - obj.jam_trip  
            durasi = self.to_minutes(minutes=durasi)
        else:
            durasi =  0
        return durasi
    def get_durasi_nyala_bertahap(self,obj):
        date = self.d_now()  
        durasi = 0
        if obj.jam_tutup and not obj.jam_normal:
            if obj.trans_ep_section.first():
                section = obj.trans_ep_section.first().jam_masuk 
                jam_masuk = section.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
                jam_masuk = datetime.datetime.strptime(jam_masuk,'%Y-%m-%d %H:%M:%S.%f') 
                # print(jam_masuk)
                durasi = date  - jam_masuk    
                durasi = self.to_minutes(minutes=durasi) 
        return durasi
    def get_ens(self,obj):
        durasi = 0
        section = obj.trans_ep_section
        if section: 
            beban_masuk = section.first().beban_masuk if section.first() else 0
            ens = section.first().ens  if section.first() else 0
            if not obj.jam_tutup and not obj.jam_normal:
                durasi_minute = self.get_durasi_minute(obj) 
                beban_masuk = self.convert_null(value=beban_masuk) if beban_masuk else 0
                ens = self.convert_null(value=ens) if ens else 0  
                durasi = durasi_minute  * float(beban_masuk) * 1000 + float(ens) 
            elif obj.jam_tutup and not obj.jam_normal: 
                durasi_nyala_bertahap = self.get_durasi_nyala_bertahap(obj) 
                beban_masuk = self.convert_null(value=beban_masuk) if beban_masuk else 0
                ens = self.convert_null(value=ens) if ens else 0 
                durasi = durasi_nyala_bertahap *  float(beban_masuk) * 1000 + float(ens)
            elif obj.jam_tutup and obj.jam_normal:
                durasi = ens  
            else:
                durasi = ens  
        return durasi
    
    def get_durasi_normal(self,obj):
        durasi = None
        if obj.jam_tutup  and obj.jam_normal and obj.jam_buka     :
            if obj.jam_normal   - obj.jam_buka:
                durasi = obj.jam_normal   - obj.jam_buka
                durasi = self.to_minutes(minutes=durasi)  
        elif obj.jam_tutup  and obj.jam_normal and obj.jam_trip  :
            if obj.jam_isolasi  and obj.jam_trip:
                durasi = obj.jam_isolasi  - obj.jam_trip 
                durasi = self.to_minutes(minutes=durasi) 
        else:
            durasi =  None
        return durasi
    def get_durasi_isolasi(self,obj):
        durasi = None
        if obj.jam_isolasi and obj.jam_trip   :
            durasi = obj.jam_isolasi  - obj.jam_trip
            durasi = self.to_minutes(minutes=durasi)
        elif obj.jam_isolasi  and obj.jam_buka :
            durasi = obj.jam_isolasi  - obj.jam_buka 
            durasi = self.to_minutes(minutes=durasi)
        elif not obj.jam_isolasi  and obj.jam_buka:
            durasi = obj.jam_normal  - obj.jam_buka
            durasi = self.to_minutes(minutes=durasi)
        elif not obj.jam_isolasi  and obj.jam_trip:
            # durasi = obj.jam_normal  - obj.jam_trip 
            durasi =  None 
        else:
            durasi =  None
        return durasi 
    def get_durasi_wrc(self,obj):
        durasi = None
        if obj.jam_wrc  and obj.jam_trip   :
            durasi = obj.jam_wrc  - obj.jam_trip
            durasi = self.to_minutes(minutes=durasi)
        elif obj.jam_wrc  and obj.jam_buka   :
            durasi = obj.jam_wrc  - obj.jam_buka 
            durasi = self.to_minutes(minutes=durasi)
        else:
            durasi =  None
        return durasi
    def get_durasi_pengusutan(self,obj):
        durasi = None
        if obj.jam_pengusutan and obj.jam_trip  :
            durasi = obj.jam_pengusutan - obj.jam_trip
            durasi = self.to_minutes(minutes=durasi)
        elif obj.jam_pengusutan and obj.jam_buka   :
            durasi = obj.jam_pengusutan - obj.jam_buka 
            durasi = self.to_minutes(minutes=durasi)
        elif not obj.jam_pengusutan and obj.jam_buka:
            durasi = obj.jam_normal  - obj.jam_buka 
            durasi = self.to_minutes(minutes=durasi)
        elif not obj.jam_pengusutan and obj.jam_trip:
            durasi = obj.jam_normal  - obj.jam_trip
            durasi = self.to_minutes(minutes=durasi)
        else:
            durasi =  None
        return durasi 
    
    def get_durasi_perbaikan(self,obj):
        durasi = None
        if obj.jam_normal and obj.jam_pengusutan and obj.jam_trip  : 
            durasi = ( obj.jam_normal - obj.jam_trip ) - ( obj.jam_pengusutan - obj.jam_trip)
            durasi = self.to_minutes(minutes=durasi)
        elif obj.jam_normal and obj.jam_pengusutan and obj.jam_buka  :
            durasi = (obj.jam_normal - obj.jam_buka ) - ( obj.jam_pengusutan - obj.jam_buka)
            durasi = self.to_minutes(minutes=durasi)
        else:
            durasi =  None
        return durasi
    
    def get_durasi_recovery(self,obj):
        durasi = None
        if obj.jam_normal and obj.jam_trip :
            durasi = obj.jam_normal - obj.jam_trip 
            durasi = self.to_minutes(minutes=durasi) 
        elif obj.jam_normal  and  obj.jam_buka :
            durasi = obj.jam_normal - obj.jam_buka 
            durasi = self.to_minutes(minutes=durasi) 
        else:
            durasi =  None
        return durasi
    def get_status(self,obj):
        status = None
        if not obj.jam_tutup and not obj.jam_normal :
            status = "Padam"
        elif obj.jam_tutup and not obj.jam_normal:
            status = "Nyala Bertahap"
        elif obj.jam_tutup and obj.jam_normal:
            status = "Normal" 
        else:
            status = "-" 
        return status
    def get_total_gangguan_month(self,obj):
        if obj.penyebab == 'TRIP':
            date = self.d_now() 
            return TransEp.objects.filter(id_trans_ep=obj.id_trans_ep,tanggal__month=date.month,tanggal__year=date.year).count()
    def get_total_gangguan_year(self,obj):
        if obj.penyebab == 'TRIP':
            date = self.d_now() 
            return TransEp.objects.filter(id_trans_ep=obj.id_trans_ep,tanggal__year=date.year).count()  


class TransEpHitungENSSerializers(serializers.ModelSerializer):   

    # trans_ep_section = TransEpSectionSerializers(many=False, read_only=True, source='id_trans_ep') 
    trans_ep_section = TransEpSectionSerializers(many=True,read_only=True) 
    durasi_nyala_bertahap = serializers.SerializerMethodField(source='get_durasi_nyala_bertahap',read_only=True)
    ens = serializers.SerializerMethodField(source='get_ens',read_only=True) 
    durasi = serializers.SerializerMethodField(source='get_durasi',read_only=True) 

    class Meta:
        model = TransEp
        fields = ['id_trans_ep','beban_padam','jam_buka','jam_tutup','jam_trip','jam_normal','durasi','durasi_nyala_bertahap','ens','trans_ep_section']   


    def convert_null(self,value=None):
        if value:
            return float(value) if value != None or value != ""  else 0
        return 0

    def d_now(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
        date  = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f')   
        return date

    def to_minutes(self,minutes=None):
        if minutes:
            minutes = minutes.total_seconds() / 60
            return round(minutes,2)
        return 0 
    def to_hour(self,value=None):
        if value:
            menit = value.total_seconds() / 60
            jam =  menit / 60  
            return round(jam,2)
        return 0 

    def convert_datum(self, value=None):
        if value:
            value = value.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
            value = datetime.datetime.strptime(value,'%Y-%m-%d %H:%M:%S.%f') 
            return value
        return None
        
    def get_durasi(self,obj): 
        durasi = 0 
        date = self.d_now()  
        if not obj.jam_buka  and not obj.jam_tutup: 
            if obj.jam_trip:  
                durasi = date  - self.convert_datum(value=obj.jam_trip)
                durasi  = self.to_hour(value=durasi) 
        elif not obj.jam_trip  and obj.jam_tutup :
            if obj.jam_buka:   
                durasi = date  - self.convert_datum(value=obj.jam_buka)
                durasi  = self.to_hour(value=durasi) 
        elif  obj.jam_buka and obj.jam_tutup  :
            durasi = obj.jam_tutup  - obj.jam_buka 
            durasi  = self.to_hour(value=durasi) 
        elif  obj.jam_tutup and obj.jam_trip:
            durasi = obj.jam_tutup   - obj.jam_trip  
            durasi  = self.to_hour(value=durasi) 
            # print(durasi)
        else:
            durasi =  0
        return durasi 
    def get_durasi_nyala_bertahap(self,obj): 

        date = self.d_now()  
        durasi = 0
        if obj.jam_tutup and not obj.jam_normal:
            if obj.trans_ep_section.last():
                section = obj.trans_ep_section.last().jam_masuk  
                # section = obj.trans_ep_section.all()
                # section = GetTransEpSectionSerializers(section, many=True).data 
                # print(section)
                # print(section)
                jam_masuk = section.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
                jam_masuk = datetime.datetime.strptime(jam_masuk,'%Y-%m-%d %H:%M:%S.%f') 
                # print(date,jam_masuk)
                durasi = date  - jam_masuk    
                durasi = self.to_hour(value=durasi)  
        return durasi
    def get_ens(self,obj):  
        durasi = 0
        section = obj.trans_ep_section 
        # exit()
        # hitung ens jika trans_section ada
        if section:   
            durasi = 0
            beban_masuk = obj.trans_ep_section.last().beban_masuk if obj.trans_ep_section.last() else 0
            ens = obj.trans_ep_section.last().ens  if obj.trans_ep_section.last() else 0
            # print(beban_masuk,ens)
            if not obj.jam_tutup and not obj.jam_normal:
                durasi_jam = self.get_durasi_jam(obj) 
                beban_masuk = self.convert_null(value=beban_masuk) if beban_masuk else 0
                ens = self.convert_null(value=ens) if ens else 0  
                # hitung ens
                durasi = durasi_jam  * float(beban_masuk) * 1000 + float(ens)  
                durasi = round(durasi,2) 
            elif obj.jam_tutup and not obj.jam_normal: 
                durasi_nyala_bertahap = self.get_durasi_nyala_bertahap(obj) 
                # print(durasi_nyala_bertahap,beban_masuk,ens)
                beban_masuk = self.convert_null(value=beban_masuk) if beban_masuk else 0
                ens = self.convert_null(value=ens) if ens else 0 
                durasi = durasi_nyala_bertahap *  float(beban_masuk) * 1000 + float(ens) 
                durasi = round(durasi,2)
            elif obj.jam_tutup and obj.jam_normal: 
                durasi_jam = self.get_durasi(obj) 
                beban_masuk = self.convert_null(value=obj.beban_padam) if obj.beban_padam else 0 
                # hitung ens 
                durasi = durasi_jam  * float(beban_masuk) * 1000 
                durasi = round(durasi,2)
                # print(durasi)
            else:
                durasi = 0  
        else:
            # print(section)
            if obj.jam_tutup and obj.jam_normal:
                durasi_jam = self.get_durasi(obj) 
                beban_masuk = self.convert_null(value=obj.beban_padam) if obj.beban_padam else 0 
                # hitung ens
                # print(durasi_jam,beban_masuk)
                durasi = durasi_jam  * float(beban_masuk) * 1000 
        return durasi  
     


class CRTransEpSerializers(serializers.ModelSerializer):  
    id_keypoint = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=True,
        style={'base_template': 'input.html'}
    )
    id_ref_ep_indikasi = serializers.SlugRelatedField(
        queryset=RefEpIndikasi.objects.all(),
        slug_field='id_ref_ep_indikasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_ep_cuaca = serializers.SlugRelatedField(
        queryset=RefEpCuaca.objects.all(),
        slug_field='id_ref_ep_cuaca',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_ep_penyebab_ggn = serializers.SlugRelatedField(
        queryset=RefEpPenyebabGgn.objects.all(),
        slug_field='id_ref_ep_penyebab_ggn',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
     
    id_ulp = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_penyulang_fdir = serializers.SlugRelatedField(
        queryset=RefEpFdir.objects.all(),
        slug_field='id_penyulang_fdir',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    
    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        style={'base_template': 'input.html'}
    ) 
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=False,
        style={'base_template': 'input.html'}
    )  
    tgl_entri = serializers.DateTimeField(read_only=True)
    tgl_update = serializers.DateTimeField(read_only=True)
    
    

    class Meta:
        model = TransEp
        fields = '__all__'


class UDTransEpSerializers(serializers.ModelSerializer):
    queryset = TransEp.objects.all()
    id_keypoint = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_ep_indikasi = serializers.SlugRelatedField(
        queryset=RefEpIndikasi.objects.all(),
        slug_field='id_ref_ep_indikasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_ep_penyebab_ggn = serializers.SlugRelatedField(
        queryset=RefEpPenyebabGgn.objects.all(),
        slug_field='id_ref_ep_penyebab_ggn',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_ref_ep_cuaca = serializers.SlugRelatedField(
        queryset=RefEpCuaca.objects.all(),
        slug_field='id_ref_ep_cuaca',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_up3 = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
     
    id_ulp = serializers.SlugRelatedField(
        queryset=RefLokasi.objects.all(),
        slug_field='id_ref_lokasi',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
    id_penyulang_fdir = serializers.SlugRelatedField(
        queryset=RefEpFdir.objects.all(),
        slug_field='id_penyulang_fdir',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    )
     
    tgl_update = serializers.DateTimeField(read_only=True)
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=True,
        style={'base_template': 'input.html'}
    )  
    class Meta:
        model = TransEp
        fields = '__all__' 


class ReflokasiPeralatanSerializers(serializers.ModelSerializer):  
    ref_jenis_lokasi = RefJenisLokasierializer(read_only=True, source='id_ref_jenis_lokasi')
    gardu_induk = ReflokasiGI(read_only=True, source='id_gardu_induk') 
    penyulang = ReflokasiPenyulang(read_only=True, source='id_penyulang')  
    zone = ReflokasiZone(read_only=True, source='id_zone')  
    section = ReflokasiZone(read_only=True, source='id_section')  
    up3 = ReflokasiUp3(read_only=True, source='id_up3_1') 
    ulp = ReflokasiUp3(read_only=True, source='id_ulp_1') 
    total_gardu_padam  = serializers.SerializerMethodField(source='get_total_gardu_padam', read_only=True)
    
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'alamat','id_ref_jenis_lokasi',
                'ref_jenis_lokasi','id_gardu_induk','id_penyulang','id_up3_1','id_ulp_1','id_section','section',
                'id_zone','gardu_induk','penyulang','zone','up3','ulp','total_gardu_padam','pelanggan_tm','pelanggan_vip'
                ]
    
    def get_total_gardu_padam(self, obj):
        return obj.trans_rekap_padam_keypoint.count()

class PeralatanSerializers(serializers.ModelSerializer):    
    class Meta:
        model = RefLokasi 
        fields = ['id_ref_lokasi','nama_lokasi', 'alamat','id_ref_jenis_lokasi']
    
    
