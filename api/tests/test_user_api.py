from django.test import TestCase
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
        self.follow_view = UserViewSet.as_view({'user': 'follow'})
        self.me_view = UserViewSet.as_view({'get': 'me'})

    def test_password_not_readable(self):
        request = self.factory.post('/api/users/', self.jsonUser, format='json')
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertNotIn('password', response.data)

    def test_password_saves_as_hash(self):
        request = self.factory.post('/api/users/', self.jsonUser, format='json')
        force_authenticate(request, user=self.user)

        response = self.create_view(request)
        new_user = User.objects.get(pk=response.data['id'])

        self.assertNotEqual(self.jsonUser['password'], new_user.password)
        self.assertTrue(new_user.check_password(self.jsonUser['password']))

    def test_me_route_returns_current_user(self):
        self.user.save()

        request = self.factory.get('/api/users/me')
        force_authenticate(request, user=self.user)
        response = self.me_view(request)
        returned_user = response.data

        self.assertEqual(self.user.username, returned_user['username'])


