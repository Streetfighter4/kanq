from django.test import TestCase
from rest_framework.test import APIRequestFactory

from api.factories import PostFactory
from api.views.posts import PostViewSet


class PostApiTest(TestCase):

    def setUp(self):
        self.post = PostFactory()
        self.factory = APIRequestFactory()
        self.detail_view = PostViewSet.as_view({'get': 'retrieve'})
        self.list_view = PostViewSet.as_view({'get': 'list'})
        self.new_filter_view = PostViewSet.as_view({'get': 'new'})

    def test_get_to_list_uses_default_serializer(self):
        request = self.factory.get("api/posts")
        response = self.list_view(request)

        self.assertNotIn('comments', response.data)

    def test_get_to_detail_uses_detail_serializer(self):
        request = self.factory.get("api/posts/%d" % self.post.id)
        response = self.detail_view(request, pk=self.post.id)

        self.assertIn('comments', response.data)

    def test_get_to_post_new_returns_sorted_by_date(self):
        PostFactory.create_batch(3)
        request = self.factory.get("api/posts/new")
        response = self.new_filter_view(request)



