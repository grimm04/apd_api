from rest_framework import filters
from django_filters import rest_framework
from .models import TransJadwalHar
from apps.additional.serializers import CharInFilter

class TransJadwalHarFilter(rest_framework.FilterSet):  
    tgl = rest_framework.DateFromToRangeFilter(field_name='tgl', label="yyy-mm-dd hh:mm") 
    status_pekerjaan = CharInFilter(field_name='status_pekerjaan', lookup_expr='in')
    
    class Meta:
        model = TransJadwalHar
        fields = ['id_ref_jenis_pekerjaan','id_gardu_induk','id_penyulang', 'id_gardu','id_up3','approval_area1','approval_apd1','tgl','butuh_padam','wilayah_padam','id_pelaksana','id_pengawas','jenis_pelayanan'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
