from rest_framework import filters
from django_filters import rest_framework
from .models import TransJadwalHarGardu


class TransJadwalHarGarduFilter(rest_framework.FilterSet):
    # tgl = rest_framework.DateFromToRangeFilter()
    class Meta:
        model = TransJadwalHarGardu
        fields = ['id_gardu','id_trans_jadwal_har'] 
        
class SearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
