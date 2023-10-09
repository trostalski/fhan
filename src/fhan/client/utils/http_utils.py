import os
from typing import Optional, Union
import requests

from dotenv import load_dotenv

load_dotenv()


def join_urls(*args):
    """
    Join multiple URLs together.
    """
    return "/".join(map(lambda x: str(x).rstrip("/"), args))


def make_put_request(
    url: str,
    session: Optional[requests.Session] = None,
    data: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> requests.Response:
    """
    Make a PUT request to a URL.
    """
    if data is None:
        data = {}
    if headers is None:
        headers = {}

    if session:
        response = session.put(url, json=data, headers=headers)
    else:
        response = requests.put(url, json=data, headers=headers)

    response.raise_for_status()
    return response


def make_post_request(
    url: str,
    session: Optional[requests.Session] = None,
    data: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> requests.Response:
    """
    Make a POST request to a URL.
    """
    if data is None:
        data = {}
    if headers is None:
        headers = {}

    if session:
        response = session.post(url, json=data, headers=headers)
    else:
        response = requests.post(url, json=data, headers=headers)

    response.raise_for_status()
    return response


def make_get_request(
    url: str,
    session: Optional[requests.Session] = None,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> requests.Response:
    """
    Make a GET request to a URL.
    """
    if params is None:
        params = {}
    if headers is None:
        headers = {}

    if session:
        response = session.get(url, params=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)

    response.raise_for_status()
    return response


def build_fhir_get_url(
    base_url: str,
    resource_type: str,
    id: str,
) -> str:
    """
    Build a FHIR URL from a base URL, resource type, and optional ID or search string.
    """
    url = join_urls(base_url, resource_type, id)
    return url


def build_fhir_search_url(
    base_url: str,
    resource_type: str,
    search: str,
):
    url = join_urls(base_url, resource_type)
    if not search:
        return url
    elif not search.startswith("?"):
        search = f"?{search}"
    url += search
    return url
