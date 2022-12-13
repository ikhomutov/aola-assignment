from rest_framework import serializers

from feedly.feed.models import FeedEntry


class FeedEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedEntry
        fields = ('id', 'title', 'activity_type', 'timestamp')
