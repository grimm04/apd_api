from numpy import source
from rest_framework import filters
from django_filters import rest_framework
from .models import TransTmTrafoGiBulan


class TransTmTrafoGiBulanFilter(rest_framework.FilterSet): 
    # datum = rest_framework.DateTimeFromToRangeFilter(field_name='datum')  
    month = rest_framework.DateTimeFromToRangeFilter(field_name='datum',label='(yyyy-mm-dd)') 
    # datum_month = rest_framework.NumberFilter(field_name='datum', lookup_expr='month') 
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
    class Meta:
        model = TransTmTrafoGiBulan
        fields = ['id_ref_lokasi_gi', 'id_ref_lokasi_trafo_gi', 'datum']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
