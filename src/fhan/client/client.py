from importlib import import_module
from typing import Literal, Optional, Union
import logging

from dotenv import load_dotenv
import requests
from requests.exceptions import HTTPError
from fhan.client.auth import Auth
from fhan.client.exceptions import AuthenticationError


from fhan.client.search_bundle import SearchBundle
from fhan.client.utils.http_utils import (
    build_fhir_get_url,
    build_fhir_search_url,
    make_get_request,
    join_urls,
)
from fhan.core.fhir_package import FhirPackageLoader
from fhan.core.fhir_types import _ResourceType
from fhan.models.R4.CapabilityStatement import CapabilityStatement
from fhan.models.generator_models import BaseModel

logger = logging.getLogger(__name__)
FHIR_VERSION = "R4"

load_dotenv()


class ServerMetadata:
    """
    Parses the metadata from a FHIR server.
    """

    def __init__(self, cap_statement: CapabilityStatement):
        self._cap_statement = cap_statement
        self._set_available_functionality()

    def _set_available_functionality(
        self,
    ) -> None:
        available_resource_types = []
        available_search_params = {}
        available_includes = {}
        available_revincludes = {}
        rests = self._cap_statement.rest
        for rest in rests:
            for resource in rest.resource:
                available_resource_types.append(resource.type)
                available_search_params[resource.type] = [
                    sp.name for sp in resource.searchParam
                ]
                available_includes[resource.type] = [
                    inc for inc in resource.searchInclude
                ]
                available_revincludes[resource.type] = [
                    revinc for revinc in resource.searchRevInclude
                ]
        available_resource_types = list(set(available_resource_types))

        self.available_resource_types = available_resource_types
        self.available_search_params = available_search_params
        self.available_includes = available_includes
        self.available_revincludes = available_revincludes


class Client:
    """
    Client for interacting with a FHIR server.

    Args:
        base_url (str): Base url of the FHIR server.
        fhir_version (str): FHIR version of the server. Defaults to version specified in the settings.
    """

    def __init__(
        self,
        base_url: str,
        fhir_version: str = FHIR_VERSION,
        auth_method: Literal["basic", "bearer", "cookie"] = "cookie",
    ):
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._fhir_version = fhir_version
        self._session = requests.Session()
        self.auth = Auth(method=auth_method, base_url=base_url, session=self._session)
        self._try_get_metadata()

    def get(
        self,
        resource_type: Literal[_ResourceType],
        id: Optional[Union[str, list[str]]] = None,
        search_params: Optional[dict] = None,
        search_string: Optional[str] = None,
        pages: Optional[int] = 1,
        as_object: Optional[bool] = False,
        count: Optional[int] = None,
        elements: Optional[list[str]] = None,
        include: Optional[list[str]] = None,
        revinclude: Optional[list[str]] = None,
        total: Optional[str] = None,
        url: Optional[str] = None,
    ) -> Union[dict, SearchBundle, BaseModel]:
        """
        The return type is a resource only when a single id is specified.
        In every other case, the return type is a search bundle.
        """
        if url:
            return make_get_request(url=url, session=self._session).json()
        is_search = search_params or search_string or isinstance(id, list) or not id
        if is_search:
            search_string = search_string or ""
            kwarg_params = _get_params_from_kwargs(
                count=count,
                elements=elements,
                include=include,
                revinclude=revinclude,
                total=total,
            )
            # overwrite search params with kwargs
            search_params = {**kwarg_params, **(search_params or {})}
            # add search params to search string
            search_string += _get_string_from_search_params(search_params) or ""
            return self._search(
                resource_type=resource_type,
                search=search_string,
                pages=pages,
                as_object=as_object,
            )
        else:
            return self._get(
                resource_type=resource_type,
                id=id,
                as_object=as_object,
            )

    def _get(
        self,
        resource_type: str,
        id: str,
        as_object: bool = False,
    ):
        url = build_fhir_get_url(
            base_url=self._base_url, resource_type=resource_type, id=id
        )
        result = make_get_request(url=url, session=self._session).json()
        if as_object:
            klass = _get_model_for_type(resource_type)
            result = klass.from_dict(result)
        return result

    def _search(
        self,
        resource_type: str,
        search: str,
        pages: Optional[int] = 1,
        as_object: bool = False,
    ):
        url = build_fhir_search_url(
            base_url=self._base_url, resource_type=resource_type, search=search
        )
        result = make_get_request(url=url, session=self._session).json()
        while pages > 1 or pages == -1:
            next_link = _get_next_link(result)
            if next_link:
                next_page = make_get_request(
                    url=next_link, session=self._session
                ).json()
                result["entry"] += next_page["entry"]
                if pages > 0:  # -1 means all pages
                    pages -= 1
            else:
                break
        if as_object:
            result = SearchBundle(result)
        return result

    import logging

    def _try_get_metadata(self, num_try: int = 0):
        if num_try > 3:
            raise AuthenticationError("Could not authenticate.")
        metadata_res = make_get_request(
            url=join_urls(self._base_url, "metadata"),
            session=self._session,
            raise_for_status=False,
        )

        if metadata_res.status_code == 200:
            self.metadata = ServerMetadata(
                CapabilityStatement.from_dict(metadata_res.json())
            )
        elif metadata_res.status_code == 401:
            logging.warning("Server requires authentication")
            logging.warning(f"Trying to authenticate. Auth method: {self.auth.method}")
            self.auth.authenticate()
            if self.auth.is_authenticated:
                logging.info("Authentication successful")
                self._try_get_metadata(num_try=num_try + 1)
            else:
                logging.error("Authentication failed")
        else:
            metadata_res.raise_for_status()


def _get_params_from_kwargs(**kwargs):
    params = {}
    for key, value in kwargs.items():
        if value:
            params[f"_{key}"] = value
    return params


def _get_string_from_search_params(search_params: Optional[dict]):
    if not search_params:
        return None
    search_string = ""
    for key, value in search_params.items():
        search_string += f"{key}={value}&"
    return search_string[:-1]


def _get_model_for_type(resource_type: str) -> BaseModel:
    """
    Get the model for a resource type.
    """
    module = import_module(f"fhan.models.{FHIR_VERSION}.{resource_type}")
    model = getattr(module, resource_type)
    return model


def _get_next_link(bundle: dict) -> Optional[str]:
    """
    Get the next link from a bundle.
    """
    if "link" not in bundle:
        return None
    for link in bundle["link"]:
        if link["relation"] == "next":
            return link["url"]
    return None
