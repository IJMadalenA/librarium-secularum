# Imported from Django.
from django.db import models


class Genre(models.Model):
	name = models.CharField(
		max_length=64,
		null=False,
		blank=False,
	)
	books = models.ManyToManyField(
		'Book'
	)
	
	def __str__(self):
		return self.name
