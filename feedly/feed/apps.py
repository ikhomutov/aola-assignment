from django.apps import AppConfig


class FeedAppConfig(AppConfig):
    name = 'feedly.feed'

    def ready(self):
        from . import signals  # noqa
