# Imported from Django.
from django.test import TestCase
from datetime import date

# Imported from Factory-Boy.
from factory.fuzzy import (
    FuzzyText,
    FuzzyInteger,
)

# Models.
from catalog.models import Book

# Serializers.
from catalog.serializers import BookSerializerIn

# Factories.
from catalog.factories import GenreFactory


class BookSerializerInTestCase(TestCase):

    def test_book_serializer_creation(self):
        genre = [GenreFactory() for i in range(2, 4)]
        data = {
            'title': FuzzyText().fuzz(),
            'summary': FuzzyText().fuzz(),
            'isbn': FuzzyInteger(8, 16).fuzz(),
            'publish_year': date.today(),
            'original_language': 'EN',
            'genre': genre
        }

        serializer = BookSerializerIn(data=data)

        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertTrue(Book.objects.filter(title=data['title']).exists())

