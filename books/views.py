from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse


from books.models import Book
from utils.converters import serialize_book


@require_GET
def index_view(request: HttpRequest) -> HttpResponse:
    return redirect(books_view)


@require_GET
def api_books_view(request: HttpRequest) -> JsonResponse:
    books = [serialize_book(book) for book in Book.fetch_books()]
    return JsonResponse({'books': books})


@require_GET
def api_book_view(request: HttpRequest, book_id: int) -> JsonResponse:
    try:
        target_book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book with this id was not found'})
    return JsonResponse(serialize_book(target_book))


@require_GET
def books_view(request: HttpRequest) -> HttpResponse:
    books = list(Book.fetch_books())
    return render(request, 'books.html', context={'books': books})


@require_GET
def book_view(request: HttpRequest, book_id: int) -> HttpResponse:
    target_book = Book.find_book_by_id(book_id)
    if not target_book:
        return HttpResponseNotFound('Book with this id was not found')
    else:
        return render(request, 'book.html', context={'book': target_book})
