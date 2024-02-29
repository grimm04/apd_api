from rest_framework import filters
from django_filters import rest_framework
from apps.master.jaringan.ref_lokasi.models import RefLokasi 
from django.db.models import Q
from apps.additional.serializers import NumberInFilter

class PenyulangUFRFilter(rest_framework.FilterSet): 
    ufr_isempty = rest_framework.BooleanFilter(field_name='ufr', lookup_expr='isnull')
    id_gardu_induk = NumberInFilter(method='filter_gardu_induk', lookup_expr='in')

    ufr = rest_framework.CharFilter(method="filter_ufr", label="1,2,3,4")
    class Meta:
        model = RefLokasi
        fields = ['ufr','id_ref_lokasi']
    
    def filter_ufr(self, queryset, name, value):
        query = Q()
        for ufr in value.split(","):
            query |= Q(ufr__contains=ufr)
        return queryset.filter(query)

    def filter_gardu_induk(self, queryset, name, value):  
        return queryset.filter(id_parent_lokasi__id_parent_lokasi__in=value)

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)