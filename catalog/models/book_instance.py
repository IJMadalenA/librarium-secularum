# Imported from Django.
import uuid
from django.db import models

# Models.
from .book import Book
from .author import Author
from .publisher import Publisher


class BookInstance(models.Model):
	class BookStatus(models.TextChoices):
		AVA = 'Available'
		BOR = 'Borrowed'
		RES = 'Reserved'
		LOS = 'LOST'
	
	status = models.CharField(
		max_length=10,
		choices=BookStatus.choices,
		default=BookStatus.AVA
	)
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		help_text='Unique ID for this particular book across whole library'
	)
	num_borrowed = models.PositiveIntegerField(
		null=True,
		blank=True,
	)
	loan_date = models.DateField(
		null=False,
		blank=False,
	)
	return_date = models.DateField(
		null=True,
		blank=True,
	)
	book = models.ForeignKey(
		Book,
		null=False,
		blank=False,
		on_delete=models.PROTECT
	)
	prologue_author = models.ForeignKey(
		Author,
		blank=True,
		null=True,
		on_delete=models.PROTECT
	)
	prologue = models.TextField(
		null=True,
		blank=True,
	)
	edition_year = models.DateField(
		null=False,
		blank=False,
	)
	edition_num = models.PositiveIntegerField(
		null=False,
		blank=False,
	)
	publisher = models.ForeignKey(
		Publisher,
		blank=False,
		null=True,
		on_delete=models.PROTECT
	)
	
	class Meta:
		ordering = ['return_date']
	
	def __str__(self):
		return f'{self.pk}, {self.book.title}'
