from django.apps import AppConfig


class ExtModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.external.ext_module'
