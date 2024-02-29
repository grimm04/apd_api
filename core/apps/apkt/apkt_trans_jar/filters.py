from rest_framework import filters
from django_filters import rest_framework
from .models import APKTTransJAR

class APKTTransJARFilter(rest_framework.FilterSet):

    tgl_padam = rest_framework.DateFromToRangeFilter(field_name='tgl_padam', label='tgl_padam example: (2022-05-11)')

    class Meta:
        model = APKTTransJAR
        fields = ['nama_laporan', 'status_laporan', 'tgl_padam']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)