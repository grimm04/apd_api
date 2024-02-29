
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"working-permit/hirarc", views.WP_HIRARCViews, basename='wp-hirarc'
) 
router.register(
    r"working-permit/hirarc/pdf", views.GenerateHirarcViews, basename='wp-hirarc-pdf'
) 