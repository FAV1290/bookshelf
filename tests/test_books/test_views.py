import json
import pytest
from django.urls import reverse


from tests.testing_helpers import create_test_book_instance, create_test_books_list
from books.views import index_view, books_view, book_view, api_books_view, api_book_view


def test__index_view__redirects_to_books_view(client):
    response = client.get(reverse(index_view))
    assert response.status_code == 302 and response.url == reverse(books_view)


@pytest.mark.django_db
def test__api_books_view__returns_correct_books_list_json(client):
    create_test_books_list()
    response = client.get(reverse(api_books_view))
    books_list = json.loads(response.content.decode("utf-8"))['books']
    books_list_titles = list(map(lambda x: x['title'], books_list))
    expected_titles = [f'Fahrenheit {temp}' for temp in range(451, 455)]
    assert books_list_titles == expected_titles


@pytest.mark.django_db
def test__api_books_view__returns_blank_list_in_case_of_empty_db(client):
    response = client.get(reverse(api_books_view))
    books_list = json.loads(response.content.decode("utf-8"))['books']
    assert books_list == []


@pytest.mark.django_db
def test__api_book_view__returns_correct_json(client):
    create_test_book_instance()
    response = client.get(reverse(api_book_view, kwargs={'book_id': 1}))
    response_json = json.loads(response.content.decode("utf-8"))
    expected_json = {
        'id': '1',
        'title': 'Fahrenheit 451',
        'author_full_name': 'Ray Bradbury',
        'year_of_publishing': '1953',
        'copies_printed': '600000',
        'short_description': 'Dystopian novel',
    }
    assert response_json == expected_json


@pytest.mark.django_db
def test__api_book_view_returns_error_json_for_undefuned_id(client):
    response = client.get(reverse(api_book_view, kwargs={'book_id': 1}))
    response_json = json.loads(response.content.decode("utf-8"))
    assert response_json == {'error': 'Book with this id was not found'}


@pytest.mark.django_db
@pytest.mark.parametrize(
    'view, kwargs, expected_template',
    [
        (books_view, {}, 'books.html', ),
        (book_view, {'book_id': 1}, 'book.html'),
    ],
)
def test__books_views__return_correct_templates(client, view, kwargs, expected_template):
    create_test_book_instance()
    response = client.get(reverse(view, kwargs=kwargs))
    assert expected_template in [template.name for template in response.templates]
