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

    def test_signup_works(self):
        # correct_user = factories.UserFactory()
        # correct_user.password = 'test'
        # correct_user.password_confirmation = 'test'

        correct_user = User(
            first_name='Ivan',
            last_name='Ivanov',
            # password=self.PASSWORD,
            email='test@test.com',
            username='ivan.ivanov'
        )
        # correct_user.password_confirmation = self.PASSWORD
        serializer = UserSerializer(correct_user)
        request_data = serializer.data
        request_data['password'] = self.PASSWORD
        request_data['password_confirmation'] = self.PASSWORD

        request = self.factory.post('/api/signup/', request_data, format='json')
        response = signup(request)

        user = response.data
        self.assertEqual(user['username'], correct_user.username)
        self.assertEqual(user['email'], correct_user.email)
        self.assertEqual(user['first_name'], correct_user.first_name)
        self.assertEqual(user['last_name'], correct_user.last_name)
