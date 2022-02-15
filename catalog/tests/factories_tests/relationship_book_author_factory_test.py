# imported from Django.
from django.test import TestCase

# Models imported.
from catalog.models import RelationshipBookAuthor

# Factories imported.
from catalog.factories import RelationshipBookAuthorFactory


class RelationshipBookAuthorTestCase(TestCase):
	
	def test_relationship_book_author_creation(self):
		
		for i in range(2):
			RelationshipBookAuthorFactory()
			
		before_relationship_creation_num = RelationshipBookAuthor.objects.all().count()
		relationship = RelationshipBookAuthorFactory()
		
		self.assertTrue(RelationshipBookAuthor.objects.get(id=relationship.id))
		self.assertEqual(RelationshipBookAuthor.objects.all().count(), before_relationship_creation_num + 1)
