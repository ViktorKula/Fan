from django.apps import AppConfig


class WallConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wall'

    def ready(self):
        from . import signals
