from rest_framework import filters
from django_filters import rest_framework
from .models import WP_QRC
 

class WP_QRCFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_QRC
        fields = ['nama_user','nama_pekerjaan','vendor','key_qrc']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
