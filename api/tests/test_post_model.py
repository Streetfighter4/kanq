import random

from django.test import TestCase

from api.factories import RatingFactory, PostFactory
from api.models import Rating


class PostModelTest(TestCase):
    def setUp(self):
        self.post = PostFactory()

    def test_ratings_are_calculated_correctly(self):
        like_count = random.randint(0, 100)
        dislike_count = random.randint(0, 100)
        expected_rating = like_count * Rating.LIKE_VALUE + dislike_count * Rating.DISLIKE_VALUE

        RatingFactory.create_batch(like_count, value=Rating.LIKE_VALUE, content_object=self.post)
        RatingFactory.create_batch(dislike_count, value=Rating.DISLIKE_VALUE, content_object=self.post)

        self.assertEqual(expected_rating, self.post.get_rating())

