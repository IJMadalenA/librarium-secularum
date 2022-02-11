# Imported from Rest-Framework.
from rest_framework import serializer
from .genre_serializer_in import GenreSerializerIn

# Models.
from catalog.models import Book


class BookSerializerIn(serializers.ModelSerializer):
    genre = GenreSerializerIn(many=True)

    class Meta:
        model = Book
        fields = (
            'title',
            'summary',
            'isbn',
            'publish_year',
            'language',
            'genre',
        )
