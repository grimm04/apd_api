from rest_framework import filters
from django_filters import rest_framework
from .models import TransWo


class TransWoFilter(rest_framework.FilterSet):

    class Meta:
        model = TransWo
        fields = ['id_pelaksana','id_station','id_ref_wo_jenis','id_user_entri', 'id_user_update'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
