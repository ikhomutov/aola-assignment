from django.db.models.signals import post_save
from django.dispatch import receiver

from feedly.core import models as core_models
from .actions import CreateFeedEntryFromObjAction


@receiver(post_save, sender=core_models.Article)
@receiver(post_save, sender=core_models.SiteUserAchievement)
@receiver(post_save, sender=core_models.Advertisement)
def create_feed_entry(sender, instance, created, **kwargs):
    if not created:
        return
    action = CreateFeedEntryFromObjAction(obj=instance)
    action.perform()
