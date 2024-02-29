from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"apkt/apkt-trans-log", views.APKTTransLogViews, basename='apkt-trans-log'
)