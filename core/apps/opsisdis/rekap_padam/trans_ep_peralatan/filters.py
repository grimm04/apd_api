from rest_framework import filters
from django_filters import rest_framework
from .models import TransEpPeralatan


class TransEpPeralatanFilter(rest_framework.FilterSet):
    tanggal = rest_framework.DateFromToRangeFilter(field_name='tgl', label="yyy-mm-dd") 
    status = rest_framework.CharFilter(field_name='status', method='filter_status',label='STATUS (Normal, Padam, Nyala Bertahap)') 

    class Meta:
        model = TransEpPeralatan
        fields = ['id_trans_ep','status_rc_close', 'status_rc_open'] 
    
    def filter_status(self, queryset, name, value):  
        if value == "Padam":
            return queryset.filter(id_trans_ep__jam_tutup__isnull=True,id_trans_ep__jam_normal__isnull=True) 
        elif value == "Nyala Bertahap":
            return queryset.filter(id_trans_ep__jam_tutup__isnull=False,id_trans_ep__jam_normal__isnull=True) 
        else:
            return queryset.filter(id_trans_ep__jam_tutup__isnull=False,id_trans_ep__jam_normal__isnull=False)   
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
