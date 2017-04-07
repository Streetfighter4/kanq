from datetime import datetime, timedelta

import pytz
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from api.factories import TopicFactory, UserFactory
from api.serializers import TopicSerializer
from api.views.topics import TopicViewSet


class TopicAPITest(TestCase):
    def setUp(self):
        self.factory = APIClient()
        self.active_topics_view = TopicViewSet.as_view({'get': 'active'})
        self.inactive_topics_view = TopicViewSet.as_view({'get': 'active'})
        self.active_topics = TopicFactory.create_batch(3, start=datetime.now(pytz.utc) - timedelta(days=3),
                                                       end=datetime.now(pytz.utc) + timedelta(days=4))
        self.inactive_topics = TopicFactory.create_batch(3, start=datetime.now(pytz.utc) + timedelta(weeks=1),
                                                       end=datetime.now(pytz.utc) + timedelta(weeks=2))
        self.user = UserFactory()

    def test_active_topics_endpoint_works(self):
        request = self.factory.get("/api/topics/active")
        force_authenticate(request, user=self.user)
        response = self.active_topics_view(request)
        print(response.data)

        for topic in response.data:
            self.assertIn(topic, self.active_topics)

        for topic in self.inactive_topics:
            self.assertNotIn(topic, response.data)
