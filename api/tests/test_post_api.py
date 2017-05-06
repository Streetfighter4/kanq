from datetime import timedelta

from django.utils import timezone
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from api.factories import PostFactory, UserFactory, RatingFactory, TopicFactory
from api.models import Rating, Post
from api.serializers import PostSerializer

from api.views.posts import PostViewSet


class PostApiTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.detail_view = PostViewSet.as_view({'get': 'retrieve'})
        self.list_view = PostViewSet.as_view({'get': 'list'})
        self.trending_view = PostViewSet.as_view({'get': 'trending'})
        self.new_filter_view = PostViewSet.as_view({'get': 'new'})
        self.create_view = PostViewSet.as_view({'post': 'create'})
        self.top_view = PostViewSet.as_view({'get': 'top'})
        self.rate_view = PostViewSet.as_view({'put': 'rate'})
        self.user = UserFactory()

    def test_get_to_list_uses_default_serializer(self):
        PostFactory()
        request = self.factory.get("api/posts")
        force_authenticate(request, user=self.user)

        response = self.list_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn('comments', response.data['results'][0])

    def test_get_to_detail_uses_detail_serializer(self):
        post = PostFactory()
        request = self.factory.get("api/posts/%d" % post.id)
        force_authenticate(request, user=self.user)
        response = self.detail_view(request, pk=post.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('comments', response.data)

    def test_get_to_post_new_returns_sorted_by_date(self):
        batch_size = 3
        PostFactory.create_batch(batch_size)
        request = self.factory.get("api/posts/new")
        force_authenticate(request, user=self.user)
        response = self.new_filter_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.data

        for post in posts:
            self.assertEqual(post['topic']['id'], topic.id)

    def test_get_to_post_new_returns_all_when_topic_filter_wrong(self):
        batch_size = 3
        PostFactory.create_batch(batch_size)
        request = self.factory.get("api/posts/new/", {'topic_id': 'gibberish'})
        force_authenticate(request, user=self.user)
        response = self.new_filter_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.data

        self.assertEqual(len(posts), batch_size)

    def test_new_create_post_is_created(self):
        topic = TopicFactory()
        newPost = PostFactory.build()
        data = PostSerializer(newPost).data
        data['creator_id'] = self.user.id

        data['topic_id'] = topic.id
        data['image'] = 'iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAABHNCSVQICAgIfAhkiAAAABtJREFUCJlj/M/A8J/hBgMDA4Pa//8M/xX/AwA5YgcbF4ARSAAAAABJRU5ErkJggg=='
        data['extension'] = '.png'
        request = self.factory.post("api/posts/", data, format='json')
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, (Post.objects.filter(creator_id=self.user.id)).count())

    def test_create_view_update_image(self):
        topic = TopicFactory()
        newPost = PostFactory.build()
        data = PostSerializer(newPost).data
        data['creator_id'] = self.user.id
        data['topic_id'] = topic.id
        data['image'] = 'iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAABHNCSVQICAgIfAhkiAAAABtJREFUCJlj/M/A8J/hBgMDA4Pa//8M/xX/AwA5YgcbF4ARSAAAAABJRU5ErkJggg=='
        data['extension'] = '.png'
        request = self.factory.post("api/posts/", data, format='json')
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['image'])

    def test_top_view_sort_correctly(self):
        batch_size = 5
        new_posts = PostFactory.create_batch(batch_size)

        for p in new_posts:
            RatingFactory.create_batch(batch_size, content_object=p)

        request = self.factory.get("api/posts/top")
        force_authenticate(request, user=self.user)
        response = self.top_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.data

        for i in range(len(posts) - 1):
            self.assertGreaterEqual(posts[i]['rating'], posts[i + 1]['rating'])

    def test_top_view_sort_right_posts(self):
        data={}
        data['topic'] = TopicFactory()
        request = self.factory.get("api/posts", data)
        force_authenticate(request, user=self.user)
        response = self.top_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.data
        for i in range(len(posts) - 1):
            self.assertEqual(posts[i]['topic'], data['topic'])

    # def test_top_view_return_ten_posts_for_paginate(self):
    #     batch_size = 15
    #     PostFactory.create_batch(batch_size)
    #
    #     data = {}
    #     data['limit'] = batch_size
    #
    #     request = self.factory.get("api/posts/top", data)
    #     force_authenticate(request, user=self.user)
    #     response_without_pagination = self.top_view(request).data
    #     #print(response_without_pagination)
    #
    #     i = 0
    #     while True:
    #         data = {}
    #         data['offset'] = i * REST_FRAMEWORK['PAGE_SIZE']
    #         data['limit'] = REST_FRAMEWORK['PAGE_SIZE']
    #
    #         request = self.factory.get("api/posts/top", data)
    #         force_authenticate(request, user=self.user)
    #         response = self.top_view(request)
    #         response.render()
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         print(response.contentf)
    #         result = json.loads(str(response.content))
    #         if result['next'] is None:
    #             break
    #         posts = result['results']
    #         self.assertLessEqual(len(posts), REST_FRAMEWORK['PAGE_SIZE'])
    #
    #         for j, post in enumerate(posts):
    #             self.assertEqual(post['id'], response_without_pagination[(i * REST_FRAMEWORK['PAGE_SIZE']) + j]['id'])
    #         i += 1

    def test_rate_view_create_correctly(self):
        new_post = PostFactory()
        data = {}
        data['vote'] = Rating.LIKE_VALUE
        request = self.factory.put("api/posts/{id}/rate", data)
        force_authenticate(request, user=self.user)
        response = self.rate_view(request, pk=new_post.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, new_post.get_rating())


    def test_rate_view_update_correctly(self):
        new_post = PostFactory()
        RatingFactory(content_object=new_post, value=Rating.LIKE_VALUE)
        data = {}
        data['vote'] = Rating.LIKE_VALUE
        request = self.factory.put("api/posts/{id}/rate", data)
        force_authenticate(request, user=self.user)
        response = self.rate_view(request, pk=new_post.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, new_post.get_rating())

    def test_trending_view_returns_highly_rated_new_posts_first(self):
        low_post = PostFactory()
        RatingFactory.create_batch(3, content_object=low_post, value=Rating.LIKE_VALUE)

        middle_post = PostFactory()
        RatingFactory.create_batch(7, content_object=middle_post , value=Rating.LIKE_VALUE)

        high_post = PostFactory()
        RatingFactory.create_batch(50, content_object=high_post , value=Rating.LIKE_VALUE)

        request = self.factory.get("api/posts/trending/")
        force_authenticate(request, self.user)
        response = self.trending_view(request)

        posts = response.data

        self.assertEqual(posts[0]["id"], high_post.id)
        self.assertEqual(posts[1]["id"], middle_post.id)
        self.assertEqual(posts[2]["id"], low_post.id)

    def test_trending_returns_earlier_post_when_equal_ratings(self):
        low_post = PostFactory()
        middle_post = PostFactory()
        high_post = PostFactory()
        for i in range(50):
            RatingFactory(content_object=low_post, value=Rating.LIKE_VALUE)
            RatingFactory(content_object=middle_post, value=Rating.LIKE_VALUE)
            RatingFactory(content_object=high_post, value=Rating.LIKE_VALUE)

        low_post.created_at = timezone.now() - timedelta(hours=20)
        low_post.save()
        middle_post.created_at = timezone.now() - timedelta(hours=10)
        middle_post.save()
        high_post.created_at = timezone.now() - timedelta(hours=3)
        high_post.save()

        request = self.factory.get("api/posts/trending/")
        force_authenticate(request, self.user)
        response = self.trending_view(request)

        posts = response.data

        self.assertEqual(posts[0]["id"], high_post.id)
        self.assertEqual(posts[1]["id"], middle_post.id)
        self.assertEqual(posts[2]["id"], low_post.id)

    def test_post_detail_serializer_return_rating(self):
        new_post = PostFactory()
        RatingFactory(content_object=new_post, user=self.user, value=Rating.LIKE_VALUE)
        request = self.factory.get("api/posts/{id}/")
        force_authenticate(request, user=self.user)
        response = self.detail_view(request, pk=new_post.id)
        self.assertEqual(response.data['user_rating']['value'], 1)
