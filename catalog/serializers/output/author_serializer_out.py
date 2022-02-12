# Imported from Rest-Framework.
from rest_framework.serializers import ModelSerializer

# Models.
from catalog.models import Author


class AuthorSerializerOut(ModelSerializer):
	
	class Meta:
		model = Author
		fields = (
			'first_name',
			'last_name',
			'Pseudonymous',
			'date_of_birth',
			'nationality',
			'mother_tongue',
			'books',
		)