from django.test import TestCase
from api.views.signup import signup
from rest_framework.test import APIRequestFactory


class SignupTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_signup_works(self):
        correctUser = {
            'username': 'frostblooded',
            'email': 'frostblooded@yahoo.com',
            'password': 'testtest',
            'password_confirmation': 'testtest',
            'first_name': 'nikolay',
            'last_name': 'danailov'
        }

        request = self.factory.post('/api/signup/', correctUser, format='json')
        response = signup(request)

        user = response.data
        self.assertEqual(correctUser['username'], user.username)
        self.assertEqual(correctUser['email'], user.email)
        self.assertEqual(correctUser['first_name'], user.first_name)
        self.assertEqual(correctUser['last_name'], user.last_name)
