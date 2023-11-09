import pytest
import requests
import requests_mock

from fhan.client.utils.http_utils import (
    make_put_request,
    make_post_request,
    join_urls,
)  # ensure to import from the correct place


@pytest.mark.parametrize(
    "parts,expected",
    [
        (["http://example.com", "path"], "http://example.com/path"),
        (["http://example.com/", "/path", "/"], "http://example.com/path"),
        (["http://example.com", "path/"], "http://example.com/path"),
    ],
)
def test_join_urls(parts, expected):
    assert join_urls(*parts) == expected


# Parametrized test for the make_put_request function
@pytest.mark.parametrize(
    "status_code,raises_exception",
    [
        (200, False),  # Successful request
        (404, True),  # Not Found
        (500, True),  # Server Error
    ],
)
def test_make_put_request(status_code, raises_exception, requests_mock):
    url = "http://example.com/resource"
    data = {"key": "value"}
    headers = {"Content-Type": "application/json"}
    requests_mock.put(url, status_code=status_code, json=data)

    if raises_exception:
        with pytest.raises(requests.HTTPError):
            make_put_request(url, data=data, headers=headers)
    else:
        response = make_put_request(url, data=data, headers=headers)
        assert response.status_code == status_code


# Parametrized test for the make_post_request function
@pytest.mark.parametrize(
    "status_code,raises_exception",
    [
        (201, False),  # Created
        (400, True),  # Bad Request
        (503, True),  # Service Unavailable
    ],
)
def test_make_post_request(status_code, raises_exception, requests_mock):
    url = "http://example.com/resource"
    data = {"key": "value"}
    headers = {"Content-Type": "application/json"}
    requests_mock.post(url, status_code=status_code, json=data)

    if raises_exception:
        with pytest.raises(requests.HTTPError):
            make_post_request(url, data=data, headers=headers)
    else:
        response = make_post_request(url, data=data, headers=headers)
        assert response.status_code == status_code
