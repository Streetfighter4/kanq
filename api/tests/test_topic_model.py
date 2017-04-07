from datetime import datetime, timedelta

import pytz
from django.test import TestCase

from api.factories import TopicFactory, PostFactory, RatingFactory
from api.models import Rating


class TopicModelTest(TestCase):
    def setUp(self):
        self.ended_topic = TopicFactory(start=datetime.now(pytz.utc) - timedelta(weeks=2),
                                   end=datetime.now(pytz.utc) - timedelta(weeks=1))

        self.active_topic = TopicFactory(start=datetime.now(pytz.utc) - timedelta(days=3),
                                    end=datetime.now(pytz.utc) + timedelta(days=4))

        self.future_topic = TopicFactory(start=datetime.now(pytz.utc) + timedelta(weeks=1),
                                    end=datetime.now(pytz.utc) + timedelta(weeks=2))

    def test_topic_active_method_works_correctly(self):
        self.assertFalse(self.ended_topic.is_active())
        self.assertTrue(self.active_topic.is_active())
        self.assertFalse(self.future_topic.is_active())

    def test_topic_has_ended_method_works_correctly(self):
        self.assertTrue(self.ended_topic.has_ended())
        self.assertFalse(self.active_topic.has_ended())
        self.assertFalse(self.future_topic.has_ended())

    def test_best_post_method_works_correctly(self):
        best_post = PostFactory(topic=self.active_topic)
        RatingFactory.create_batch(20, content_object=best_post, value=Rating.LIKE_VALUE)

        other_posts = PostFactory.create_batch(5, topic=self.active_topic)

        for post in other_posts:
            RatingFactory.create_batch(10, content_object=post)

        self.assertEqual(best_post, self.active_topic.best_post())
