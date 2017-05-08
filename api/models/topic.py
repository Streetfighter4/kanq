from datetime import datetime

import pytz
from django.db import models

from .tag import Tag


class Topic(models.Model):
    name = models.CharField(max_length=500, blank=False)
    description = models.TextField(max_length=150)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)
    tags = models.ManyToManyField(Tag, related_name='topics')
    closed = models.BooleanField(default=False)

    def is_active(self):
        return self.start <= datetime.now(pytz.utc) <= self.end

    def has_ended(self):
        now = datetime.now(pytz.utc)
        return self.start <= now and self.end <= now

    def get_best_posts(self, post_count=1):
        posts = self.posts.all()

        if posts:
            return sorted(posts, key=lambda p: -p.get_rating())[:post_count]
        else:
            return None

    @staticmethod
    def get_topics_to_close():
        return Topic.objects.filter(end__lt=datetime.now(pytz.utc), closed=False)

    def __str__(self):
        return self.name
