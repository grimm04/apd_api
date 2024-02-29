from rest_framework import filters
from django_filters import rest_framework
from apps.users.models import Users
from django.core.validators import EMPTY_VALUES

class MyCharFilter(rest_framework.CharFilter):
    empty_value = 'EMPTY'

    def filter(self, qs, value):
        print(self.field_name,self.lookup_expr)
        if value != self.empty_value:
            return super().filter(qs, value)

        qs = self.get_method(qs)(**{'%s__%s' % (self.field_name, self.lookup_expr): ""})
        return qs.distinct() if self.distinct else qs

class EmptyStringFilter(rest_framework.BooleanFilter):
        def filter(self, qs, value):
            if value in EMPTY_VALUES:
                return qs

            exclude = self.exclude ^ (value is False)
            method = qs.exclude if exclude else qs.filter

            return method(**{self.field_name: ""})

class UserFilter(rest_framework.FilterSet):
    # username = rest_framework.NumberFilter(default=False)
    id_ref_regu_petugas_isempty = rest_framework.BooleanFilter(field_name='id_ref_regu_petugas', lookup_expr='isnull')
    # id_ref_regu_petugas_exist = MyCharFilter(field_name='id_ref_regu_petugas',lookup_expr='isnull')
    # idd_ref_regu_petugas__isempty = EmptyStringFilter(field_name='id_ref_regu_petugas')
    class Meta:
        model = Users 
        fields = ['username', 'email', 'is_active', 'fullname', 'akses_login', 'id_perusahaan', 'id_jabatan',
                  'id_departemen','id_ref_regu_petugas']
        # example exact, iexact, contains, isnull, .. https://docs.djangoproject.com/en/4.0/topics/db/queries/
        # exact
        # iexact
        # contains
        # icontains
        # in
        # gt
        # gte
        # lt
        # lte
        # startswith
        # istartswith
        # endswith
        # iendswith
        # range

        # date
        # year
        # iso_year
        # month
        # day
        # week
        # week_day
        # iso_week_day
        # quarter
        # time
        # hour
        # minute
        # second

        # isnull
        # regex
        # iregex
        # https://github.com/carltongibson/django-filter/blob/main/docs/guide/usage.txt
        # fields = {
        #         'name': ['exact'],
        #         'release_date': ['isnull'],
        #     }
        #     filter_overrides = {
        #         models.CharField: {
        #             'filter_class': django_filters.CharFilter,
        #             'extra': lambda f: {
        #                 'lookup_expr': 'icontains',
        #             },
        #         },
        #         models.BooleanField: {
        #             'filter_class': django_filters.BooleanFilter,
        #             'extra': lambda f: {
        #                 'widget': forms.CheckboxInput,
        #             },
        #         },
        #     }


class SearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
