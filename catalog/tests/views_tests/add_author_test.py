# Imported from Django.
from django.urls import reverse
import datetime

# Imported from Factory-Boy.
from factory.fuzzy import FuzzyText, FuzzyDate
from rest_framework.test import APITestCase

# Imported from Rest-Framework.
from rest_framework import status

# Factories.
from catalog.factories import AuthorFactory

# Models.
from catalog.models import Author


class AddAuthorTestCase(APITestCase):
    endpoint_name = 'add-author'

    def setUp(self):
        super().setUp()
        self.url = reverse(self.endpoint_name)

        self.body = {
            'first_name': FuzzyText().fuzz(),
            'last_name': FuzzyText().fuzz(),
            'date_of_birth': FuzzyDate(datetime.date(1800, 1, 1)),
            'date_of_death': FuzzyDate(datetime.date(2022, 1, 1)),
        }

    def test_add_author(self):
        for i in range(2, 4):
            AuthorFactory()

        before_count = Author.objects.count()

        response = self.client.post(self.url, self.body, follow='jason')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
