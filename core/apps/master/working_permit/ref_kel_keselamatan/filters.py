from rest_framework import filters
from django_filters import rest_framework
from .models import RefKelKeselamatan 
 

class RefKelKeselamatanFilter(rest_framework.FilterSet):

    kategori = rest_framework.CharFilter(field_name='kategori', label='pelindung, perlengkapan')


    class Meta:
        model = RefKelKeselamatan
        fields = ['name', 'alias','kategori']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
