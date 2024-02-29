
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"trans/opsisdis/wo-log-status", views.TransWoLogStatusViews, basename='trans-wo-log-status'
) 