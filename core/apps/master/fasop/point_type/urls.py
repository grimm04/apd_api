from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/point-type-tree", views.PointTypeTreeViews, basename='point-type-tree'
)
router.register(
    r"master/fasop/point-type", views.PointTypeViews, basename='point-type'
)

