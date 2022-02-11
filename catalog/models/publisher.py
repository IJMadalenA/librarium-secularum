# Imported from Django.
from django.db import models


class Publisher(models.Model):
	name = models.CharField(
		max_length=128,
		null=False,
		blank=False,
	)
	country = models.CharField(
		max_length=128,
		null=False,
		blank=False,
	)

	def __str__(self):
		return f'{self.name}, {self.country}'
