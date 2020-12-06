from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'alu.core'

    def ready(self):
        import alu.core.signals
