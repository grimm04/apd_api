from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/path-3", views.Path3View, basename='path-3'
)