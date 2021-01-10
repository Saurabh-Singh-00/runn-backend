from django.apps import AppConfig


class MarathonConfig(AppConfig):
    name = 'marathon'

    def ready(self):
        import signals
