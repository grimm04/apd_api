from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/penyulang", views.TelemetringPenyulangViews, basename='telemetring-penyulang'
)
router.register(
    r"opsisdis/telemetring/penyulang-total", views.TelemetringGetCountPenyulangViews, basename='telemetring-penyulang-total'
)