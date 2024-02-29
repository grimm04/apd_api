
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"master/opsisdis/pm/ref-pm-detail-logic", views.RefPMDetailLogicViews, basename='ref-pm-detail-logic'
) 