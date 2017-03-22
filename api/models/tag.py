from django.db import models

from api.models.post import Post
from api.models.topic import Topic


class Tag(models.Model):
    name = models.TextField(max_length=500)
    topic = models.ManyToManyField(Topic, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post, on_delete=models.CASCADE)