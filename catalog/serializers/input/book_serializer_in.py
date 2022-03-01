# Imported from Rest-Framework.
from rest_framework.serializers import ModelSerializer
from .genre_serializer_in import GenreSerializerIn

# Models.
from catalog.models import Book


class BookSerializerIn(ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title',
            'summary',
            'isbn',
            'publish_year',
            'original_language',
        )
