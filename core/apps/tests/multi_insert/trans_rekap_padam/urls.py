
from rest_framework import routers
from . import views 


router = routers.DefaultRouter(trailing_slash=False) 
router.register(
    r"test/multi-insert/trans-rekap-padam", views.TransRekapPadamViews, basename='test-trans-rekap-padam'
)  