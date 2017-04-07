from django.test import TestCase
from api.helpers import user_service

from api.factories import UserFactory, PostFactory


class UserServiceTest(TestCase):
    POSTS_PER_USER = 10

    def setUp(self):
        self.main_user = UserFactory()
        self.follower = UserFactory()
        self.test_user = UserFactory()
        self.main_user.followers.add(self.follower)
        self.follower.following.add(self.main_user)

        for i in range(0, self.POSTS_PER_USER):
            PostFactory(creator=self.main_user)
            PostFactory(creator=self.test_user)
            PostFactory(creator=self.follower)

    def test_user_feed_returns_posts_from_correct_users(self):
        posts = user_service.get_user_feed(self.follower.id, 0, 20)

        self.assertEqual(len(posts), self.POSTS_PER_USER * 2)
        for post in posts:
            self.assertIn(post.creator_id, [self.main_user.id, self.follower.id])

    def test_user_feed_returns_posts_ordered_correctly(self):
        posts = user_service.get_user_feed(self.follower.id, 0, 20)

        for i in range(0, len(posts) - 1):
            self.assertGreater(posts[i].created_at, posts[i + 1].created_at)

    def test_user_feed_returns_correct_pages(self):
        pass
