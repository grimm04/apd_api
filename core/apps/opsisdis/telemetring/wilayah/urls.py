from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/wilayah", views.TelemetringWilayahViews, basename='telemetring-wilayah'
)

router.register(
    r"opsisdis/telemetring/wilayah-total", views.TelemetringGetCountPenyulangViews, basename='telemetring-wilayah-total'
)