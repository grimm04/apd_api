from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/working-permit/risk-point-qrc", views.RiskPointQRCView, basename='risk-point-qrc'
)