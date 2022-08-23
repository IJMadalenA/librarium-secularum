# Imported from Rest-Framework.
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    DateField,
)

# Models imported.
from catalog.models import Author

# Serializers imported.
from catalog.serializers.input import BookSerializerIn


class AuthorSerializerIn(ModelSerializer):

    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "pseudonymous",
            "date_of_birth",
            "date_of_death",
            "nationality",
            "mother_tongue",
            "books",
        )

    first_name = CharField(
        max_length=64,
        allow_blank=False,
        allow_null=False,
        required=True,
    )
    last_name = CharField(
        max_length=64,
        allow_blank=False,
        allow_null=False,
        required=True,
    )
    pseudonymous = CharField(
        max_length=64,
        allow_blank=False,
        allow_null=False,
        required=True,
    )
    date_of_birth = DateField(
        required=True,
        allow_null=False,
    )
    date_of_death = DateField(
        required=True,
        allow_null=False,
    )
    # nationalitu = serializers.CharField()
    mother_tongue = CharField(
        max_length=2,
        allow_null=True,
        allow_blank=True,
    )
    book = BookSerializerIn(
        many=True,
        allow_null=False,
        required=True,
    )
