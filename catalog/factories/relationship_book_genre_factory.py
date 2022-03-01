# Imported from Factory-Boy.
from factory.django import DjangoModelFactory
from factory import SubFactory

# Models.
from catalog.models import RelationshipBookGenre

# Factories.
from catalog.factories import (
    GenreFactory,
    BookFactory
)


class RelationshipBookGenreFactory(DjangoModelFactory):

    class Meta:
        model = RelationshipBookGenre

    book = SubFactory(BookFactory)
    genre = SubFactory(GenreFactory)
