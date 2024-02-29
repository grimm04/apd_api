from rest_framework import filters
from django_filters import rest_framework
from .models import CPoint


class CharInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass


class CPointFilter(rest_framework.FilterSet):
    path4 = CharInFilter(field_name='path4', lookup_expr='in')

    class Meta:
        model = CPoint
        # fields = ['id_pointtype', 'point_name', 'point_type', 'active', 'aor_id', 'aor_id_dw', 'int',
        #           'tariff_group_id', 'ctrl_area_int_id', 'ctrl_area_ext_id', 'meas_unit', 'state_set_id',
        #           'collection_rate', 'absolute_error', 'significant_digits', 'energy_type',
        #           'import_export', 'counter_type', 'scaling_facktor', 'rollover_limit', 'precision_processing',
        #           'created', 'ddc_trigger_report_flag', 'system_id', 'collection_delay', 'value',
        #           'last_update', 'p1', 'p2', 'p3', 'p4', 'p5', 'element', 'info', 'status_network', 'update_network',
        #           'kinerja', 'id_station', 'point_class', 'send_telegram', 'elementtext', 'capture_telemetring',
        #           'format_pesan', 'durasi_perubahan', 'rc', 'trip', 'rc_telegram', 'trip_telegram',
        #           'status', 'wilayah']
        fields = ['point_number', 'path1', 'path2', 'path3', 'path5', 'id_pointtype', 'point_type',
                  'kinerja', 'capture_telemetring', 'active']


class SearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)
