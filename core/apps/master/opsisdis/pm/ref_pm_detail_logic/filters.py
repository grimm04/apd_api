from rest_framework import filters
from django_filters import rest_framework
from .models import RefPMDetailLogic


class RefPMDetailLogicFilter(rest_framework.FilterSet):

    class Meta:
        model = RefPMDetailLogic
        fields = ['id_ref_pm_detail'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
