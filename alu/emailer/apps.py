from django.apps import AppConfig


class EmailerConfig(AppConfig):
    name = 'alu.emailer'

    def ready(self):
        import alu.emailer.signals
