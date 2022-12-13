from django.contrib import admin

from . import models


class SiteUserAchievementInline(admin.StackedInline):
    model = models.SiteUserAchievement
    extra = 0


@admin.register(models.SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    inlines = (SiteUserAchievementInline,)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at')


@admin.register(models.Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
