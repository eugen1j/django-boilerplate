from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'django_boilerplate.user'

    def ready(self):
        from django_boilerplate.user import signals  # noqa
