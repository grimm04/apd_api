from rest_framework import filters
from django_filters import rest_framework
from .models import APKTTransLog

class APKTTransLogFilter(rest_framework.FilterSet):

    tgl_mulai = rest_framework.DateTimeFromToRangeFilter(field_name='tgl_mulai', label='tgl_mulai example: (2022-05-11)')
    tgl_selesai = rest_framework.DateTimeFromToRangeFilter(field_name='tgl_selesai', label='tgl_selesai example: (2022-05-11)')

    class Meta:
        model = APKTTransLog
        fields = ['id_apkt_trans_log', 'tgl_mulai', 'tgl_selesai']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)