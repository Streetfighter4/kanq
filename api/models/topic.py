from django.db import models


class Topic(models.Model):
    name = models.TextField(max_length=500)
    start = models.DateField()
    end = models.DateField()
    