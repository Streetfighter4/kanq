from django.test import TestCase
from rest_framework.authtoken.models import Token

from api.factories import UserFactory


class UserModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_user_has_token(self):
        self.assertIsNotNone(Token.objects.get(user=self.user))