from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/external/ext-user-token", views.ExtUserTokenViews, basename='ext-user-token'
)
