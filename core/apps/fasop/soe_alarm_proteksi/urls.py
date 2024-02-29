from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/laporan_scada/soe_alarm_proteksi", views.SoeAlarmProteksiView, basename='soe-alarm-proteksi'
)

router.register(
    r"fasop/laporan_scada/get_pathtext", views.PathView, basename='path-text'
)


