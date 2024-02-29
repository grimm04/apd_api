
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/master-sop-jsa", views.WP_MASTER_SOP_JSAViews, basename='wp-master-sop-jsa'
) 