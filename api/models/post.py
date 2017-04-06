import redis
import logging
from api import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from .rating import Rating
from .image import Image
from .topic import Topic
from .tag import Tag
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
            followers_ids = self.creator.followers.values_list('id', flat=True)
            redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

            try:
                redis_instance.ping()
            except redis.ConnectionError:
                logger.warning("Could not establish redis connection on %s:%s" % (settings.REDIS_HOST, settings.REDIS_PORT))
                return

            redis_pipe = redis_instance.pipeline(transaction=False)

            for follower_id in followers_ids:
                redis_pipe.lpush(follower_id, self.id).ltrim(follower_id, 0, settings.REDIS_FEED_MAX_LENGTH)

            redis_pipe.execute()

    def __str__(self):
        return self.title
