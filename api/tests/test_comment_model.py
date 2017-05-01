import random

from django.test import TestCase

from api.factories import RatingFactory, CommentFactory
from api.models import Rating


class CommentModelTest(TestCase):
    def setUp(self):
        self.comment = CommentFactory()

    def test_ratings_are_calculated_correctly(self):
        like_count = random.randint(0, 100)
        dislike_count = random.randint(0, 100)
        expected_rating = like_count * Rating.LIKE_VALUE + dislike_count * Rating.DISLIKE_VALUE

        RatingFactory.create_batch(like_count, value=Rating.LIKE_VALUE, content_object=self.comment)
        RatingFactory.create_batch(dislike_count, value=Rating.DISLIKE_VALUE, content_object=self.comment)

        self.assertEqual(expected_rating, self.comment.get_rating())
