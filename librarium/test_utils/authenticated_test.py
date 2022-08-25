from rest_framework.test import APITestCase
from django.urls import reverse

# Factories imported.
from core.factories.user_factory import UserFactory

from factory.fuzzy import (
    FuzzyText,
    FuzzyInteger,
    FuzzyChoice,
    FuzzyFloat,
)
from rest_framework import status


class AuthenticatedApiTestCase(APITestCase):
    """
    This class help us to authenticate the requests of the endpoint, to can test the views.
    The objective is to inherit from this class, which will be in charge of authenticating the calls.
    """

    endpoint_name = None
    kwargs = None
    args = None

    def setUp(self) -> None:
        self.password = '123456'
        self.user = UserFactory(password=self.password)

        self.kwargs = None
        self.args = None

        if self.endpoint_name is not None:
            self.url = reverse(self.endpoint_name, args=self.args, kwargs=self.kwargs)

        login_body = {
            'username': self.user.username,
            'password': self.password
        }
        login_url = reverse('token_obtain_pair')
        self.user_token = self.client.post(login_url, login_body, format='json').data.get('access', None)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')

    def forbidden_client(self):
        self.client.credentials(HTTP_AUTHORIZATION='')