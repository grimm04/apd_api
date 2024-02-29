from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/amr-energi", views.TelemetringAMREnergiViews, basename='telemetring-amr-energi'
)