from typing import Optional

import requests
from cachetools import TTLCache
from dotenv import load_dotenv
from fhirmodels.R4 import DetectedIssue, OperationOutcome
from requests.exceptions import JSONDecodeError

from fhan.client.decorators import conditional_cache
from fhan.client.exceptions import OperationOutcomeException, RequestException
from fhan.client.log import logger
from fhan.client.utils.fhir_utils import safe_get
from fhan.client.utils.issue_types import ISSUE_TYPES

load_dotenv()


def join_urls(*args):
    """
    Join multiple URLs together.
    """
    parts = [arg.strip("/") for arg in args if arg is not None]
    url = "/".join(parts)
    return url.rstrip("/")


@conditional_cache
def _make_get_request(
    url: str,
    session: Optional[requests.Session] = None,
    raise_for_status: Optional[bool] = True,
    token: Optional[str] = None,
    token_type: Optional[str] = None,
    headers: Optional[dict] = None,
    use_cache: bool = False,
    cache: Optional[TTLCache] = None,
) -> dict:
    """
    Make a GET request to a URL.
    """
    if headers is None:
        headers = {}
    if token:
        headers["Authorization"] = f"{token_type} {token}"
    if session:
        response = session.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers)
    if raise_for_status:
        logger.debug(
            f"GET request to {url} returned status code {response.status_code}."
        )
        response.raise_for_status()
    try:
        data = response.json()
    except JSONDecodeError:
        raise RequestException(f"Could not decode response as JSON, endpoint: {url}")
    if data.get("resourceType") == "OperationOutcome":
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
            logger.debug("OperationOutcome success.")
        elif issue.code in ISSUE_TYPES:
            raise_exc = ISSUE_TYPES[issue.code]["raise"]
            logger.warning(f"OperationOutcome issue code: {issue.code}.")
            raise raise_exc(error_text)
        else:
            logger.warning(
                f"Unknown issue code: {issue.code}.\nOperation Outcome: {operation_outcome.as_dict()}"
            )
            raise OperationOutcomeException(error_text)
    return operation_outcome
