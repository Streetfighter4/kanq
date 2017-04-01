from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from enum import Enum
from .user import User


class Rating(models.Model):
    RATING_CHOICES = (
        (-1, 'DISLIKE_VALUE'),
        (0, 'DEFAULT_VALUE'),
        (1, 'LIKE_VALUE'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    value = models.CharField(max_length=1, choices=RATING_CHOICES)

    def __str__(self):
        return self.user + " " + self.value
