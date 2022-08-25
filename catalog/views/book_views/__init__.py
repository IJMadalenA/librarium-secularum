from catalog.views.book_views.add_book import PostBookView
from catalog.views.book_views.delete_book import DestroyBookView


class BookView(PostBookView, DestroyBookView):
    def post(self, request):
        super().post(request)

    def delete(self, request, *args, **kwargs):
        super().post(request)
