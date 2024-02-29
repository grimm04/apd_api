
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/online", views.WP_ONLINEViews, basename='wp-online'
) 