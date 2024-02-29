 
from rest_framework import filters
import django_filters 
from apps.opsisdis.telemetring.trafo_gi_non_ktt.models import TelemetringTrafoGI   
from library.date_converter import date_converter_dt 

class LaporanTrafoGIFilter(django_filters.FilterSet):
    datum = django_filters.DateTimeFromToRangeFilter(field_name='datum',label="yyy-mm-dd hh:mm:ss") 
    # datum_1 = django_filters.DateTimeFromToRangeFilter(field_name='datum_1',label='datum_1(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    # datum_2 = django_filters.DateTimeFromToRangeFilter(field_name='datum_2',label='datum_2(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    # id_pointtype = django_filters.NumberFilter(field_name='id_pointtype', method='filter_id_pointtype')  
    jenis_layanan = django_filters.CharFilter(field_name='jenis_layanan', method='filter_jenis_layanan', label='KTT, NON KTT')
    id_ref_lokasi_gi  = django_filters.NumberFilter(field_name='id_parent_lokasi')  
    id_ref_lokasi_trafo_gi  = django_filters.NumberFilter(field_name='id_lokasi')  
    i_gte = django_filters.CharFilter(field_name='i', lookup_expr='gte' ,label="Ampere >=")
    i_lte = django_filters.CharFilter(field_name='i', lookup_expr='lte', label="Ampere <=")
    i_exact = django_filters.CharFilter(field_name='i', lookup_expr='exact', label="Ampere =")
    p_gte = django_filters.CharFilter(field_name='p', lookup_expr='gte' ,label="MW >=")
    p_lte = django_filters.CharFilter(field_name='p', lookup_expr='lte', label="MW <=")
    p_exact = django_filters.CharFilter(field_name='p', lookup_expr='exact', label="MW =")
    def filter_jenis_layanan(self, queryset, name, value):  
        return queryset.filter(id_lokasi__jenis_layanan__exact=value) 
    class Meta:
        model = TelemetringTrafoGI
        fields = ['datum','id_lokasi','id_parent_lokasi']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
