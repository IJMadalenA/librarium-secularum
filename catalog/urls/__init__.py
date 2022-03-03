from django.urls import path
from catalog.views import (
    AddAuthorView,
)

urlpatterns = [
    path('add', AddAuthorView.as_view(), name='add-author'),
]
