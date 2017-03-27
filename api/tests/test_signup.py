from django.test import TestCase
from api.views.signup import signup
from rest_framework.test import APIRequestFactory

from api import factories
from api.serializers import UserSerializer


class SignupTest(TestCase):
    PASSWORD = 'test'
    REQUIRED_FIELD_ERROR = 'This field is required.'

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

    def test_signup_returns_errors_on_missing_required_fields(self):
        request = self.factory.post('/api/signup/', {}, format='json')
        response = signup(request)

        data = response.data
        print(data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['username'])
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['password'])
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['email'])
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['first_name'])
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['last_name'])
