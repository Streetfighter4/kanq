from django.utils import timezone

from api.models import Topic


def update_topics():
    Topic.objects.create(name="test topic cron", start=timezone.now(), end=timezone.now())
