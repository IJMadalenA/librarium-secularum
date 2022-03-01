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


class BookFactory(DjangoModelFactory):

	class Meta:
		model = Book
		
	title = FuzzyText()
	summary = FuzzyText()
	isbn = FuzzyInteger(
		10, 1000
	)
	publish_year = FuzzyDate(
		datetime.date(2000, 1, 1)
	)
	original_language = FuzzyChoice(
		LANGUAGE_CHOICE
	)
	author = SubFactory(AuthorFactory)