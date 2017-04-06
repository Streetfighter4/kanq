from datetime import datetime, timedelta

import pytz
from django.test import TestCase

from api.factories import TopicFactory


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
