from django.db import models

from api.models.comment import Comment
from api.models.post import Post
from api.models.user import User


class Rating(models.Model):
    type = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)