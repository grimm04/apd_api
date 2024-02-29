from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/pegawai/regu-petugas", views.REF_REGU_PETUGAS_MODELSViews, basename='pegawai-regu-petugas'
)