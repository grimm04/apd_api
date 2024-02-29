from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/point-type-state", views.PointTypeStateViews, basename='point-type-state'
)
