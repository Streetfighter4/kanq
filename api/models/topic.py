from django.core.checks import Tags
from django.db import models


class Topic(models.Model):
    name = models.TextField(max_length=500)
    start = models.DateField()
    end = models.DateField()
    tags = models.ManyToManyField(Tags, on_delete=models.CASCADE)