
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/online-pekerja", views.WP_ONLINE_PEKERJAViews, basename='wp-online-pekerja'
) 