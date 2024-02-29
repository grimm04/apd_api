from rest_framework import filters
from django_filters import rest_framework
from .models import ExtUserToken


class ExtUserTokenFilter(rest_framework.FilterSet):

    class Meta:
        model = ExtUserToken
        fields = ['id_user']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
