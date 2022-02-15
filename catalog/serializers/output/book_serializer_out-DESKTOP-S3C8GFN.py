# Imported from Rest-Framework.
from rest_framework.serializers import ModelSerializer
from .book_serializer_out import BookSerializerOut

# Model.
from catalog.models import Author


class AuthorSerializerOut(ModelSerializer):
    author = AuthorSerializerOut(many=True)

    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
        )