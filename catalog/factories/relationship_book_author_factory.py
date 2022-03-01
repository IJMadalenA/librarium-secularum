# Imported from Factory-Boy.
from factory.django import DjangoModelFactory
from factory import SubFactory

# Models.
from catalog.models import RelationshipBookAuthor

# Factories.
from catalog.factories import (
	AuthorFactory,
	BookFactory
)


class RelationshipBookAuthorFactory(DjangoModelFactory):
	
	class Meta:
		model = RelationshipBookAuthor
		
	book = SubFactory(BookFactory)
	author = SubFactory(AuthorFactory)
