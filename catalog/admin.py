# Imported from Django.
from django.contrib import admin

# Models.
from .models import (
    Author,
    Book,
    BookInstance,
    Publisher,
    Genre,
    RelationshipBookGenre,
    RelationshipBookAuthor,
)

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Genre)


class BookInLine(admin.TabularInline):
    models = Book
    extra = 0
    fields = ["title", "isbn"]


class AuthorInLine(admin.TabularInline):
    model = Author
    extra = 0
    fields = ['first_name', 'last_name']


class RelationshipBookAuthorInLine(admin.TabularInline):
    model = RelationshipBookAuthor
    extra = 0
    fields = ['author']
    allow_add = True


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name',
        'date_of_birth', 'date_of_death'
    )
    fields = [
        'first_name', 'last_name',
        ('date_of_birth', 'date_of_death')
    ]
