from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/his/rtu", views.SCD_HIS_RTUViews, basename='his-rtu'
)
