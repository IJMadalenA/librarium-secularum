# Imported from Django.
from django.test import TestCase

# Factories.
from catalog.factories import AuthorFactory

# Models.
from catalog.models import Author


class AuthorModelTestCase(TestCase):
	
	def test_author_model(self):
		before_create = Author.objects.count()
		author = AuthorFactory()
		self.assertEqual(Author.objects.count(), before_create + 1)