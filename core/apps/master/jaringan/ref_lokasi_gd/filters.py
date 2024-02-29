from rest_framework import filters
import django_filters
from .models import RefLokasiGD
from apps.master.jaringan.ref_lokasi.models import RefLokasi

# def ourBranches(request):
#     if request is None:
#         return RefLokasi.objects.none()

#     id_parent_lokasi = request.GET.get('id_parent_lokasi')
#     return RefLokasi.objects.filter(id_parent_lokasi=id_parent_lokasi)

class RefLokasiGDFilter(django_filters.rest_framework.FilterSet):
    # id_parent_lokasi = django_filters.ModelChoiceFilter(queryset=ourBranches, empty_label=("All Ref Lokasi"))
    class Meta:
        model = RefLokasiGD
        fields = ('id_ref_lokasi','id_ref_lokasi_child')

 
class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
