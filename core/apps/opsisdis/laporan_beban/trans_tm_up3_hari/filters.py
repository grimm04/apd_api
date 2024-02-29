from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import TransTmUp3Hari 


class TransTmUp3HariFilter(rest_framework.FilterSet):
    # datum = rest_framework.DateTimeFromToRangeFilter(field_name='datum')  
    day = rest_framework.DateTimeFromToRangeFilter(field_name='datum',label='(yyyy-mm-dd)')  
    
    # def filter_datum_date(self, queryset, name, value):  
    #     start_date = date_converter_dt(date=value,time='00:00:00')
    #     end_date = date_converter_dt(date=value,time='23:59:00')  
    #     return queryset.filter(datum__range=(start_date,end_date)) 
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
    class Meta:
        model = TransTmUp3Hari
        fields = ['id_ref_lokasi_up3','datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
