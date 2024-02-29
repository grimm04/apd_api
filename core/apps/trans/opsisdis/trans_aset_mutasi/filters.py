from rest_framework import filters
from django_filters import rest_framework
from .models import TransAsetMutasi


class TransAsetMutasiFilter(rest_framework.FilterSet):

    class Meta:
        model = TransAsetMutasi
        fields = ['id_station','id_bay','id_pelaksana','id_ref_aset_lantai', 'id_ref_kondisi_aset','id_trans_wo','id_ref_aset_ruangan','id_ref_aset_rak','id_jenis_aset_mutasi','id_ref_aset','tgl_mutasi'] 
        
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
