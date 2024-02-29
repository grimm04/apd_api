from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/opsisdis/jenis-penyebab-gangguan", views.JenisPenyebabGangguanViews, basename='jenis-penyebab-gangguan'
)
