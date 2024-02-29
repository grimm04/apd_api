from rest_framework import filters
from django_filters import rest_framework
from .models import TransPMDetail


class TransPMDetailFilter(rest_framework.FilterSet):

    class Meta:
        model = TransPMDetail
        fields = ['id_trans_pm','id_ref_pm','id_induk_ref_pm_detail','induk', 'id_user_entri','satuan'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
