# Imported from Factory-Boy.
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from factory.fuzzy import FuzzyDate

# Models.
from catalog.models import Author

# Utils.
import datetime


class AuthorFactory(DjangoModelFactory):
	
	class Meta:
		model = Author
		
	first_name = FuzzyText()
	last_name = FuzzyText()
	date_of_birth = FuzzyDate(
		datetime.date(2000, 1, 1)
	)
	date_of_death = FuzzyDate(
		datetime.date(2000, 1, 1)
	)
