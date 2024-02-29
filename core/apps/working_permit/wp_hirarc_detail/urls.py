
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/hirarc-detail", views.WP_HIRARC_DETAILViews, basename='wp-hirarc-detail'
) 