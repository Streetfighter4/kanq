from django.db import models


class Image(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    uri = models.CharField(max_length=500)
