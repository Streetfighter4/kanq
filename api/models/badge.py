from django.db import models

from .user import User
from .post import Post


class Badge(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)