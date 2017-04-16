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

    def is_active(self):
        return self.start <= datetime.now(pytz.utc) <= self.end

    def has_ended(self):
        now = datetime.now(pytz.utc)
        return self.start <= now and self.end <= now

    def get_best_post(self):
        posts = self.posts.all()

        if posts.count() <= 0:
            return None

        return max(posts, key=lambda p: p.get_rating() or 0)

    def __str__(self):
        return self.name