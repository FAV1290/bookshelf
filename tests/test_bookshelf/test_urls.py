import pytest


from tests.testing_helpers import create_test_book_instance


@pytest.mark.django_db
@pytest.mark.parametrize(
    'url, expected_status_code, expected_redirect_url',
    [
        ('', 302, '/books/'),
        ('/', 302, '/books/'),
        ('/books', 301, '/books/'),
        ('/admin', 301, '/admin/'),
        ('/books/', 200, None),
        ('/api/books/', 200, None),
        ('/api/books/123456', 200, None),
    ],
)
def test__urls__show_up_with_empty_db(client, url, expected_status_code, expected_redirect_url):
    response = client.get(url)
    assert response.status_code == expected_status_code
    assert response.url == expected_redirect_url if expected_redirect_url else True


@pytest.mark.django_db
@pytest.mark.parametrize('url, expected_status_code', [('/books/1', 200), ('/book/13146363', 404)])
def test__urls__show_up_with_filled_db(client, url, expected_status_code):
    create_test_book_instance()
    response = client.get(url)
    assert response.status_code == expected_status_code


def test__admin_panel__shows_up(admin_client):
    direct_request = admin_client.get('/admin/')
    indirect_request = admin_client.get('/admin')
    assert direct_request.status_code == 200
    assert indirect_request.status_code == 301
    assert indirect_request.url == '/admin/'
