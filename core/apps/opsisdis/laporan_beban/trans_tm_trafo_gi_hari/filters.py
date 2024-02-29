from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import TransTmTrafoGiHari

from library.date_converter import date_converter_dt

class TransTmTrafoGiHariFilter(rest_framework.FilterSet):
    day = rest_framework.DateTimeFromToRangeFilter(field_name='datum', label='(yyyy-mm-dd)') 
    # datum_1 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_1',label='datum_1(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    # datum_2 = rest_framework.DateTimeFromToRangeFilter(field_name='datum_2',label='datum_2(24hour) example: (2022-05-11 13:00) bisa milisecond') 
    # id_pointtype = rest_framework.NumberFilter(field_name='id_pointtype', method='filter_id_pointtype')  
    jenis_layanan = rest_framework.CharFilter(field_name='jenis_layanan', method='filter_jenis_layanan', label='KTT, NON KTT')
    i_max_siang_gte = rest_framework.CharFilter(field_name='i_max_siang', lookup_expr='gte' ,label="Ampere >=")
    i_max_siang_lte = rest_framework.CharFilter(field_name='i_max_siang', lookup_expr='lte', label="Ampere <=")
    i_max_siang_exact = rest_framework.CharFilter(field_name='i_max_siang', lookup_expr='exact', label="Ampere =")
    p_max_siang_gte = rest_framework.CharFilter(field_name='p_max_siang', lookup_expr='gte' ,label="MW >=")
    p_max_siang_lte = rest_framework.CharFilter(field_name='p_max_siang', lookup_expr='lte', label="MW <=")
    p_max_siang_exact = rest_framework.CharFilter(field_name='p_max_siang', lookup_expr='exact', label="MW =")
    i_max_malam_gte = rest_framework.CharFilter(field_name='i_max_malam', lookup_expr='gte' ,label="Ampere >=")
    i_max_malam_lte = rest_framework.CharFilter(field_name='i_max_malam', lookup_expr='lte', label="Ampere <=")
    i_max_malam_exact = rest_framework.CharFilter(field_name='i_max_malam', lookup_expr='exact', label="Ampere =")
    p_max_malam_gte = rest_framework.CharFilter(field_name='p_max_malam', lookup_expr='gte' ,label="MW >=")
    p_max_malam_lte = rest_framework.CharFilter(field_name='p_max_malam', lookup_expr='lte', label="MW <=")
    p_max_malam_exact = rest_framework.CharFilter(field_name='p_max_malam', lookup_expr='exact', label="MW =")
    def filter_jenis_layanan(self, queryset, name, value):  
        return queryset.filter(id_ref_lokasi_trafo_gi__jenis_layanan__exact=value)
    
    # def filter_id_pointtype(self, queryset, name, value):  
    #     return queryset.filter(point_number__id_pointtype=value)
    # datum_date = rest_framework.DateFilter(field_name='datum_date', method='filter_datum_date', label='datum example: (2022-05-11)') 
    
    def filter_datum_date(self, queryset, name, value):  
        start_date = date_converter_dt(date=value,time='00:00:00')
        end_date = date_converter_dt(date=value,time='23:59:00')  
        return queryset.filter(datum__range=(start_date,end_date)) 
    class Meta:
        model = TransTmTrafoGiHari
        fields = ['id_ref_lokasi_gi', 'id_ref_lokasi_trafo_gi','datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
