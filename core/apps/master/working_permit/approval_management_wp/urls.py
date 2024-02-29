from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/working-permit/approval-management-wp", views.ApprovalManagementWPView, basename='approval-management-wp'
)