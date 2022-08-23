# Imported from Rest-Framework.
from rest_framework.serializers import (
	ModelSerializer,
	CharField,
	DateField,
)

# Models imported.
from catalog.models import Author

# Serializers imported.
from catalog.serializers.output.book_serializer_out import BookBasicSerializerOut


class AuthorBasicSerializerOut(ModelSerializer):
	
	class Meta:
		model = Author
		fields = (
			'first_name',
			'last_name',
			'Pseudonymous',
		)


class AuthorSerializerOut(AuthorBasicSerializerOut):

	class Meta:
		model = Author
		fields = AuthorBasicSerializerOut.Meta.fields + (
			"date_of_birth",
			"date_of_death",
			"nationality",
			"mother_tongue",
			"books",
		)

	date_of_birth = DateField(
		allow_null=False,
		required=True,
	)
	date_of_death = DateField(
		allow_null=True,
		required=False,
	)
	nationality = CharField(
		allow_blank=False,
		allow_null=False,
		required=True,
	)
	mother_tongue = CharField(
		allow_blank=True,
		allow_null=False,
		max_length=2,
		required=True,
	)
	books = BookBasicSerializerOut(
		allow_null=True,
		many=True,
		partial=True,
		read_only=True,
		required=True,
	)
