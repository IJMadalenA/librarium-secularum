# Imported from Rest-Framework.
from rest_framework.serializers import (
	ModelSerializer,
	CharField,
	DateField,
)

# Models imported.
from catalog.models import Author

# Serializers imported.


class AuthorBasicSerializerOut(ModelSerializer):
	
	class Meta:
		model = Author
		fields = (
			"first_name",
			"last_name",
			"Pseudonymous",
		)


class AuthorSerializerOut(AuthorBasicSerializerOut):
	# To avoid a circular import, the "BookBasicSerializerOut" is imported directly
	# inside the serializer that uses it.
	from catalog.serializers.output.book_serializer_out import BookBasicSerializerOut

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
	)
	date_of_death = DateField(
		allow_null=True,
	)
	nationality = CharField(
		allow_blank=False,
		allow_null=False,
	)
	mother_tongue = CharField(
		allow_blank=True,
		allow_null=False,
		max_length=2,
	)
	books = BookBasicSerializerOut(
		allow_null=True,
		many=True,
		partial=True,
		read_only=True,
	)
