from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/master-bulan", views.SCD_KIN_MASTER_BULANViews, basename='kin-master-bulanan'
)
