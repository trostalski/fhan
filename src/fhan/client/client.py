import importlib
import os
from typing import Any, Dict, List, Literal, Optional, Union

import requests
from dotenv import load_dotenv

from fhan.client import log, utils
from fhan.client.auth import Auth
from fhan.client.resource_type import _ResourceType
from fhan.client.search_bundle import SearchBundle

load_dotenv()


class Client:
    """
    Client for interacting with a FHIR server.

    This class provides methods to authenticate, retrieve, and search for FHIR resources from a specified server.

    Args:
        base_url (str, optional): Base URL of the FHIR server. If not provided, it will be read from the BASE_URL environment variable.
        auth_method (Literal["basic", "bearer", "cookie"], optional): Authentication method to use. Defaults to "basic".
        login_url (str, optional): URL for authentication if using cookie-based auth.
        username (str, optional): Username for authentication.
        password (str, optional): Password for authentication.
        token (str, optional): Authentication token if using token-based auth.
        token_type (str, optional): Type of the authentication token (e.g., "Bearer").
        logging_level (Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], optional): Logging level for the client. Defaults to "WARNING".

    Raises:
        ValueError: If base_url is not provided and cannot be read from environment variables.

    Attributes:
        _session (requests.Session): Session object for making HTTP requests.
        _base_url (str): Base URL of the FHIR server.
        token (str): Authentication token.
        auth (Auth): Authentication handler.

    """

    def __init__(
        self,
        base_url: str = None,
        auth_method: Literal["basic", "bearer", "cookie"] = "basic",
        login_url: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        token: Optional[str] = None,
        token_type: Optional[str] = None,
        fhir_version: Optional[Literal["R4", "R4B", "R5"]] = "R4",
        logging_level: Optional[
            Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        ] = "INFO",
    ):
        base_url = base_url or os.getenv("BASE_URL")
        if not base_url:
            raise ValueError("Base URL is required.")

        self._session = requests.Session()
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self.fhir_version = fhir_version

        self.token = token
        self.authenticate(
            auth_method=auth_method,
            username=username,
            password=password,
            token=token,
            token_type=token_type,
            login_url=login_url,
        )

        # Set up logging
        self._setup_logging(logging_level)
        log.logger.info("Client initialized")

    def _setup_logging(self, logging_level: str):
        """Set up logging for the client."""
        log.set_logging_level(logging_level)

    def authenticate(
        self,
        username: str = None,
        password: str = None,
        token: str = None,
        token_type: str = "Bearer",
        login_url: str = None,
        auth_method: Literal["basic", "bearer", "cookie"] = "cookie",
    ) -> bool:
        log.logger.debug(
            "Authenticating",
            auth_method=auth_method,
            username=username,
            token=token,
            token_type=token_type,
            login_url=login_url,
        )
        self.auth = Auth(
            method=auth_method,
            session=self._session,
            username=username,
            password=password,
            token=token,
            token_type=token_type,
            login_url=login_url,
        )
        self.auth.authenticate()

    def get(
        self,
        resource_type: Optional[_ResourceType] = None,
        id: Optional[Union[str, List[str]]] = None,
        search_params: Optional[Dict[str, str]] = None,
        search_string: Optional[str] = None,
        pages: Optional[int] = 1,
        as_object: Optional[bool] = False,
        count: Optional[int] = None,
        include: Optional[str] = None,
        revinclude: Optional[str] = None,
        total: Optional[str] = None,
        url: Optional[str] = None,
        raise_for_status: Optional[bool] = False,
        headers: Optional[Dict[str, str]] = None,
        token: Optional[str] = None,
        token_type: Optional[str] = "Bearer",
    ):
        """
        Retrieve FHIR resources from the server.

        This method can be used to fetch a single resource by ID, perform a search, or make a request to a specific URL.

        Args:
            resource_type (Optional[_ResourceType]): The type of FHIR resource to retrieve.
            id (Optional[Union[str, List[str]]]): The ID(s) of the resource(s) to retrieve.
            search_params (Optional[Dict[str, str]]): A dictionary of search parameters.
            search_string (Optional[str]): A pre-formatted search string.
            pages (Optional[int]): The number of pages to retrieve for paginated results. Defaults to 1.
            as_object (Optional[bool]): If True, return the result as a FHIR model object. Defaults to False.
            count (Optional[int]): The maximum number of resources to return per page.
            include (Optional[str]): Resources to include that are referenced by the matched resources.
            revinclude (Optional[str]): Resources to include that reference the matched resources.
            total (Optional[str]): Indicates whether the search result should include a total count.
            url (Optional[str]): A specific URL to request instead of constructing one.
            raise_for_status (Optional[bool]): If True, raise an exception for HTTP errors. Defaults to False.
            headers (Optional[Dict[str, str]]): Additional headers to include in the request.
            token (Optional[str]): An authentication token to use instead of the client's default.
            token_type (Optional[str]): The type of the authentication token. Defaults to "Bearer".

        Returns:
            Union[Dict, Any]: The retrieved resource(s). If a single resource is requested by ID, it returns that resource.
            Otherwise, it returns a search bundle containing the requested resources.

        Raises:
            RequestException: If there's an error with the HTTP request.
            OperationOutcomeException: If the server returns an OperationOutcome resource indicating an error.
        """
        headers = headers or {}
        token = token or self.token
        if token:
            headers["Authorization"] = f"{token_type} {token}"
        kwarg_params = utils.get_params_from_kwargs(
            count=count,
            include=include,
            revinclude=revinclude,
            total=total,
        )
        search_params = {**kwarg_params, **(search_params or {})}
        if url:
            # just use the provided url
            url = utils.join_urls(self._base_url, url)
            result = utils.make_get_request(
                url=url,
                session=self._session,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )
        elif search_params or search_string or isinstance(id, List) or not id:
            # build the search url
            search_string = utils.incorporate_ids_in_search(id, search_string)
            search_string += (
                f"&{utils.convert_params_to_string(search_params)}"
                if search_params
                else ""
            )
            result = self._search(
                resource_type=resource_type,
                search_string=search_string,
                pages=pages,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )
        else:
            url = utils.join_urls(self._base_url, resource_type, id)

            result = utils.make_get_request(
                url=url,
                session=self._session,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )

        return self._process_result(result, resource_type, as_object)

    def _process_result(
        self, result: Dict[str, Any], resource_type: str, as_object: bool
    ):
        """
        If as_object is True, return the result as a FHIR model object.
        """
        if as_object:
            if utils.is_bundle(result):
                return SearchBundle(result)
            if not resource_type:
                resource_type = result["resourceType"]
            klass = self.get_model_for_type(resource_type)
            return klass.from_dict(result)
        return result

    def _search(
        self,
        resource_type: str,
        search_string: str,
        pages: Optional[int] = 1,
        raise_for_status: bool = False,
        headers: Optional[Dict[str, str]] = None,
        token: Optional[str] = None,
        token_type: Optional[str] = "Bearer",
    ):
        """
        Perform a search request.
        - If pages is 0, return only the first page.
        - If pages is -1, fetch all pages.
        - If pages is > 0, fetch that many pages.
        """
        url = utils.join_urls(self._base_url, resource_type)
        if search_string:
            if not search_string.startswith("?"):
                search_string = f"?{search_string}"
            url += search_string
        log.logger.debug("Fetching page 1")
        result = utils.make_get_request(
            url=url,
            session=self._session,
            raise_for_status=raise_for_status,
            headers=headers,
            token=token,
            token_type=token_type,
        )
        next_link = utils.get_next_link(result, self._base_url)

        current_page = 1
        while (pages > 1 or pages == -1) and next_link:
            current_page += 1
            log.logger.debug(f"Fetching page {current_page}")
            next_page = utils.make_get_request(
                url=next_link,
                session=self._session,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )
            next_link = utils.get_next_link(next_page, self._base_url)
            result["entry"] = result.get("entry", []) + next_page.get("entry", [])
            if pages > 0:
                pages -= 1

        return result

    def get_model_for_type(self, resource_type: str):
        """
        Get the model for a resource type.
        """
        module = importlib.import_module(
            f"fhirmodels.{self.fhir_version}.{resource_type}"
        )
        model = getattr(module, resource_type)
        return model
