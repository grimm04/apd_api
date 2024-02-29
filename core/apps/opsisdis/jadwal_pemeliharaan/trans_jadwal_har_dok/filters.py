from rest_framework import filters
from django_filters import rest_framework
from .models import TransJadwalHarDok


class TransJadwalHarDokFilter(rest_framework.FilterSet):

    class Meta:
        model = TransJadwalHarDok
        fields = ['id_trans_jadwal_har'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
