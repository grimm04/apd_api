from email.policy import default
from rest_framework import filters
from django_filters import rest_framework
from .models import WP_ONLINE
from apps.additional.serializers import NumberInFilter

class WP_ONLINEFilter(rest_framework.FilterSet):
    # TCHOICE = (
    #     (0, 'TIDAK'),
    #     (1,'YA')
    # )
    status_persetujuan = NumberInFilter(field_name='status_persetujuan', lookup_expr='in')
 
    # manuver = rest_framework.ChoiceFilter(choices=TCHOICE)
    # grounding = rest_framework.ChoiceFilter(choices=TCHOICE)

    tgl_pekerjaan = rest_framework.DateTimeFromToRangeFilter(field_name='tgl_pekerjaan',label='tgl_pekerjaan(24hour) example: (2022-05-11 13:00)') 
    tgl_pekerjaan_selesai = rest_framework.DateTimeFromToRangeFilter(field_name='tgl_pekerjaan',label='tgl_pekerjaan(24hour) example: (2022-05-11 13:00)') 
    # tgl_pekerjaan = rest_framework.DateTimeFilter(field_name='tgl_pekerjaan',label='tgl_pekerjaan(24hour) example: (2022-01-01 00:00:00)')   
    # tgl_pekerjaan_selesai = rest_framework.DateTimeFilter(field_name='tgl_pekerjaan_selesai',label='tgl_pekerjaan_selesai(24hour) example: (2022-01-01 00:00:00)') 
    tgl_persetujuan = rest_framework.DateTimeFilter(field_name='tgl_persetujuan',label='tgl_persetujuan(24hour) example: (2022-01-01 00:00:00)')  

    # nama_pengawas = rest_framework.CharFilter(field_name='nama_pengawas', method='filter_nama_pengawas' , label='id_pengawas')
    # nama_pengawask3 = rest_framework.CharFilter(field_name='nama_pengawask3', method='filter_nama_pengawask3' , label='id_pengawas')
    nama_bagian = rest_framework.CharFilter(field_name='bagian', method='filter_bagian',label='id_wp_master_bagian') 
    nama_vendor = rest_framework.CharFilter(field_name='vendor', method='filter_vendor',label='id_wp_master_vendor') 

    # def filter_nama_pengawas(self, queryset, name, value):  
    #     return queryset.filter(id_pengawas__fullname__contains=value)

    # def filter_nama_pengawask3(self, queryset, name, value):  
    #     return queryset.filter(id_pengawask3__fullname__contains=value)

    def filter_bagian(self, queryset, name, value):  
        return queryset.filter(id_wp_master_bagian__name__contains=value)

    def filter_filter_vendor(self, queryset, name, value):  
        return queryset.filter(vendor_pelaksana__nama__contains=value)
 
    class Meta:
        model = WP_ONLINE
        fields = ['nomor_formulir','jenis_pekerjaan','nomor_sop','pekerjaan_dilakukan','lokasi_pekerjaan','id_wp_master_bagian','id_user_direksi',
        'nama_pengawas','nama_pengawask3','vendor_pelaksana','nama_koordinator_vendor','tgl_pekerjaan','petugas_zona1','petugas_zona2','petugas_zona3',
        'manuver','grounding','status_persetujuan','id_user_entri','id_user_persetujuan','tgl_pekerjaan_selesai','tgl_persetujuan']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
