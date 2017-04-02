from django.db import models

from .user import User
from .post import Post


class Badge(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(User, related_name='badges')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='badges')
