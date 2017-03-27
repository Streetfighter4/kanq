from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .comment import Comment
from .post import Post
from .user import User


class Rating(models.Model):
    DISLIKE_VALUE = -1
    LIKE_VALUE = 1

    type = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.SmallIntegerField(default=0, validators=[
        MinValueValidator(DISLIKE_VALUE),
        MaxValueValidator(LIKE_VALUE),
    ])
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.post + " " + self.value
