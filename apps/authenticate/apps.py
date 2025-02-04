from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authenticate'
    
    def ready(self):
        import apps.authenticate.signals