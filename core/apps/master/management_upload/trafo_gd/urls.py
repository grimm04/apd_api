from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/management-upload/trafo-gardu-distribusi", views.TrafoGDView, basename='trafo-gd'
)