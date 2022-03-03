# Imported from Django.
from django.test import TestCase

# Factories.
from catalog.factories import BookFactory

# Models.
from catalog.models import Book


class BookModelTestCase(TestCase):

    def test_book_model(self):
        before_create = Book.objects.count()
        book = BookFactory()
        self.assertTrue(Book.objects.filter(id=book.id).exists())
        self.assertEqual(Book.objects.count(), before_create + 1)
