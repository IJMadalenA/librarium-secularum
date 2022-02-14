# Imported from Factory-Boy.
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from factory.fuzzy import FuzzyDate

# Models.
from catalog.models import Book

# Utils.
import datetime


class BookFactory(DjangoModelFactory):
	
	class Meta:
		model = Book
		
		