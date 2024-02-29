from rest_framework import filters
from django_filters import rest_framework
from .models import RefAsetExtAtr
 

class RefAsetExtAtrFilter(rest_framework.FilterSet):

    class Meta:
        model = RefAsetExtAtr
        fields = ['status', 'nilai','id_ref_aset','id_ref_aset_ex_atr']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
