from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/laporan_scada/gangguan_peralatan_scada", views.RealtimeScadaView, basename='realtime-scada'
)


