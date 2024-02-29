from rest_framework import filters
from django_filters import rest_framework
from .models import WP_HIRARC_DETAIL
 

class WP_HIRARC_DETAILFilter(rest_framework.FilterSet):

    class Meta:
        model = WP_HIRARC_DETAIL
        fields = ['id_wp_hirarc','kegiatan','bahaya','resiko_bahaya','peluang','akibat','tingkat_resiko','pengendalian','penanggung_jawab',
        'peluang2','akibat2','tingkat_resiko2','status_pengendalian']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
