import pytest


from books.models import Book


@pytest.mark.django_db
def create_test_book_instance() -> Book:
    Book.objects.create(
        title='Fahrenheit 451',
        author_full_name='Ray Bradbury',
        year_of_publishing=1953,
        copies_printed=600000,
        short_description='Dystopian novel',
    )


@pytest.mark.django_db
def create_test_books_list() -> list[Book]:
    books = []
    for temp in range(451, 455):
        new_book = Book.objects.create(
            title=f'Fahrenheit {temp}',
            author_full_name='Ray Bradbury',
            year_of_publishing=1953,
            copies_printed=600000,
            short_description='Dystopian novel',
        )
        books.append(new_book)
    return books
