from rest_framework import filters
from django_filters import rest_framework
from .models import RefPM


class RefPMFilter(rest_framework.FilterSet):

    class Meta:
        model = RefPM
        fields = ['id_ref_aset_jenis','status','id_user_entri', 'id_user_update'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
