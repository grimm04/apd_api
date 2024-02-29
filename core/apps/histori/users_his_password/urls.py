from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"his/users/password", views.UsersHisPasswordViews, basename='his-users-password'
)