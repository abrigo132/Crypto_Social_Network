from django.db import models
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now())
    like_count = models.IntegerField(blank=True, null=True)
    dislike_count = models.IntegerField(blank=True, null=True)
    reposts_count = models.IntegerField(blank=True, null=True)
