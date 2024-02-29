from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"master/management-upload/temp", views.ManagemetUploadTempView, basename='management-upload'
)
router.register(
    r"master/management-upload/temp", views.ManagemetUploadDataView, basename='management-upload-data'
)