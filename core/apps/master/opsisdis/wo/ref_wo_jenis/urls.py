
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"master/opsisdis/wo/ref-wo-jenis", views.RefWOJenisViews, basename='ref-wo-jenis'
) 