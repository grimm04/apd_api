from email.policy import default
from rest_framework import filters
from django_filters import rest_framework
from .models import RefLokasi, RefLokasiTemp


class NumberInFilter(rest_framework.BaseInFilter, rest_framework.NumberFilter):
    pass


class RefLokasiFilter(rest_framework.FilterSet):
    id_ref_jenis_lokasi_in = NumberInFilter(field_name='id_ref_jenis_lokasi', lookup_expr='in')

    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_ref_jenis_lokasi','id_ref_jenis_pembangkit', 'id_user_entri', 'id_ref_jenis_lokasi_in',
                  'id_user_update',
                  'tree_jaringan', 'coverage', 'kva', 'phase', 'status_listrik', 'no_tiang', 'status_listrik',
                  'jenis_jaringan', 'status_penyulang', 'id_uid', 'id_up3_1', 'id_up3_2',  'id_ulp_1','id_ulp_2', 'id_penyulang','id_up2b',
                  'id_zone', 'id_section', 'id_segment', 'id_unit_pembangkit', 'id_pembangkit', 'id_gardu_induk',
                  'id_trafo_gi', 'id_gardu_distribusi', 'id_trafo_gd','id_gardu_hubung','no_urut','id_ref_province','id_ref_regency','id_ref_district','jenis_gi','jenis_layanan','status_trafo','ufr']


# Filter Unit Pembangkit
class UnitPembangkitFilter(rest_framework.FilterSet):
    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_user_entri', 'id_uid', 'id_up3_1', 'id_up3_2',  'id_ulp_1','id_ulp_2', 'id_penyulang',
                  'id_zone', 'id_section', 'id_segment', 'status_listrik']


# Filter  Pembangkit
class PembangkitFilter(rest_framework.FilterSet):
    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_user_entri', 'id_uid', 'id_up3_1', 'id_up3_2',  'id_ulp_1','id_ulp_2', 'id_penyulang',
                  'id_zone', 'id_section', 'id_segment', 'status_listrik']


# Filter  Pembangkit
class GIFilter(rest_framework.FilterSet):
    class Meta:
        model = RefLokasi
        fields = ['id_parent_lokasi', 'id_user_entri', 'id_uid', 'id_up3_1', 'id_up3_2',  'id_ulp_1','id_ulp_2', 'status_listrik']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)


class RefLokasiFilterTemp(rest_framework.FilterSet):
    class Meta:
        model = RefLokasiTemp
        fields = ['id_ref_jenis_lokasi', 'id_user_entri']
