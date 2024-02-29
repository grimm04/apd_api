from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/telemetring/trafo-gi-ktt", views.TelemetringTrafoGIKTTViews, basename='telemetring-trafo-gi'
)
router.register(
    r"opsisdis/telemetring/trafo-gi-ktt-total", views.TelemetringGetCountTrafoGIKTTViews, basename='telemetring-trafo-gi-total'
)


router.register(
    r"opsisdis/telemetring/trafo-gi-non-ktt", views.TelemetringTrafoGINonKTTViews, basename='telemetring-trafo-gi-non-ktt'
)
router.register(
    r"opsisdis/telemetring/trafo-gi-non-ktt-total", views.TelemetringGetCountTrafoGINonKTTViews, basename='telemetring-trafo-gi-total-non-ktt'
)