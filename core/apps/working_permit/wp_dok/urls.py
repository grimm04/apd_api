
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/dok", views.WP_DOKViews, basename='wp-dok'
) 