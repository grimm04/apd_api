from django.apps import AppConfig


class PenyulangConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.opsisdis.telemetring.penyulang'
    label = 'telemetring_penyulang'

    def ready(self):
        # import the scheduler in the ready function
        from apps.opsisdis.telemetring.penyulang.scheduler import start
        start()