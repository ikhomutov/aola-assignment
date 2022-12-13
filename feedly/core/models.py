from django.db import models


class SiteUser(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    author = models.ForeignKey(
        to=SiteUser,
        related_name='articles',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=512)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=256)
    condition = models.TextField()
    icon = models.ImageField()
    users = models.ManyToManyField(
        to=SiteUser,
        through='SiteUserAchievement'
    )

    def __str__(self):
        return self.title


class SiteUserAchievement(models.Model):
    user = models.ForeignKey(
        to=SiteUser,
        on_delete=models.CASCADE
    )
    achievement = models.ForeignKey(
        to=Achievement,
        on_delete=models.CASCADE
    )
    got_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f'{self.user} - {self.achievement}'


class Advertisement(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
