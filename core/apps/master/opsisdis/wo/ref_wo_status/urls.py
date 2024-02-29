
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"master/opsisdis/wo/ref-wo-status", views.RefWOStatusViews, basename='ref-wo-status'
) 