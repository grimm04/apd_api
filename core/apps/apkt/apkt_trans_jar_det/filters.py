from rest_framework import filters
from django_filters import rest_framework
from .models import APKTTransJARDet

class APKTTransJARDetFilter(rest_framework.FilterSet):

    tgl_padam = rest_framework.DateFromToRangeFilter(field_name='tgl_padam', label='tgl_padam example: (2022-05-11)')
    tgl_nyala = rest_framework.DateFromToRangeFilter(field_name='tgl_nyala', label='tgl_padam example: (2022-05-11)')

    class Meta:
        model = APKTTransJARDet
        fields = ['id_apkt_trans_jar', 'tgl_padam', 'tgl_nyala']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)