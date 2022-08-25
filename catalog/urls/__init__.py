from django.urls import path
from catalog.views import (
    AddAuthorView,
)
from catalog.views.book_views import BookView


urlpatterns = [
    path("author", AddAuthorView.as_view(), name='add-author'),
    path("book", BookView.as_view(), name="book"),
]
