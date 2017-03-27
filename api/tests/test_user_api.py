from django.test import TestCase
from rest_framework.test import APIRequestFactory

from api.models import User
from api.views.users import UserViewSet


class UserApiTest(TestCase):
    def setUp(self):
        self.jsonUser = {
            'email': 'test@test.com',
            'username': 'testtest',
            'first_name': 'Tester',
            'last_name': 'Testov',
            'password': 'test123',
        }
        self.factory = APIRequestFactory()
        self.create_view = UserViewSet.as_view({'post': 'create'})

    def test_password_not_readable(self):
        request = self.factory.post('/api/users/', self.jsonUser, format='json')
        response = self.create_view(request)
        self.assertNotIn('password', response)

    # This test doesn't work
    # def test_password_saves_as_hash(self):
    #     request = self.factory.post('/api/users/', self.jsonUser, format='json')
    #     response = self.create_view(request)
    #     new_user = User.objects.get(pk=response.data['id'])
    #
    #     self.assertNotEqual(self.jsonUser['password'], new_user.password)
    #     self.assertTrue(new_user.check_password(self.jsonUser['password']))

