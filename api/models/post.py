from django.db import models


class Post(models.Model):
    description = models.TextField(max_length=500)
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)