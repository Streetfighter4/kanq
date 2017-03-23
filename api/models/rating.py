from django.db import models

from .comment import Comment
from .post import Post
from .user import User


class Rating(models.Model):
    type = models.CharField(max_length=32, blank=False)
    value = models.BigIntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)