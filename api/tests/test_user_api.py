from django.test import TestCase
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.test import APIRequestFactory, force_authenticate

from api.factories import UserFactory
from api.models import User
from api.serializers import UserSerializer
from api.views.users import UserViewSet


class UserApiTest(TestCase):
    def setUp(self):
        self.user = UserFactory.build()
        self.jsonUser = UserSerializer(self.user).data
        self.jsonUser['password'] = 'test123'
        self.jsonUser['password_confirmation'] = 'test123'

        self.factory = APIRequestFactory()
        self.create_view = UserViewSet.as_view({'post': 'create'})
        self.follow_view = UserViewSet.as_view({'put': 'follow'})
        self.unfollow_view = UserViewSet.as_view({'put': 'unfollow'})

    def test_password_not_readable(self):
        request = self.factory.post('/api/users/', self.jsonUser, format='json')
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('password', response.data)

    def test_password_saves_as_hash(self):
        request = self.factory.post('/api/users/', self.jsonUser, format='json')
        force_authenticate(request, user=self.user)

        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_user = User.objects.get(pk=response.data['id'])

        self.assertNotEqual(self.jsonUser['password'], new_user.password)
        self.assertTrue(new_user.check_password(self.jsonUser['password']))

    def test_user_follow_other_user(self):
        u = UserFactory() # toni
        u1 = UserFactory() # yasen
        data={}
        data['followed'] = u1.id
        request = self.factory.put("api/users/follow", data)
        force_authenticate(request, user=u)
        response = self.follow_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(u.id, u1.get_followers_ids())

    def test_user_unfollow_other_user(self):
        u = UserFactory()  # toni
        u1 = UserFactory()  # yasen
        u.followers.add(u1)
        u.save()
        data={}
        data['followed'] = u1.id
        request = self.factory.put("api/users/unfollow", data)
        force_authenticate(request, user=u)
        response = self.unfollow_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(u.id, u1.get_followers_ids())