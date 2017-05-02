from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Sum

from .rating import Rating
from .post import Post
from .user import User


class Comment(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    ratings = GenericRelation(Rating)

    def get_rating(self):
        rating = self.ratings.aggregate(Sum('value'))['value__sum']
        return rating or 0

    def get_current_user_vote(self, user):
        return Rating.objects.filter(user=user, object_id=self.id).first()

    def __str__(self):
        return self.content
