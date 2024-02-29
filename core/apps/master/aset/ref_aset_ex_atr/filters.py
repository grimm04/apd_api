from rest_framework import filters
from django_filters import rest_framework
from .models import RefAsetExAtr
 

class RefAsetExAtrFilter(rest_framework.FilterSet):

    class Meta:
        model = RefAsetExAtr
        fields = ['status', 'nama','satuan','id_ref_aset_jenis','id_user_entri','id_user_update']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
