from django.apps import AppConfig 

class TrafoGiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.opsisdis.telemetring.trafo_gi_non_ktt'
    label = 'telemetring_trafo_gi' 

    def ready(self):
        # import the scheduler in the ready function
        from apps.opsisdis.telemetring.trafo_gi_non_ktt.scheduler import start
        start()