from django.db import models

from .image import Image
from .topic import Topic
from .tag import Tag
from .user import User


class Post(models.Model):
    description = models.TextField(max_length=500)
    title = models.CharField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

