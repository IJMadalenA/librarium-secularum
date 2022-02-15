# Imported from Django.
from django.test import TestCase

# Models Imported.
from catalog.models import Book

# Factories Imported.
from catalog.factories import BookFactory


class BookFactoryTestCase(TestCase):
	
	def test_book_creation(self):
		for i in range(2):
			BookFactory()
		
		before_author_creation_num = Book.objects.all().count()
		book = BookFactory()
		
		self.assertTrue(Book.objects.get(id=book.id))
		self.assertEqual(before_author_creation_num, Book.objects.all().count() - 1)
