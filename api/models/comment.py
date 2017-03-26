from django.db import models

from .post import Post
from .user import User


class Comment(models.Model):
    content = models.TextField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', null=True)

    def __str__(self):
        return self.content