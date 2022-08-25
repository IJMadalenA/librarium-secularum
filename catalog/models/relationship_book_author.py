# Imported from Django.
from django.db import models

# Models.
from .book import Book
from .author import Author


class RelationshipBookAuthor(models.Model):
	book = models.ForeignKey(
		Book,
		null=False,
		blank=False,
		on_delete=models.CASCADE
	)
	author = models.ForeignKey(
		Author,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
	)
	
	def __str__(self):
		return f"{self.book}, {self.author.first_name} {self.author.last_name}"
