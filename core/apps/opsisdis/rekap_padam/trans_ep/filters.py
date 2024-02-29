from rest_framework import filters
from django_filters import rest_framework
from .models import TransEp
from apps.master.jaringan.ref_lokasi.models import RefLokasi   


class TransEpFilter(rest_framework.FilterSet):  
    tanggal = rest_framework.DateFromToRangeFilter(field_name='tanggal', label="yyy-mm-dd") 
    status = rest_framework.CharFilter(field_name='status', method='filter_status',label='STATUS (Normal, Padam, Nyala Bertahap)') 
    
    class Meta:
        model = TransEp
        fields = ['id_up3','id_ulp','tanggal','posting','id_keypoint','jenis_keypoint','jenis_padam','penyebab','id_ref_ep_indikasi','id_ref_ep_penyebab_ggn','id_ref_ep_cuaca']
    
    def filter_status(self, queryset, name, value):  
        if value == "Padam":
            return queryset.filter(jam_tutup__isnull=True,jam_normal__isnull=True) 
        elif value == "Nyala Bertahap":
            return queryset.filter(jam_tutup__isnull=False,jam_normal__isnull=True) 
        else:
            return queryset.filter(jam_tutup__isnull=False,jam_normal__isnull=False)   

class PeralatanFilter(rest_framework.FilterSet):   
    class Meta:
        model = RefLokasi
        fields = ['id_ref_jenis_lokasi'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
