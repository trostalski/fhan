from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv
from fhirmodels.R4 import DetectedIssue, OperationOutcome
from requests.exceptions import JSONDecodeError

from fhan.client.exceptions import OperationOutcomeException, RequestException
from fhan.client.issue_types import ISSUE_TYPES
from fhan.client.log import logger

load_dotenv()


def join_urls(*args):
    """
    Join multiple URLs together.
    """
    parts = [arg.strip("/") for arg in args if arg is not None]
    url = "/".join(parts)
    return url.rstrip("/")


def make_get_request(
    url: str,
    session: Optional[requests.Session] = None,
    raise_for_status: Optional[bool] = True,
    token: Optional[str] = None,
    token_type: Optional[str] = None,
    headers: Optional[dict] = None,
) -> dict:
    """
    Make a GET request to an URL using the given session.
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


def handle_operation_outcome(operation_outcome: OperationOutcome):
    """
    Handle FHIR Server OperationOutcome responses.
    """
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


def is_bundle(input: Any):
    if not isinstance(input, dict):
        return False
    return "resourceType" in input and input["resourceType"] == "Bundle"


def is_empty_bundle(input: dict):
    """This does not check if the input is a bundle."""
    return "entry" not in input or len(input["entry"]) == 0


def safe_get(target, *attrs):
    """
    Try to get the item from the target safely.
    If any item in the chain is missing, return None.
    """
    for attr in attrs:
        try:
            # Check if the target is a dict or list, and then attempt to access the item.
            if isinstance(target, dict) and attr in target:
                target = target[attr]
            elif (
                isinstance(target, list)
                and isinstance(attr, int)
                and attr < len(target)
            ):
                target = target[attr]
            else:
                # If the attr is not a valid index/key, or the target is not a dict/list, return None
                return None
        except (TypeError, IndexError, KeyError):
            # If any exception occurred due to invalid indexing/key, return None
            return None
    return target


def get_next_link(bundle: dict, base_url: str) -> Optional[str]:
    """
    Get the next link from a bundle.
    """
    if "link" not in bundle:
        return None
    for link in bundle["link"]:
        if link["relation"] == "next":
            next_link = link["url"]
            return urljoin(base_url, next_link)
    return None


def get_params_from_kwargs(**kwargs):
    """
    Transform search parameters for FHIR compatibility.
    FHIR expects the search parameters that the client exposes to be prefixed
    with an underscore. This function adds the underscore prefix to each non-empty parameter.
    """
    params = {}
    for key, value in kwargs.items():
        if value:
            params[f"_{key}"] = value
    return params


def incorporate_ids_in_search(
    id: Optional[Union[str, List[str]]], search_string: str
) -> str:
    """
    Incorporate the id(s) into the search string.
    """
    if isinstance(id, list):
        return f"{search_string or ''}_id={','.join(id)}"
    elif isinstance(id, str):
        return f"{search_string or ''}_id={id}"
    return search_string or ""


def convert_params_to_string(params: Dict[str, Any]) -> str:
    """
    Convert a dictionary of search parameters into a query string.
    """
    return "&".join([f"{key}={value}" for key, value in params.items()])
