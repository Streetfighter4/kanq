from django.db import models

from .tag import Tag


class Topic(models.Model):
    name = models.CharField(max_length=500, blank=False)
    description = models.TextField(max_length=150)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)
    tags = models.ManyToManyField(Tag, related_name='topic_tags')

    def __str__(self):
        return self.name