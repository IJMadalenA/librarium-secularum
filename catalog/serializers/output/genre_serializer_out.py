# Imported from Rest-Framework.
from rest_framework import ModelSerializer

# Models.
from catalog.models.genre import Genre


class GenreSerializerOut(ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'name',
        )
