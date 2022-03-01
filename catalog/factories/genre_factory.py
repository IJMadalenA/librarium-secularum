# Imported from Factory-Boy
from factory.django import DjangoModelFactory
from factory.fuzzy import (
	FuzzyText,
)

# Models.
from catalog.models import Genre


class GenreFactory(DjangoModelFactory):
	
	class Meta:
		model = Genre
		
	name = FuzzyText()