from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"fasop/spectrum/his/rc", views.SCD_HIS_RCViews, basename='his-rc'
)
