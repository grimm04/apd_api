from rest_framework import filters
from django_filters import rest_framework
from .models import FASOPPATH1

class FASOPPATH1Filter(rest_framework.FilterSet):

    class Meta:
        model = FASOPPATH1
        fields = ['path1']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
