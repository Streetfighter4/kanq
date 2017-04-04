from django.test import TestCase
from django.urls import resolve
from rest_framework.test import APIRequestFactory, force_authenticate

from api.factories import PostFactory, UserFactory
from api.models import Post
from api.views.posts import PostViewSet


class PostApiTest(TestCase):

    def setUp(self):
        self.post = PostFactory()
        self.factory = APIRequestFactory()
        self.detail_view = PostViewSet.as_view({'get': 'retrieve'})
        self.list_view = PostViewSet.as_view({'get': 'list'})
        self.user = UserFactory()

    def test_get_to_list_uses_default_serializer(self):
        request = self.factory.get("api/posts")
        force_authenticate(request, user=self.user)

        response = self.list_view(request)
        self.assertNotIn('comments', response.data)

    def test_get_to_detail_uses_detail_serializer(self):
        request = self.factory.get("api/posts/%d" % self.post.id)
        force_authenticate(request, user=self.user)

        response = self.detail_view(request, pk=self.post.id)
        self.assertIn('comments', response.data)

