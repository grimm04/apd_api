from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/his/analog", views.SCD_HIS_ANALOGViews, basename='his-analog'
)
