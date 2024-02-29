from rest_framework import filters
from django_filters import rest_framework
from .models import ExtUserTokenRole


class ExtUserTokenRoleFilter(rest_framework.FilterSet):

    class Meta:
        model = ExtUserTokenRole
        fields = ['id_token', 'id_module']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
