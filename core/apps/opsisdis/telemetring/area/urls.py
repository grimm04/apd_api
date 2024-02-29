from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/area", views.TelemetringAreaViews, basename='telemetring-area'
)
router.register(
    r"opsisdis/telemetring/area-total", views.TelemetringGetCountAreaViews, basename='telemetring-area-total'
)