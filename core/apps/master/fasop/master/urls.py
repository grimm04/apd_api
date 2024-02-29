from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/fasop/master", views.FASOPMASTERViews, basename='fasop-master'
)