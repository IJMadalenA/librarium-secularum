# Imported from Rest-Framework.
from rest_framework.serializers import (
	ModelSerializer,
	CharField,
	DateField,
)
from rest_framework.validators import UniqueValidator

# Models.
from catalog.models.book import Book

# Serializers imported.
from catalog.serializers.output import AuthorBasicSerializerOut
from catalog.serializers.output import GenreSerializerOut


class BookBasicSerializerOut(ModelSerializer):

	class Meta:
		model = Book
		fields = (
			"title",
			"summary",
			"publish_year",
			"genres",
			"authors",
		)

	title = CharField(
		allow_blank=False,
		allow_null=False,
		max_length=128,
		required=True,
		read_only=True,
	)
	summary = CharField(
		allow_blank=True,
		allow_null=True,
		required=False,
		read_only=True
	)
	publish_year = DateField(
		allow_null=True,
		read_only=True,
		required=False,
	)
	genres = GenreSerializerOut(
		allow_null=True,
		many=True,
		partial=True,
		required=True,
		read_only=True,
	)
	authors = AuthorBasicSerializerOut(
		allow_null=True,
		many=True,
		partial=True,
		required=True,
		read_only=True,
	)


class BookSerializerOut(BookBasicSerializerOut):

	class Meta:
		model = Book
		fields = BookBasicSerializerOut.Meta.fields + (
			"isbn",
			"original_language",
		)

	isbn = CharField(
		allow_blank=False,
		allow_null=False,
		required=True,
		max_length=16,
		read_only=True,
		validators=[UniqueValidator(queryset=Book.objects.all())]
	)
	original_language = CharField(
		allow_blank=False,
		allow_null=False,
		required=True,
		max_length=16,
		read_only=True,
	)
