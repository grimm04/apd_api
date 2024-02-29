from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/kin/master-hari", views.SCD_KIN_MASTER_HARIANViews, basename='kin-master-harian'
)
