from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/frekuensi/scd-frek-rtl", views.FrekuensiRTLViews, basename='frekuensi.scd-frek-rtl'
)