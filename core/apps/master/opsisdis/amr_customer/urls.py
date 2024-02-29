from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/opsisdis/amr-customer", views.TelemetringAMRCustomerViews, basename='telemetring-amr-customer'
)