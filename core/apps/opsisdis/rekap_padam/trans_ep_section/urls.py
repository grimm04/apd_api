
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"opsisdis/rekap-padam/trans-ep-section", views.TransEpSectionViews, basename='trans-ep-section'
) 