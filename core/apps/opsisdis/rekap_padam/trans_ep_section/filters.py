from rest_framework import filters
from django_filters import rest_framework
from .models import TransEpSection


class TransEpSectionFilter(rest_framework.FilterSet):

    class Meta:
        model = TransEpSection
        fields = ['id_trans_ep'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
