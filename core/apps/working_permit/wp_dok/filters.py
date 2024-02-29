from rest_framework import filters
from django_filters import rest_framework
from .models import WP_DOK
 

class WP_DOKFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_DOK
        fields = ['id_wp_online']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
