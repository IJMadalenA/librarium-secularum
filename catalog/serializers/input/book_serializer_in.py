# Imported from Rest-Framework.
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    DateField,
)
from rest_framework.validators import UniqueValidator

# Serializers imported.
from catalog.serializers.input.author_serializer_in import AuthorSerializerIn
from catalog.serializers.input.genre_serializer_in import GenreSerializerIn

# Models.
from catalog.models import Book


class BookSerializerIn(ModelSerializer):

    class Meta:
        model = Book
        fields = (
            "title",
            "summary",
            "isbn",
            "publish_year",
            "original_language",
            "genres",
            "authors",
        )

    title = CharField(
        max_length=128,
        required=True,
        allow_blank=False,
        allow_null=False,
    )
    summary = CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    isbn = CharField(
        max_length=16,
        required=True,
        allow_blank=False,
        allow_null=False,
        validators=[UniqueValidator(queryset=Book.objects.all())]
    )
    publish_year = DateField(
        required=False,
        allow_null=True,
    )
    original_language = CharField(
        max_length=16,
        required=True,
        allow_blank=False,
        allow_null=False,
    )
    genres = GenreSerializerIn(
        many=True,
        required=True,
        allow_null=False,
        partial=True,
    )
    authors = AuthorSerializerIn(
        many=True,
        required=True,
        partial=True,
        allow_null=True,
    )
