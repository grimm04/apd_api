from rest_framework import filters
from django_filters import rest_framework
from .models import FrekuensiTH
from datetime import datetime

class FrekuensiTHFilter(rest_framework.FilterSet):

    datum = rest_framework.DateTimeFilter(field_name='datum', label='datum example: 2022-05-11', method='filter_datum')

    def filter_datum(self, queryset, name, value):
        value = value.strftime('%Y-%m-%d')
        return queryset.filter(datum__date=value)
    
    frek_nama = rest_framework.CharFilter(field_name='frek_nama', method='filter_frek_nama', label='from id_meter') 

    def filter_frek_nama(self, queryset, name, value):  
        return queryset.filter(id_meter__nama__contains=value)

    frek_lokasi = rest_framework.CharFilter(field_name='frek_lokasi', method='filter_frek_lokasi', label='from id_meter') 

    def filter_frek_lokasi(self, queryset, name, value):  
        return queryset.filter(id_meter__lokasi__contains=value)

    class Meta:
        model = FrekuensiTH
        fields = ['id_meter', 'datum', 'range_nilai']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)