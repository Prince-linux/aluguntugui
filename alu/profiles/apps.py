from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'alu.profiles'

    def ready(self):
        import alu.profiles.signals
