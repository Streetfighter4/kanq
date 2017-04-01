from django.test import TestCase
from django.urls import resolve
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from api.models import Image
from api.models import Post
from api.models import Topic
from api.models import User
from api.views.posts import PostViewSet


class PostApiTest(TestCase):

    def setUp(self):
        user = User.objects.create()
        topic = Topic.objects.create(start=timezone.now(), end=timezone.now())
        image = Image.objects.create()
        self.post = {
            'title': 'Some random post',
            'description': 'This is the best post',
            'creator': user,
            'topic': topic,
            'image': image,
        }
        self.factory = APIRequestFactory()
        self.create_view = PostViewSet.as_view({'post': 'create'})

    def test_get_to_list_uses_default_serializer(self):
        url = '/api/posts/'
        view = resolve(url)
        request = self.factory.get(url)
        response = view.func(request)

        self.assertNotIn('comments', response.data)

    def test_get_to_detail_uses_detail_serializer(self):
        Post.objects.create(**self.post)
        url = '/api/posts/1/'
        view = resolve(url)
        request = self.factory.get(url)
        response = view.func(request, pk=1)

        self.assertIn('comment_post', response.data)

