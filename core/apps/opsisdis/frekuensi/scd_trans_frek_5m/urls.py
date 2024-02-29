from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/frekuensi/scd-trans-frek-5m", views.Frekuensi5MViews, basename='frekuensi.scd-trans-frek-5m'
)