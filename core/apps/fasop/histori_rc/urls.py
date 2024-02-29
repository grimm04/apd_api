from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/laporan_scada/histori_rc", views.SoeAlarmProteksiView, basename='soe-alarm-proteksi'
)
