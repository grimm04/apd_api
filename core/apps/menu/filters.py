from rest_framework import filters
from django_filters import rest_framework
from .models import Menu


class MenuFilter(rest_framework.FilterSet):

    class Meta:
        model = Menu
        fields = ['idParent', 'hidden', 'search', 'divider']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
