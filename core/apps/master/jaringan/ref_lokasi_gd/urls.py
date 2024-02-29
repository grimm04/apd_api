
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"master/jaringan/ref-lokasi-gd", views.RefLokasiGDViews, basename='jaringan-ref-lokasi-gd'
)