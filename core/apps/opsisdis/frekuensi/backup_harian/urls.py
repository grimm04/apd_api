from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"opsisdis/frekuensi/backup-harian", views.BackupHarianViews, basename='frekuensi.backup-harian'
)