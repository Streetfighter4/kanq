import logging

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .image import Image
from .rating import Rating
from .tag import Tag
from .topic import Topic
from .user import User

from api.helpers import redis_connection

logger = logging.getLogger(__name__)


class Post(models.Model):
    description = models.TextField(max_length=500)
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    ratings = GenericRelation(Rating)

    def save(self, *args, **kwargs):
        save_to_redis = False

        if not self.pk:
            save_to_redis = True

        super(Post, self).save(*args, **kwargs)

        if save_to_redis:
            redis_connection.push_new_post(self)

    def __str__(self):
        return self.title
