import pytz
from datetime import datetime, timedelta
from django.test import TestCase

from api.factories import TopicFactory
from rest_framework.test import APIRequestFactory, force_authenticate
from api.factories import UserFactory
from api.serializers import TopicSerializer
from api.views.topics import TopicViewSet


class TopicAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.active_view = TopicViewSet.as_view({'get': 'active'})
        self.inactive_view = TopicViewSet.as_view({'get': 'inactive'})
        self.user = UserFactory()

        self.active_topics_count = 5
        self.inactive_topics_count = 5

        TopicFactory.create_batch(self.active_topics_count, start=datetime.now(pytz.utc) - timedelta(days=3),
                                  end=datetime.now(pytz.utc) + timedelta(days=4))
        TopicFactory.create_batch(self.inactive_topics_count, start=datetime.now(pytz.utc) + timedelta(weeks=1),
                                  end=datetime.now(pytz.utc) + timedelta(weeks=2))

    def test_active_topics_are_returned_correctly(self):
        request = self.factory.get("api/topics/active")
        force_authenticate(request, user=self.user)
        response = self.active_view(request)
        topics = TopicSerializer(data=response.data['results'], many=True)
        topics.is_valid(raise_exception=True)
        topics = topics.create(topics.validated_data)

        self.assertEqual(self.active_topics_count, len(topics))

        for topic in topics:
            self.assertTrue(topic.is_active())

    def test_inactive_topics_are_returned_correctly(self):
        request = self.factory.get("api/topics/inactive")
        force_authenticate(request, user=self.user)
        response = self.inactive_view(request)
        topics = TopicSerializer(data=response.data['results'], many=True)
        topics.is_valid(raise_exception=True)
        topics = topics.create(topics.validated_data)

        self.assertEqual(self.inactive_topics_count, len(topics))

        for topic in topics:
            self.assertFalse(topic.is_active())
