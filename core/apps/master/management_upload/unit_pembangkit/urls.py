from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/management-upload/unit-pembangkit", views.UnitPembangkitView, basename='unit-pembangkit'
)