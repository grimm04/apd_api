from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/pegawai/perusahaan", views.PerusahaanViews, basename='pegawai-perusahaan'
)
