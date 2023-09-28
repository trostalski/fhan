import requests
from urllib.parse import urljoin


def join_urls(*args):
    """
    Join multiple URLs together.
    """
    return "/".join(map(lambda x: str(x).rstrip("/"), args))


def make_get_request(
    url: str,
    session: requests.Session | None = None,
    params: dict | None = None,
    headers: dict | None = None,
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
