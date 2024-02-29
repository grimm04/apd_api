from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/management-upload/gardu-induk", views.GarduIndukView, basename='gardu-induk'
)