import logging
from typing import Optional
from cachetools import TTLCache
import requests

from dotenv import load_dotenv

from fhan.client.decorators import conditional_cache
from fhan.client.utils.issue_types import ISSUE_TYPES
from fhan.core.exceptions import (
    OperationOutcomeException,
)
from fhan.core.utils.fhir_utils import safe_get
from fhan.models.R4 import OperationOutcome, DetectedIssue


load_dotenv()


def join_urls(*args):
    """
    Join multiple URLs together.
    """
    parts = [arg.strip("/") for arg in args if arg is not None]
    url = "/".join(parts)
    return url.rstrip("/")


def make_put_request(
    url: str,
    session: Optional[requests.Session] = None,
    data: Optional[dict] = None,
    headers: Optional[dict] = None,
    raise_for_status: Optional[bool] = True,
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

    if raise_for_status:
        response.raise_for_status()
    return response


def make_post_request(
    url: str,
    session: Optional[requests.Session] = None,
    data: Optional[dict] = None,
    headers: Optional[dict] = None,
    raise_for_status: Optional[bool] = True,
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

    if raise_for_status:
        response.raise_for_status()
    return response


@conditional_cache
def _make_get_request(
    url: str,
    session: Optional[requests.Session],
    raise_for_status: Optional[bool],
    token: Optional[str] = None,
    token_type: Optional[str] = None,
    headers: Optional[dict] = None,
    use_cache: bool = None,  # used for conditional_cache decorator
    cache: Optional[TTLCache] = None,  # used for conditional_cache decorator
) -> dict:
    """
    Make a GET request to a URL.
    """
    if headers is None:
        headers = {}

    print("URL : ", url)
    if token:
        headers["Authorization"] = f"{token_type} {token}"
    if session:
        response = session.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers)

    if raise_for_status:
        response.raise_for_status()

    data = response.json()

    if data["resourceType"] == "OperationOutcome":
        data = handle_operation_outcome(OperationOutcome.from_dict(data))
    return data


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


def handle_operation_outcome(operation_outcome: OperationOutcome):
    issues = operation_outcome.issue

    def get_error_text(issue: DetectedIssue):
        text = []
        if issue.code in ISSUE_TYPES:
            text.append("Code: " + ISSUE_TYPES[issue.code]["display"])
        details = (
            safe_get(issue, "details", "text")
            or safe_get(issue, "diagnostics")
            or safe_get(issue, "details", "coding", 0, "display")
        )
        if details:
            text.append("Details: " + details)
        if len(text) == 0:
            text.append(issue.code)
        return ". ".join(text)

    for issue in issues:
        error_text = get_error_text(issue)
        if issue.code == "success":
            logging.info("OperationOutcome success.")
        elif issue.code in ISSUE_TYPES:
            raise_exc = ISSUE_TYPES[issue.code]["raise"]
            raise raise_exc(error_text)
        else:
            logging.error(
                f"Unknown issue code: {issue.code}.\nOperation Outcome: {operation_outcome.as_dict()}"
            )
            raise OperationOutcomeException(error_text)
    return operation_outcome
