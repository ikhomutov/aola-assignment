from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from feedly.feed.constants import ACTIVITY_TYPES, ACTIVITY_ADVERTISEMENT


class FeedActivityTypeFilter(BaseFilterBackend):
    activity_type_param = 'type'

    def filter_queryset(self, request, queryset, view):
        params = request.query_params.get(self.activity_type_param)

        if not params:
            return queryset
        activity_types = [param.strip() for param in params.split(',')]
        q = Q()
        for activity_type in activity_types:
            if activity_type in ACTIVITY_TYPES:
                q = q | Q(activity_type__iexact=activity_type)

        if ACTIVITY_ADVERTISEMENT not in activity_types:
            q = q | Q(activity_type__iexact=ACTIVITY_ADVERTISEMENT)
        return queryset.filter(q)
