from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .user import User


class Rating(models.Model):
    DISLIKE_VALUE = -1
    LIKE_VALUE = 1

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    value = models.SmallIntegerField(default=0, validators=[
        MinValueValidator(DISLIKE_VALUE),
        MaxValueValidator(LIKE_VALUE)
    ])

    def __str__(self):
        return self.user + " " + self.value
