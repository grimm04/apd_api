from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/frekuensi/scd-trans-frek-his", views.FrekuensiHISViews, basename='frekuensi.scd-trans-frek-his'
)