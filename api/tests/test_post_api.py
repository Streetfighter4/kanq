from django.test import TestCase

from api.factories import TopicFactory
from rest_framework.test import APIRequestFactory, force_authenticate
from api.factories import PostFactory, UserFactory
from api.views.posts import PostViewSet


class PostApiTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.detail_view = PostViewSet.as_view({'get': 'retrieve'})
        self.list_view = PostViewSet.as_view({'get': 'list'})
        self.new_filter_view = PostViewSet.as_view({'get': 'new'})
        self.user = UserFactory()

    def test_get_to_list_uses_default_serializer(self):
        PostFactory()
        request = self.factory.get("api/posts")
        force_authenticate(request, user=self.user)

        response = self.list_view(request)
        self.assertNotIn('comments', response.data[0])

    def test_get_to_detail_uses_detail_serializer(self):
        post = PostFactory()
        request = self.factory.get("api/posts/%d" % post.id)
        force_authenticate(request, user=self.user)
        response = self.detail_view(request, pk=post.id)

        self.assertIn('comments', response.data)

    def test_get_to_post_new_returns_sorted_by_date(self):
        batch_size = 3
        PostFactory.create_batch(batch_size)
        request = self.factory.get("api/posts/new")
        force_authenticate(request, user=self.user)
        response = self.new_filter_view(request)

        posts = response.data

        for i in range(len(posts) - 1):
            self.assertGreater(posts[i]['created_at'], posts[i + 1]['created_at'])

    def test_get_to_post_new_returns_filtered_by_topic(self):
        batch_size = 3
        topic = TopicFactory()
        PostFactory.create_batch(batch_size, topic=topic)
        PostFactory.create_batch(batch_size)
        request = self.factory.get("api/posts/new/", {'topic_id': topic.id})
        force_authenticate(request, user=self.user)
        response = self.new_filter_view(request)

        posts = response.data

        for post in posts:
            self.assertEqual(post['topic']['id'], topic.id)


    def test_get_to_post_new_returns_all_when_topic_filter_wrong(self):
        batch_size = 3
        PostFactory.create_batch(batch_size)
        request = self.factory.get("api/posts/new/", {'topic_id': 'gibberish'})
        force_authenticate(request, user=self.user)
        response = self.new_filter_view(request)

        posts = response.data

        self.assertEqual(len(posts), batch_size)
