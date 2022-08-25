# Imported from Django.
from django.urls import reverse
import datetime

# Imported from Factory-Boy.
from factory.fuzzy import (
    FuzzyText,
    FuzzyDate,
    FuzzyChoice
)
from factory import SubFactory
from rest_framework.test import APITestCase

# Imported from Rest-Framework.
from rest_framework import status

# Factories.
from catalog.factories.author_factory import AuthorFactory
from catalog.factories.book_factory import BookFactory

# Models.
from catalog.models import Author


class AddAuthorTestCase(APITestCase):
    endpoint_name = "add-author"

    def setUp(self):
        super().setUp()
        self.url = reverse(self.endpoint_name)

        self.body = {
            "first_name": FuzzyText().fuzz(),
            "last_name": FuzzyText().fuzz(),
            "pseudonymous": FuzzyText().fuzz(),
            "date_of_birth": FuzzyDate(datetime.date(1800, 1, 1)),
            "date_of_death": FuzzyDate(datetime.date(2022, 1, 1)),
            "nationality": FuzzyChoice().fuzz(),
            "mother_tongue": FuzzyChoice(["EN", "FR", "ES"]).fuzz(),
            "books": SubFactory(BookFactory)
        }

    def test_add_author(self):
        for i in range(2, 4):
            AuthorFactory()

        before_count = Author.objects.count()

        response = self.client.post(self.url, self.body, follow="jason")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
