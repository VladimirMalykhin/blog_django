from django.db import models

# Create your models here.
from django.utils import timezone


class Blog(models.Model):
    author = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    title = models.CharField(max_length=140)


class Comments(models.Model):
    author = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    post_id = models.CharField(max_length=140)
