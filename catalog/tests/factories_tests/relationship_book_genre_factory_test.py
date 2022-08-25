# Imported from Django.
from django.test import TestCase

# Models imported.
from catalog.models import RelationshipBookGenre

# Factories imported.
from catalog.factories import RelationshipBookGenreFactory


class RelationshipBookGenreTestCase(TestCase):

    def test_relationship_book_genre_creation(self):

        for i in range(2):
            RelationshipBookGenreFactory()

        before_relationship_creation_num = RelationshipBookGenre.objects.all().count()
        relationship = RelationshipBookGenreFactory()

        self.assertTrue(RelationshipBookGenre.objects.get(id=relationship.id))
        self.assertEqual(RelationshipBookGenre.objects.all().count(), before_relationship_creation_num + 1)
