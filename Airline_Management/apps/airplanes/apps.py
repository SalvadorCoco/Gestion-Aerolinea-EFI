from django.apps import AppConfig

class AirplanesConfig(AppConfig):
    name = 'apps.airplanes'

    def ready(self):
        import apps.airplanes.models