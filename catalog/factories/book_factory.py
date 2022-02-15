# Imported from Factory-Boy.
from factory.django import DjangoModelFactory
from factory.fuzzy import (
	FuzzyText,
	FuzzyDate,
	FuzzyInteger,
	FuzzyChoice,
)
from factory import SubFactory

# Models.
from catalog.models import Book

# Utils.
import datetime

# Lists imported.
from catalog.models.languaje import LANGUAGE_CHOICE

# Factories.
from catalog.factories.author_factory import AuthorFactory
from catalog.factories.genre_factory import GenreFactory


class BookFactory(DjangoModelFactory):
	
	class Meta:
		model = Book
		
	title = FuzzyText()
	summary = FuzzyText()
	isbn = FuzzyInteger(
		1, 16
	)
	publish_year = FuzzyDate(
		datetime.date(2000, 1, 1)
	)
	original_language = FuzzyChoice(
		LANGUAGE_CHOICE
	)