 
from rest_framework import filters
import django_filters 
from .models import TransTmSubsistem  
 

class LaporanTransTmSubsistemFilter(django_filters.FilterSet):
    datum = django_filters.DateTimeFromToRangeFilter(field_name='datum', label="yyy-mm-dd hh:mm:ss")  
    # jenis_layanan = django_filters.CharFilter(field_name='jenis_layanan', method='filter_jenis_layanan', label='KTT, NON KTT') 
    i_gte = django_filters.CharFilter(field_name='i', lookup_expr='gte' ,label="Ampere >=")
    i_lte = django_filters.CharFilter(field_name='i', lookup_expr='lte', label="Ampere <=")
    i_exact = django_filters.CharFilter(field_name='i', lookup_expr='exact', label="Ampere =")
    p_gte = django_filters.CharFilter(field_name='p', lookup_expr='gte' ,label="MW >=")
    p_lte = django_filters.CharFilter(field_name='p', lookup_expr='lte', label="MW <=")
    p_exact = django_filters.CharFilter(field_name='p', lookup_expr='exact', label="MW =")
    class Meta:
        model = TransTmSubsistem
        fields = ['datum','id_lokasi','id_parent_lokasi','id_ref_lokasi_subsistem']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
