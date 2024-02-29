
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"master/aset/ref-aset-ext-atr", views.RefAsetExtAtrViews, basename='aset-ref-aset-ext-atr'
) 