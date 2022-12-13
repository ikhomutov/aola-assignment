import logging

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .constants import ACTIVITY_TYPES

logger = logging.getLogger(__name__)


class FeedEntry(models.Model):
    activity_type = models.CharField(
        max_length=100, choices=[(at, at) for at in ACTIVITY_TYPES]
    )
    title = models.TextField()
    timestamp = models.DateTimeField()
    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = 'FeedEntries'
        ordering = ('timestamp', )
