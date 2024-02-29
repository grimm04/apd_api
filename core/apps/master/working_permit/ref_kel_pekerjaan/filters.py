from rest_framework import filters
from django_filters import rest_framework
from .models import RefKelPekerjaan  
 

class RefKelPekerjaanFilter(rest_framework.FilterSet):
    kategori = rest_framework.CharFilter(field_name='kategori', label='klasifikasi, prosedur, lampiran')

    class Meta:
        model = RefKelPekerjaan
        fields = ['name', 'alias']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
