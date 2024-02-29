from rest_framework import filters
from django_filters import rest_framework
from .models import RefAsetManufaktur


class RefAsetManufakturFilter(rest_framework.FilterSet):

    class Meta:
        model = RefAsetManufaktur
        fields = ['status','id_user_entri', 'id_user_update'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
