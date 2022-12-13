from functools import singledispatchmethod

from feedly.core import models
from . import constants
from .models import FeedEntry


class CreateFeedEntryFromObjAction:
    def __init__(self, obj):
        self.obj = obj

    @singledispatchmethod
    def get_create_kwargs(self, obj):
        raise NotImplementedError('Unknown model for creating feed entry')

    @get_create_kwargs.register
    def _(self, obj: models.Article):
        return {'title': f'User {obj.author} just wrote a post {obj.title}',
                'timestamp': obj.created_at,
                'activity_type': constants.ACTIVITY_ARTICLE}

    @get_create_kwargs.register
    def _(self, obj: models.SiteUserAchievement):
        return {'title': (f'User {obj.user} just got an '
                          f'achievement {obj.achievement}'),
                'timestamp': obj.got_at,
                'activity_type': constants.ACTIVITY_ACHIEVEMENT}

    @get_create_kwargs.register
    def _(self, obj: models.Advertisement):
        return {'title': f'AD: {obj.title}',
                'timestamp': obj.published_at,
                'activity_type': constants.ACTIVITY_ADVERTISEMENT}

    def perform(self):
        create_kwargs = self.get_create_kwargs(self.obj)
        create_kwargs.update(
            content_object=self.obj
        )
        return FeedEntry.objects.create(**create_kwargs)
