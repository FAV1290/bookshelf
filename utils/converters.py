from books.models import Book


def serialize_book(book: Book) -> dict[str, str]:
    return {
        'id': str(book.pk),
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': str(book.year_of_publishing),
        'copies_printed': str(book.copies_printed),
        'short_description': book.short_description,
    }
