from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/zona", views.TelemetringZonaViews, basename='telemetring-zona'
)
router.register(
    r"opsisdis/telemetring/zona-total", views.TelemetringGetCountZonaViews, basename='telemetring-zona-total'
)