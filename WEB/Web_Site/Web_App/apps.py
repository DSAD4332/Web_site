from django.apps import AppConfig

class WebAppConfig(AppConfig):
    name = 'Web_App' 
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import Web_App.signals  
