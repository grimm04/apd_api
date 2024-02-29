
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)  
router.register(
    r"opsisdis/rekap-padam/trans-ep-peralatan", views.TransEpPeralatanViews, basename='trans-ep-peralatan'
) 