import logging
import math

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Sum
from django.utils import timezone

from api.helpers import redis_connection
from .image import Image
from .rating import Rating
from .tag import Tag
from .topic import Topic
from .user import User

logger = logging.getLogger(__name__)


class Post(models.Model):
    description = models.TextField(max_length=500)
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    ratings = GenericRelation(Rating)

    def save(self, *args, **kwargs):
        save_to_redis = False

        if not self.pk:
            save_to_redis = True

        super(Post, self).save(*args, **kwargs)

        if save_to_redis:
            redis_connection.push_new_post(self)

    def get_rating(self):
        rating = self.ratings.aggregate(Sum('value'))['value__sum']
        return rating or 0

    def get_trend_coefficient(self, old_time):
        time_alive = max(float((timezone.now() - self.created_at).total_seconds()), 1.01)
        n = 2
        normalizer = pow(10, 5)
        if time_alive < old_time:
            coef = (math.pow(self.get_rating(), n) * old_time) \
                   / (math.log(time_alive) * normalizer)
        else:
            coef = 0

        return coef

    def get_current_user_vote(self, user):
        return Rating.objects.filter(user=user, object_id=self.id).first()

    def __str__(self):
        return self.title
