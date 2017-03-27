from django.test import TestCase
from api.views.signup import signup
from rest_framework.test import APIRequestFactory

from api import factories
from api.models import User


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
            password=self.PASSWORD,
            email='test@test.com',
            username='ivan.ivanov'
        )
        correct_user.password_confirmation = self.PASSWORD

        request = self.factory.post('/api/signup/', correct_user, format='json')
        response = signup(request)

        user = response.data
        self.assertEqual(correct_user['username'], user.username)
        self.assertEqual(correct_user['email'], user.email)
        self.assertEqual(correct_user['first_name'], user.first_name)
        self.assertEqual(correct_user['last_name'], user.last_name)
