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

        self.factory = APIRequestFactory()
        self.create_view = UserViewSet.as_view({'post': 'create'})
        self.follow_view = UserViewSet.as_view({'put': 'follow'})

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

    def test_user_follow_other_user(self):
        u = UserFactory() # toni
        u1 = UserFactory() # yasen
        data={}
        data['followed'] = u1.id
        request = self.factory.put("api/users/follow", data)
        force_authenticate(request, user=u)
        response = self.follow_view(request)
        self.assertIn(u.id, u1.get_followers_ids())

    # def test_follow_connection_is_created(self):
    #     u = UserFactory()
    #     u1 = UserFactory()
    #     data={}
    #     data['follower'] = u.id
    #     data['followed'] = u1.id
    #     request = self.factory.put("api/users", data)
    #     response = self.follow_view(request)
    #
    #     print('boc------->' + str(response.data))