from rest_framework import filters
from django_filters import rest_framework
from .models import USER_HIS_PASSWORD

class USER_HIS_PASSWORDFilter(rest_framework.FilterSet):

    class Meta:
        model = USER_HIS_PASSWORD
        fields = ['id_user']

class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
