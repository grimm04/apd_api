from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/external/ext-user-token-role", views.ExtUserTokenRoleViews, basename='ext-user-token-role'
)
