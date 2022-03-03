# Imported from Django.
from django.test import TestCase

# Imported from Factory-Boy
from factory.fuzzy import (
    FuzzyText,
    FuzzyInteger,
)

# Models.
from catalog.models import Genre

# Serializers.
from catalog.serializers import GenreSerializerIn


class GenreSerializerInTestCase(TestCase):

    def test_genre_serializer_creation(self):
        data = {
            'name': FuzzyText().fuzz()
        }

        serializer = GenreSerializerIn(data=data)

        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertTrue(Genre.objects.filter(name=data['name']).exists())
