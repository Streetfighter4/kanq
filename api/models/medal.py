from django.db import models

from .post import Post
from .user import User


class Medal(models.Model):
    rank = models.IntegerField()
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.post.title, self.rank)
