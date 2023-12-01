import pytest


from books.models import Book
from django.core.exceptions import ValidationError
from tests.testing_helpers import create_test_books_list


@pytest.mark.django_db
def test__book_fetch_books__gets_correct_books_list():
    create_test_books_list()
    books = list(Book.fetch_books())
    books_titles_last_symbols = list(map(lambda x: int(x.title[-1]), books))
    assert len(books) == 4 and books_titles_last_symbols == list(range(1, 5))


@pytest.mark.django_db
def test__book_fetch_books__returns_blank_list_if_db_is_empty():
    assert list(Book.fetch_books()) == []


@pytest.mark.django_db
def test__book_find_book_by_id__returns_correct_book():
    create_test_books_list()
    target_book = Book.find_book_by_id(2)
    assert target_book.title == 'Fahrenheit 452'


@pytest.mark.django_db
def test__book_find_book_by_id__returns_none_for_undefined_id():
    assert Book.find_book_by_id(2) is None


@pytest.mark.django_db
@pytest.mark.parametrize(
    'title, author_name', [('111'*600, 'Ray Bradbury'), ('Fahrenheit 451', '111'*600)])
def test__book_init__does_not_allow_to_create_too_long_title_and_author_name(title, author_name):
    with pytest.raises(ValidationError):
        Book.objects.create(
            title=title,
            author_full_name=author_name,
            year_of_publishing=1953,
            copies_printed=600000,
            short_description='Dystopian novel',
        ).full_clean()
