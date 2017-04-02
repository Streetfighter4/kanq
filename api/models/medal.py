from django.db import models

from .user import User
from .post import Post


class Medal(models.Model):
    rank = models.IntegerField()
    user = models.ForeignKey(User, related_name='medals')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='medal')

    def __str__(self):
        return "%s %s" % (self.post.title, self.rank)
