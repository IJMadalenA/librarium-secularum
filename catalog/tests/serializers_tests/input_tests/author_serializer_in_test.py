# Imported from Django.
import datetime
from django.test import TestCase

# Imported from Factory-Boy.
from factory.fuzzy import (
    FuzzyText,
    FuzzyDate,
)

# Models.
from catalog.models import Author

# Serializers.
from catalog.serializers import AuthorSerializerIn


class AuthorSerializerInTestCase(TestCase):

    def test_author_serializer_creation(self):
        data = {
            'first_name': FuzzyText().fuzz(),
            'last_name': FuzzyText().fuzz(),
            'date_of_birth': FuzzyDate(datetime.date(1800, 1, 1)).fuzz(),
            'date_of_death': FuzzyDate(datetime.date(2008, 1, 1)).fuzz(),
        }

        serializer = AuthorSerializerIn(data=data)

        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertTrue(Author.objects.filter(first_name=data['first_name']).exists())
