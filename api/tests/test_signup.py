from django.test import TestCase
from api.views.signup import signup
from rest_framework.test import APIRequestFactory

from api import factories, serializers
from api.models import User
from api.serializers import UserSerializer


class SignupTest(TestCase):
    PASSWORD = 'test'

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = factories.UserFactory.build()

    def test_signup_works(self):
        serializer = UserSerializer(self.user)
        request_data = serializer.data
        request_data['password'] = self.PASSWORD
        request_data['password_confirmation'] = self.PASSWORD

        request = self.factory.post('/api/signup/', request_data, format='json')
        response = signup(request)

        new_user = response.data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(new_user.username, self.user.username)
        self.assertEqual(new_user.email, self.user.email)
        self.assertEqual(new_user.first_name, self.user.first_name)
        self.assertEqual(new_user.last_name, self.user.last_name)
