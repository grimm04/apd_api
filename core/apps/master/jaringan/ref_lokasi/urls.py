
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"master/jaringan/ref-lokasi", views.RefLokasiViews, basename='jaringan-ref-lokasi'
)
# router.register(
#     r"master/jaringan/unit-pembangkit", views.UnitPembangkitViews, basename='jaringan-unit-pembangkit'
# )
# router.register(
#     r"master/jaringan/pembangkit", views.PembangkitViews, basename='jaringan-pembangkit'
# )
# router.register(
#     r"master/jaringan/gardu-induk", views.GIViews, basename='ardu-induk'
# )