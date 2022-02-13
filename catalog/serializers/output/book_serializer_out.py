# Imported from Rest-Framework.
from rest_framework.serializers import ModelSerializer

# Models.
from catalog.models.book import Book


class BookSerializerOut(ModelSerializer):
	
	class Meta:
		model = Book
		fields = (
			'first_name',
			'last_name',
		)
