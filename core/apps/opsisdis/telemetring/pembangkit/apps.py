from django.apps import AppConfig


class PembangkitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.opsisdis.telemetring.pembangkit'
    label = 'telemetring_pembangkit'

    def ready(self):
        # import the scheduler in the ready function
        from apps.opsisdis.telemetring.pembangkit.scheduler import start
        start()