# Imported from Rest-Framework.
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)

# Models imported.
from catalog.models.genre import Genre


class GenreSerializerIn(ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            "name",
        )

    name = CharField(
        max_length=64,
        allow_blank=False,
        allow_null=False,
        required=True,
    )
