

from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False)
router.register( 
    r"master/jaringan/ref-pemilik-jaringan", views.RefPemilikJaringanViews, basename='jaringan-ref-pemilik-jaringan'
)  