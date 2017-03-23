from django.db import models

from .tag import Tag


class Topic(models.Model):
    name = models.TextField(max_length=500, blank=False)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)
    tags = models.ManyToManyField(Tag)