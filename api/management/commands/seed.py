from django.core.management import BaseCommand

from api.factories import TopicFactory, PostFactory
from api.models import User, Topic


class Command(BaseCommand):
    def handle(self, *args, **options):
        TopicFactory.create_batch(5)

        for topic in Topic.objects.all():
            PostFactory.create_batch(5, topic=topic)

