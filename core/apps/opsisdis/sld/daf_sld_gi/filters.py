from rest_framework import filters
from django_filters import rest_framework
from .models import DAF_SLD_GI
 

class DAF_SLD_GIFilter(rest_framework.FilterSet):
    TCHOICE = (
        ('SLD', 'SLD'),
        ('SPD','SPD')
    )

    kelompok = rest_framework.ChoiceFilter(field_name='kelompok',choices=TCHOICE, method='filter_kelompok',label='Kelompk SLD,SPD')

    def filter_kelompok(self, queryset, name, value):  
        return queryset.filter(kelompok__exact=value)
    class Meta:
        model = DAF_SLD_GI
        fields = ['id_gardu_induk','kelompok']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
