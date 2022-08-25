# Imported from Django.
from django.db import models

# Imported from django_countries.
from django_countries.fields import CountryField
# https://pypi.org/project/django-countries/

# List of languages.
from .languaje import LANGUAGE_CHOICE


class Author(models.Model):
	first_name = models.CharField(
		blank=False,
		max_length=64,
		null=False,
	)
	last_name = models.CharField(
		blank=True,
		max_length=64,
		null=True,
	)
	pseudonymous = models.CharField(
		blank=True,
		max_length=64,
		null=True,
	)
	date_of_birth = models.DateField(
		blank=False,
		null=False,
	)
	date_of_death = models.DateField(
		blank=True,
		null=True,
	)
	nationality = CountryField(
		blank_label="(select country)",
		blank=False,
		null=False,
	)
	mother_tongue = models.CharField(
		blank=True,
		choices=LANGUAGE_CHOICE,
		max_length=2,
		null=True,
	)
	books = models.ManyToManyField(
		"Book",
		through="RelationshipBookAuthor",
	)
	
	# To Do: create a field "genre". It will be a ManyToMany field.
	
	class Meta:
		ordering = ["last_name", "first_name"]
	
	def __str__(self):
		return f"{self.last_name}, {self.first_name}"
