from django.db import models


class Comment(models.Model):
    description = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perantComment = models.ForeignKey("self")