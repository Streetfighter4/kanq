from django.test import TestCase
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory

from api.factories import CommentFactory, RatingFactory, UserFactory
from api.models import Rating
from api.views.comments import CommentViewSet


class CommentApiTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.rate_view = CommentViewSet.as_view({'put': 'rate'})
        self.user = UserFactory()

    def test_rate_view_update_correctly(self):
        new_comment = CommentFactory()
        RatingFactory(content_object=new_comment, value=Rating.LIKE_VALUE)
        data = {}
        data['vote'] = 1
        request = self.factory.put("api/comments/{id}/rate", data)
        force_authenticate(request, user=self.user)
        response = self.rate_view(request, pk=new_comment.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, new_comment.get_rating())
