from rest_framework import filters
from django_filters import rest_framework
from .models import RefAset


class RefAsetFilter(rest_framework.FilterSet):

    class Meta:
        model = RefAset
        fields = ['id_ref_aset_parent','id_ref_aset_status', 'id_ref_aset_jenis','id_ref_aset_manufaktur','id_ref_aset_level','id_aset_mutasi','id_trans_pm',
            'id_ref_lokasi_1','id_ref_lokasi_2','id_ref_lokasi_3'
        ] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
