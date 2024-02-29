from rest_framework import filters
from django_filters import rest_framework
from .models import TransEpLaporan


class TransEpLaporanFilter(rest_framework.FilterSet):

    class Meta:
        model = TransEpLaporan
        fields = ['id_trans_ep','status_s','status_g','tegangan'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
