
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"opsisdis/sld", views.DAF_SLD_GIViews, basename='opsisdid-sld'
) 