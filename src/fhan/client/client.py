from importlib import import_module
from typing import Literal, Optional, Union
import logging

from dotenv import load_dotenv
from urllib.parse import urljoin
import requests

from fhan.client.auth import Auth
from fhan.core.exceptions import AuthenticationError
from fhan.client.search_bundle import SearchBundle
from fhan.core.fhir_package import FhirPackage, FhirPackageLoader
from fhan.core.fhir_types import _ResourceType
from fhan.models.R4.CapabilityStatement import CapabilityStatement
from fhan.models.generator_models import BaseModel
from fhan.client.utils.http_utils import (
    build_fhir_get_url,
    build_fhir_search_url,
    make_get_request,
    join_urls,
)

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
                    inc.replace(".", ":") for inc in resource.searchInclude
                ]
                available_revincludes[resource.type] = [
                    revinc.replace(".", ":") for revinc in resource.searchRevInclude
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
        load_package_context: bool = False,
        auth_method: Literal["basic", "bearer", "cookie"] = "cookie",
    ):
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._session = requests.Session()
        self.ping()
        self._fhir_version = fhir_version
        self._package_context: Optional[FhirPackage] = (
            None
            if not load_package_context
            else self._load_fhir_package(fhir_version=fhir_version)
        )
        self.auth = Auth(method=auth_method, base_url=base_url, session=self._session)
        self._try_get_metadata()

    def ping(self):
        try:
            make_get_request(
                url=self._base_url, session=self._session, raise_for_status=False
            )
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"Could not connect to server. Make sure the URL is correct: {self._base_url}"
            )

    def get(
        self,
        resource_type: Optional[Literal[_ResourceType]] = None,
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
        raise_for_status: Optional[bool] = True,
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
            if isinstance(id, list):
                search_string += f"_id={','.join(id)}"
            elif isinstance(id, str):
                search_string += f"_id={id}"
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
                search_string=search_string,
                pages=pages,
                as_object=as_object,
                raise_for_status=raise_for_status,
            )
        else:
            return self._get(
                resource_type=resource_type,
                id=id,
                as_object=as_object,
                raise_for_status=raise_for_status,
            )

    def filter_available_search_params(
        self, resource_type: _ResourceType, param_name: Literal["revinclude", "include"]
    ):
        """When the server does not declare the supported search parameters in its
        capability statement, the package context can be used to set these parameters.
        However, the server might not support all parameters. This method filters out the
        unsupported parameters for a specific resource and parameter type."""
        valid_params: list[str] = []
        possible_params: list[str] = []
        if param_name == "revinclude":
            possible_params = self.metadata.available_revincludes[resource_type]
        elif param_name == "include":
            possible_params = self.metadata.available_includes[resource_type]
        else:
            raise ValueError(
                f"Invalid parameter name: {param_name}.\nSupported parameters are: 'revinclude', 'include'"
            )
        for param in possible_params:
            response_resource = self._search(
                resource_type=resource_type,
                search_string=f"_{param_name}={param}",
                pages=1,
                raise_for_status=False,
            )
            response_type = response_resource["resourceType"]
            if response_type == "OperationOutcome":
                continue
            elif response_type == "Bundle":
                valid_params.append(param)
        if param_name == "revinclude":
            self.metadata.available_revincludes[resource_type] = valid_params
        elif param_name == "include":
            self.metadata.available_includes[resource_type] = valid_params

    def get_patient_data(
        self, patient_id: str, pages: Optional[int] = 1, as_object: bool = False
    ):
        possible_revincludes = self.metadata.available_revincludes["Patient"]
        search_string = f"_id={patient_id}"
        c = 0
        for revinclude in possible_revincludes:
            if c > 10:
                break
            search_string += f"&_revinclude={revinclude}"
        res = self._search(
            resource_type="Patient",
            search_string=search_string,
            pages=pages,
            as_object=as_object,
        )
        return res

    def _get(
        self,
        resource_type: str,
        id: str,
        as_object: bool = False,
        raise_for_status: bool = True,
    ):
        url = build_fhir_get_url(
            base_url=self._base_url, resource_type=resource_type, id=id
        )
        result = make_get_request(
            url=url, session=self._session, raise_for_status=raise_for_status
        ).json()
        if as_object:
            klass = _get_model_for_type(resource_type)
            result = klass.from_dict(result)
        return result

    def _search(
        self,
        resource_type: str,
        search_string: str,
        pages: Optional[int] = 1,
        as_object: bool = False,
        raise_for_status: bool = True,
    ):
        url = build_fhir_search_url(
            base_url=self._base_url, resource_type=resource_type, search=search_string
        )
        result = make_get_request(
            url=url, session=self._session, raise_for_status=raise_for_status
        ).json()
        next_link = _get_next_link(result, self._base_url)
        while pages > 1 or pages == -1:
            if next_link:
                next_page = make_get_request(
                    url=next_link, session=self._session
                ).json()
                next_link = _get_next_link(next_page, self._base_url)
                result["entry"] += next_page["entry"]
                if pages > 0:  # -1 means all pages
                    pages -= 1
            else:
                break
        if as_object:
            result = SearchBundle(result)
        return result

    def _load_fhir_package(
        self, fhir_version: Optional[str] = None, package_name: Optional[str] = None
    ) -> FhirPackage:
        """
        Load the FHIR package for the specified FHIR version.
        TODO: Add support for loading a specific package by name.
        """
        fhir_version = fhir_version or self._fhir_version
        loader = FhirPackageLoader()
        package = loader.load_package_from_version(fhir_version=fhir_version)
        return package

    def _try_get_metadata(self, num_try: int = 0):
        if num_try > 3:
            raise AuthenticationError("Could not authenticate.")
        metadata_res = make_get_request(
            url=join_urls(self._base_url, "metadata"),
            session=self._session,
            raise_for_status=False,
        )

        if metadata_res.status_code == 200:
            metadata = metadata_res.json()
            # merge with package context
            if self._package_context:
                metadata = {
                    **metadata,
                    **self._package_context.base_capability_statement,
                }
            self.metadata = ServerMetadata(CapabilityStatement.from_dict(metadata))
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


def _get_next_link(bundle: dict, base_url: str) -> Optional[str]:
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
