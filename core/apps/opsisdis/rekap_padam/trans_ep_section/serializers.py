from rest_framework import serializers

from apps.users.models import Users
from library.datetimenTimezone import CustomDateTimeField
from .models import TransEpSection
from apps.opsisdis.rekap_padam.trans_ep.models import TransEp
from apps.master.jaringan.ref_lokasi.models import RefLokasi    
import datetime 
class GetTransSignleEpSerializers(serializers.ModelSerializer): 
    class Meta:
        model = TransEp
        fields = ['id_trans_ep','beban_padam']   
   

class GetTransEpSectionSerializers(serializers.ModelSerializer):     
    jam_masuk = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')  
    # jam_masuk = CustomDateTimeField()
    class Meta:
        model = TransEpSection
        fields = '__all__' 

class GetTransEpSerializers(serializers.ModelSerializer):
    trans_ep_section = GetTransEpSectionSerializers(many=True,read_only=True)  
    durasi = serializers.SerializerMethodField(source='get_durasi_minute',read_only=True) 
    durasi_nyala_bertahap = serializers.SerializerMethodField(source='get_durasi_nyala_bertahap',read_only=True)
    keypoint_name = serializers.SerializerMethodField(source='get_keypoint_name')  
    ens = serializers.SerializerMethodField(source='get_ens',read_only=True)
    class Meta:
        model = TransEp
        fields = ['id_trans_ep','beban_padam','keypoint_name','jam_padam','jam_buka','jam_tutup','jam_trip','jam_normal','durasi','durasi_nyala_bertahap','ens','trans_ep_section','keypoint_name','id_keypoint']   
    def get_keypoint_name(self,obj):
        return obj.id_keypoint.nama_lokasi
    
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

class TransEpSectionSerializers(serializers.ModelSerializer):   
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 
    # gardu_induk = IDSRef_LokasiSerializer(read_only=True, source='id_gardu')   

    class Meta:
        model = TransEpSection
        fields = '__all__'

class CRTransEpSectionSerializers(serializers.ModelSerializer):    
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=True,
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
    class Meta:
        model = TransEpSection
        fields = '__all__' 

class UDTransEpSectionSerializers(serializers.ModelSerializer):
    queryset = TransEpSection.objects.all()
 
    id_trans_ep = serializers.SlugRelatedField(
        queryset=TransEp.objects.all(),
        slug_field='id_trans_ep',
        allow_null=True,
        required=False,
        style={'base_template': 'input.html'}
    ) 

    id_user_entri = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True,
        required=False, 
        style={'base_template': 'input.html'}
    ) 
    
    id_user_update = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='id_user',
        allow_null=True, 
        required=True,
        style={'base_template': 'input.html'}
    )  

    class Meta:
        model = TransEpSection
        fields = '__all__'

 