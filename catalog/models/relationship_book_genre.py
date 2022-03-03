# Imported from Django.
from django.db import models

# Models.
from .book import Book
from .genre import Genre


class RelationshipBookGenre(models.Model):
    book = models.ForeignKey(
        Book,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.book}, {self.genre.name}'
