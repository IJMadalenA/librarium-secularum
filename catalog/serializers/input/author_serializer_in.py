# Imported from Rest-Framework.
from rest_framework import serializers

# Models.
from catalog.models import Author


class AuthorSerializerIn(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_death',
        )