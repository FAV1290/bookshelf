import pytest


from books.models import Book
from utils.converters import serialize_book


@pytest.mark.django_db
@pytest.mark.parametrize(
    'title, author, year_of_publishing, copies_printed, description',
    [
        ('Fahrenheit 451', 'Ray Bradbury', 1953, 600000, 'Dystopian novel'),
    ],
)
def test__serialize_book__converts_book_instance_to_mapping(
    title, author, year_of_publishing, copies_printed, description,
):
    test_book = Book.objects.create(
        title=title,
        author_full_name=author,
        year_of_publishing=year_of_publishing,
        copies_printed=copies_printed,
        short_description=description,
    )
    test_mapping = serialize_book(test_book)
    expected_mapping = {
        'id': '1',
        'title': title,
        'author_full_name': author,
        'year_of_publishing': str(year_of_publishing),
        'copies_printed': str(copies_printed),
        'short_description': description,
    }
    assert test_mapping == expected_mapping
