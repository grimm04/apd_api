from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"apkt/apkt-trans-jar", views.APKTTransJARViews, basename='apkt-trans-jar'
)