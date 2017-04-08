from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from api import factories
from api.serializers import UserSerializer
from api.views.users import UserViewSet


class SignupTest(TestCase):
    PASSWORD = 'test'
    REQUIRED_FIELD_ERROR = 'This field is required.'

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = factories.UserFactory.build()
        self.signup = UserViewSet.as_view({'post': 'create'})

    def test_signup_works(self):
        serializer = UserSerializer(self.user)
        request_data = serializer.data
        request_data['password'] = self.PASSWORD
        request_data['password_confirmation'] = self.PASSWORD

        request = self.factory.post('/api/users/', request_data, format='json')
        response = self.signup(request)

        new_user = response.data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(new_user['username'], self.user.username)
        self.assertEqual(new_user['email'], self.user.email)
        self.assertEqual(new_user['first_name'], self.user.first_name)
        self.assertEqual(new_user['last_name'], self.user.last_name)

    def test_signup_returns_errors_on_invalid_input(self):
        # This test checks if the API returns an error
        # if the input data is invalid. Required fields
        # are used only as an example
        request = self.factory.post('/api/signup/', {}, format='json')
        response = self.signup(request)

        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['username'])
        self.assertTrue(self.REQUIRED_FIELD_ERROR in data['password'])
