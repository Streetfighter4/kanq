from datetime import datetime, timedelta
import factory
import pytz
from factory import DjangoModelFactory

from api.models import User, Post, Image, Tag, Topic


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker('word')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class TopicFactory(DjangoModelFactory):
    class Meta:
        model = Topic

    name = factory.Faker('word')
    description = factory.Faker('text')
    start = datetime.now(pytz.utc)
    end = start + timedelta(weeks=1)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    createdAt = datetime.now(pytz.utc)
    uri = factory.Faker('file_name', category='image')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    description = factory.Faker('text')
    title = factory.Faker('sentence')
    createdAt = datetime.now(pytz.utc)
    creator = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    image = factory.SubFactory(ImageFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)

