# imported from Django.
from django.test import TestCase

# Models imported.
from catalog.models import Genre

# Factories imported.
from catalog.factories import GenreFactory


class GenreFactoryTestCase(TestCase):
	
	def test_genre_creation(self):
		
		for i in range(2):
			GenreFactory()
			
		before_genre_creation_num = Genre.objects.all().count()
		genre = GenreFactory()
		
		# Creating genre test.
		self.assertNotEqual(before_genre_creation_num, Genre.objects.all().count())
		self.assertEqual(before_genre_creation_num + 1, Genre.objects.all().count())
		self.assertEqual(genre.id, Genre.objects.get(id=genre.id).id)
