from django.db import models

from .tag import Tag


class Topic(models.Model):
    name = models.TextField(max_length=500)
    start = models.DateField()
    end = models.DateField()
    tags = models.ManyToManyField(Tag)