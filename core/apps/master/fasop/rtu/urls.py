from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/rtu", views.RTUViews, basename='rtu'
)

router.register(
    r"master/fasop/rtu-tree", views.RTUTreeViews, basename='rtu'
)
