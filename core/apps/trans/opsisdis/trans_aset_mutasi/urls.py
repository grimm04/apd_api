
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"trans/opsisdis/aset-mutasi", views.TransAsetMutasiViews, basename='trans-aset-mutasi'
) 