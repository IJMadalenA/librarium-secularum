# Imported from Django.
from django.db import models


class Genre(models.Model):
	name = models.CharField(
		max_length=64,
		null=False,
		blank=False,
	)
	
	def __str__(self):
		return self.name
