from django.contrib import admin
from django.urls import path


from books.views import api_books_view, api_book_view, books_view, book_view, index_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('api/books/', api_books_view),
    path('api/books/<int:book_id>', api_book_view),
    path('books/', books_view, name='books'),
    path('books/<int:book_id>', book_view),
]
