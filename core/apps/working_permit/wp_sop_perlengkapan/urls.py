
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/sop-perlengkapan", views.WPSOPPerlengkapanViews, basename='wp-sop-perlengkapan'
) 