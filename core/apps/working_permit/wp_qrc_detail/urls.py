
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/qrc-detail", views.WP_QRC_DETAILViews, basename='wp-qrc-detail'
) 