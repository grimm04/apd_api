
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"master/pegawai/user", views.REF_PEGAWAIViews, basename='master-pegawai'
) 