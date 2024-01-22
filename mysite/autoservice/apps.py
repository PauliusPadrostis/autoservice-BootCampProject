from django.apps import AppConfig


class AutoserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autoservice'


class LibraryConfig(AppConfig):
    name = 'library'

    def ready(self):
        from .signals import create_profile, save_profile
