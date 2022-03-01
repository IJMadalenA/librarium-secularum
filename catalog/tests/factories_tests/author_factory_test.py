# Imported from Django.
from django.test import TestCase

# Models imported.
from catalog.models import Author

# Factories imported.
from catalog.factories import AuthorFactory


class AuthorFactoryTestCase(TestCase):
	
	def test_author_factory(self):
		
		for i in range(2):
			AuthorFactory()
			
		authors_num_before_create = Author.objects.all().count()
		author = AuthorFactory()
		
		# Creating authors.
		self.assertEqual(author, Author.objects.get(id=author.id))