
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/aproval-ttd", views.WP_APROVAL_TTDViews, basename='wp-aproval-ttd'
) 