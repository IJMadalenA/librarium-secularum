# Imported from Django.
from django.db import models

# Models.
from .genre import Genre

# List of languages.
from .languaje import LANGUAGE_CHOICE


class Book(models.Model):
	title = models.CharField(
		max_length=128,
		null=False,
		blank=False,
	)
	summary = models.TextField(
		null=True,
		blank=True,
	)
	isbn = models.CharField(
		'ISBN',
		unique=True,
		max_length=16,
		null=False,
		blank=False,
	)
	publish_year = models.DateField(
		blank=True,
		null=True,
	)
	original_language = models.CharField(
		choices=LANGUAGE_CHOICE,
		blank=False,
		null=False,
		max_length=16
	)
	genre = models.ManyToManyField(
		Genre,
	)
	authors = models.ManyToManyField(
		'Author',
		through='RelationshipBookAuthor',
	)
	
	def __str__(self):
		return f'{self.title}'
	
	
class Meta:
	ordering = ['title']
