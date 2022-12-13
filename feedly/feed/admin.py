from django.contrib import admin

from .models import FeedEntry


@admin.register(FeedEntry)
class FeedEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'activity_type')
    list_filter = ('activity_type',)
