from rest_framework import filters
from django_filters import rest_framework
from .models import RefAsetDoc
 

class RefAsetDocFilter(rest_framework.FilterSet):

    class Meta:
        model = RefAsetDoc
        fields = ['status', 'tipe', 'jenis', 'id_user_entri',
                  'id_user_update', 'id_ref_aset']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
