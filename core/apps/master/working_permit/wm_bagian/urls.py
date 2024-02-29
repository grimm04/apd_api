from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/working-permit/bagian", views.WP_BAGIANViews, basename='wp-bagian'
)
