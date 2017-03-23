from django.db import models


class Image(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)
    uri = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.uri