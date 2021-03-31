from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'django_boilerplate.blog'

    def ready(self):
        from django_boilerplate.blog import signals  # noqa
