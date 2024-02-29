from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/c-point", views.CPointViews, basename='c-point'
)
