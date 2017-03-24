from django.db import models

from .user import User
from .post import Post

class Badge():
    price = models.FloatField()
    users = models.ForeignKey(User)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)