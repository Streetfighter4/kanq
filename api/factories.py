import random
from datetime import datetime, timedelta

import factory
import pytz
from factory import DjangoModelFactory
from factory import fuzzy

from api.models import Comment
from api.models import Medal
from api.models import Rating
from api.models import User, Post, Image, Tag, Topic, Badge


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


class BadgeFactory(DjangoModelFactory):
    class Meta:
        model = Badge

    price = fuzzy.FuzzyDecimal(10, 20, 2)
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker('text')
    createdAt = datetime.now(pytz.utc)
    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
    parent = None

class MedalFactory(DjangoModelFactory):
    class Meta:
        model = Medal

    rank = factory.fuzzy.FuzzyInteger(1, 3)
    post = factory.SubFactory(PostFactory)

class RatingFactory(DjangoModelFactory):
    class Meta:
        model = Rating

    type = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    value = factory.fuzzy.FuzzyChoice([-1, 1])
    post = factory.SubFactory(PostFactory)
    comment = factory.SubFactory(CommentFactory)
