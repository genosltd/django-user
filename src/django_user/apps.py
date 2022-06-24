from django.apps import AppConfig


class DjangoUserConfig(AppConfig):
    name = 'django_user'
    verbose_name = 'user'

    def ready(self):
        from . import signals
