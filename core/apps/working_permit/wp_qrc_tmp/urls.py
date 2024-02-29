
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/qrc-tmp", views.WP_QRC_TMPViews, basename='wp-qrc-tmp'
) 