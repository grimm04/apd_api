
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"trans/opsisdis/pm-detail", views.TransPMDetailViews, basename='trans-pm'
) 