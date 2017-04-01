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

    @factory.post_generation
    def following(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for f in extracted:
                self.following.add(f)


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

    uri = factory.Faker('file_name', category='image')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    description = factory.Faker('text')
    title = factory.Faker('sentence')
    creator = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    image = factory.SubFactory(ImageFactory)
    created_at = fuzzy.FuzzyDateTime(datetime(2017, 1, 1, tzinfo=pytz.UTC))

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)


class BadgeFactory(DjangoModelFactory):
    MIN_PRICE = 10.00
    MAX_PRICE = 20.00
    PRICE_PRECISION = 2

    class Meta:
        model = Badge

    price = fuzzy.FuzzyDecimal(MIN_PRICE, MAX_PRICE, PRICE_PRECISION)
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker('text')
    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
    created_at = fuzzy.FuzzyDateTime(datetime(2017, 1, 1, tzinfo=pytz.UTC))

    # Subfactory needs to be added like that, because otherwise
    # it can't reference itself
    parent = factory.SubFactory('api.factories.CommentFactory')

    # Tell the recursion to go only up to 3 levels deep
    parent__parent__parent = None


class MedalFactory(DjangoModelFactory):
    MIN_RANK = 1
    MAX_RANK = 3

    class Meta:
        model = Medal

    rank = factory.fuzzy.FuzzyInteger(MIN_RANK, MAX_RANK)
    post = factory.SubFactory(PostFactory)


class RatingFactory(DjangoModelFactory):
    class Meta:
        model = Rating

    type = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    value = factory.fuzzy.FuzzyChoice([Rating.RATING_CHOICES[0][0], Rating.RATING_CHOICES[2][0]])
    post = factory.SubFactory(PostFactory)
    comment = factory.SubFactory(CommentFactory)
