from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/laporan_scada/histori_peralatan_scd", views.HistoriPeraltanScdView, basename='histori-peralatan-scd'
)
