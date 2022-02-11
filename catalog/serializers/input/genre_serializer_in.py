# Imported from Rest-Framework.
from rest_framework.serializers import ModelSerializer

# Models.
from catalog.models.genre import Genre


class GenreSerializerIn(ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'name',
        )
