from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/pembangkit", views.TelemetringPembangkitViews, basename='telemetring-pembangkit'
)
router.register(
    r"opsisdis/telemetring/pembangkit-total", views.TelemetringGetCountPembangkitViews, basename='telemetring-pembangkit-total'
)