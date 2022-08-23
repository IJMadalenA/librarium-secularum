# Imported from Rest-Framework.
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)

# Models imported.
from catalog.models.publisher import Publisher


class PublisherSerializerIn(ModelSerializer):

    class Meta:
        model = Publisher
        fields = (
            "name",
            "country",
        )

    name = CharField(
        allow_blank=False,
        allow_null=False,
        max_length=64,
        required=True,
    )
    country = CharField(
        allow_blank=False,
        allow_null=False,
        max_length=128,
        required=True,
    )
