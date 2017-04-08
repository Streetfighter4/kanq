from django.core.management import BaseCommand

from api.factories import TopicFactory, PostFactory, RatingFactory
from api.models import Topic, Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        TopicFactory.create_batch(5)

        for topic in Topic.objects.all():
            PostFactory.create_batch(5, topic=topic)

        for post in Post.objects.all():
            RatingFactory.create_batch(5, content_object=post)
