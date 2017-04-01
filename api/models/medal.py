from django.db import models

from .post import Post


class Medal(models.Model):
    rank = models.IntegerField()
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='medal_post')

    def __str__(self):
        return "%s %s" % (self.post.title, self.rank)
