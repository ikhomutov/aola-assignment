from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from feedly.feed.models import FeedEntry
from .filters import FeedActivityTypeFilter
from .serializers import FeedEntrySerializer


class FeedListView(ListAPIView):
    serializer_class = FeedEntrySerializer
    filter_backends = [SearchFilter, FeedActivityTypeFilter]
    queryset = FeedEntry.objects.all()
    search_fields = ('title',)
