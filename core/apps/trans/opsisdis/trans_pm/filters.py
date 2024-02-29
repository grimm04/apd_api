from rest_framework import filters
from django_filters import rest_framework
from .models import TransPM


class TransPMFilter(rest_framework.FilterSet):

    class Meta:
        model = TransPM
        fields = ['id_ref_pm','id_trans_wo','id_ref_hi','id_ref_aset', 'id_trans_aset_mutasi','id_user_entri','status','level_pm','kesimpulan'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
