from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/path-1", views.Path1View, basename='path-1'
)