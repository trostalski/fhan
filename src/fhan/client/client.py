from importlib import import_module
import os
from typing import Any, Literal, Optional, Union, List, Dict
import logging
from cachetools import TTLCache

from dotenv import load_dotenv
from urllib.parse import urljoin
import requests

from cachetools import Cache
from fhan.client.auth import Auth
from fhan.client.metadata import ServerMetadata
from fhan.core.exceptions import OperationOutcomeException
from fhan.client.search_bundle import SearchBundle
from fhan.core.fhir_package import FhirPackage, FhirPackageLoader
from fhan.core.fhir_types import _ResourceType
from fhan.core.utils.fhir_utils import is_bundle
from fhan.models.R4.CapabilityStatement import CapabilityStatement
from fhan.models.generator_models import BaseModel
from fhan.client.utils.http_utils import (
    build_fhir_get_url,
    build_fhir_search_url,
    _make_get_request,
    join_urls,
)

FHIR_VERSION = "R4"
load_dotenv()


class Client:
    """
    Client for interacting with a FHIR server.

    Args:
        base_url (str): Base url of the FHIR server.
        fhir_version (str): FHIR version of the server. Defaults to version specified in the settings.
    """

    def __init__(
        self,
        base_url: str = None,
        fhir_version: str = FHIR_VERSION,
        load_package_context: bool = False,
        authenticate: bool = True,
        auth_method: Literal["basic", "bearer", "cookie"] = "cookie",
        use_cache: bool = False,
        cache: Cache = None,
        cache_ttl: int = 300,  # 5 minutes
        cache_maxsize: int = 128,
        username: Optional[str] = None,
        password: Optional[str] = None,
        login_url: Optional[str] = None,
        token: Optional[str] = None,
        token_type: Optional[str] = None,
        logging_level: Optional[str] = "INFO",
    ):
        base_url = base_url or os.getenv("BASE_URL")
        if not base_url:
            raise ValueError("Base URL is required.")
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._session = requests.Session()
        self._fhir_version = fhir_version
        # context
        self.metadata = None
        self._package_context = None
        self.test_connection()
        if load_package_context:
            self._init_context(fhir_version=fhir_version)
        # cache
        self._init_cache(
            use_cache=use_cache,
            cache=cache,
            cache_ttl=cache_ttl,
            cache_maxsize=cache_maxsize,
        )
        # auth
        self.token = token
        if authenticate:
            self.authenticate(
                auth_method=auth_method,
                username=username,
                password=password,
                token=token,
                token_type=token_type,
                login_url=login_url,
            )

    def _init_context(self, fhir_version: str):
        self._package_context: Optional[FhirPackage] = self._load_fhir_package(
            fhir_version=fhir_version
        )

    def _init_cache(
        self, use_cache: bool, cache: Cache, cache_ttl: int, cache_maxsize: int
    ):
        self.use_cache = use_cache
        if self.use_cache:
            # TODO: Add support for other cache types
            self.cache = (
                TTLCache(maxsize=cache_maxsize, ttl=cache_ttl) if not cache else cache
            )
        else:
            self.cache = None

    def authenticate(
        self,
        username: str = None,
        password: str = None,
        token: str = None,
        token_type: str = "Bearer",
        login_url: str = None,
        auth_method: Literal["basic", "bearer", "cookie"] = "cookie",
    ) -> bool:
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
        self._get_metadata()

    def test_connection(self):
        try:
            _make_get_request(
                url=self._base_url,
                session=self._session,
                raise_for_status=True,
                cache=None,
                use_cache=False,
            )
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"Could not connect to server. Make sure the URL is correct: {self._base_url}"
            )
        except Exception:
            # Silently ignore all other exceptions
            pass

    def get(
        self,
        resource_type: Optional[_ResourceType] = None,
        id: Optional[Union[str, List[str]]] = None,
        search_params: Optional[Dict[str, str]] = None,
        search_string: Optional[str] = None,
        pages: Optional[int] = 1,
        as_object: Optional[bool] = False,
        count: Optional[int] = None,
        elements: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        revinclude: Optional[List[str]] = None,
        total: Optional[str] = None,
        url: Optional[str] = None,
        raise_for_status: Optional[bool] = False,
        headers: Optional[Dict[str, str]] = None,
        token: Optional[str] = None,
        token_type: Optional[str] = "Bearer",
    ) -> Union[Dict, "SearchBundle", "BaseModel"]:
        """
        The return type is a resource only when a single id is specified.
        In every other case, the return type is a search bundle.
        """
        headers = headers or {}
        token = token or self.token
        if token:
            headers["Authorization"] = f"{token_type} {token}"
        search_params = self._merge_search_params(
            count, elements, include, revinclude, total, search_params
        )
        if url:
            result = self._get_result_from_url(
                url=url,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )
        elif self._is_search_request(
            id=id, search_params=search_params, search_string=search_string
        ):
            search_string = self._build_search_string(
                id=id, search_string=search_string
            )
            if search_string:
                search_string += "&"
            search_string += self._convert_params_to_string(search_params)
            result = self._execute_search(
                resource_type=resource_type,
                search_string=search_string,
                pages=pages,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )
        else:
            result = self._get_resource_by_id(
                resource_type=resource_type,
                id=id,
                raise_for_status=raise_for_status,
                headers=headers,
                token=token,
                token_type=token_type,
            )

        return self._process_result(result, resource_type, as_object)

    def _get_result_from_url(
        self,
        url: str,
        raise_for_status: bool,
        headers: Optional[Dict[str, str]],
        token: Optional[str],
        token_type: Optional[str],
    ) -> Dict:
        url = join_urls(self._base_url, url)
        return _make_get_request(
            url=url,
            session=self._session,
            raise_for_status=raise_for_status,
            headers=headers,
            cache=self.cache,
            use_cache=self.use_cache,
            token=token,
            token_type=token_type,
        )

    def _is_search_request(self, id, search_params, search_string) -> bool:
        return search_params or search_string or isinstance(id, List) or not id

    def _build_search_string(self, id, search_string) -> str:
        search_string = search_string or ""
        if isinstance(id, list):
            search_string += f"_id={','.join(id)}"
        elif isinstance(id, str):
            search_string += f"_id={id}"
        return search_string

    def _merge_search_params(
        self, count, elements, include, revinclude, total, search_params
    ) -> Dict:
        kwarg_params = _get_params_from_kwargs(
            count=count,
            elements=elements,
            include=include,
            revinclude=revinclude,
            total=total,
        )
        return {**kwarg_params, **(search_params or {})}

    def _execute_search(
        self,
        resource_type,
        search_string,
        pages,
        raise_for_status,
        headers,
        token,
        token_type,
    ):
        return self._search(
            resource_type=resource_type,
            search_string=search_string,
            headers=headers,
            pages=pages,
            raise_for_status=raise_for_status,
            token=token,
            token_type=token_type,
        )

    def _get_resource_by_id(
        self,
        resource_type: str,
        id: str,
        raise_for_status: bool,
        headers: Dict[str, str],
        token: Optional[str],
        token_type: Optional[str],
    ):
        return self._get(
            resource_type=resource_type,
            id=id,
            raise_for_status=raise_for_status,
            headers=headers,
            token=token,
            token_type=token_type,
        )

    def _process_result(self, result, resource_type, as_object):
        if as_object:
            if is_bundle(result):
                return SearchBundle(result)
            if not resource_type:
                resource_type = result["resourceType"]
            klass = _get_model_for_type(resource_type)
            return klass.from_dict(result)
        return result

    def _convert_params_to_string(self, params: Dict[str, Any]) -> str:
        """
        Convert a dictionary of search parameters into a query string.
        """
        return "&".join([f"{key}={value}" for key, value in params.items()])

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
            try:
                response_resource = self._search(
                    resource_type=resource_type,
                    search_string=f"_{param_name}={param}",
                    pages=1,
                    raise_for_status=False,
                )
                valid_params.append(param)
            except OperationOutcomeException as e:
                continue
        if param_name == "revinclude":
            self.metadata.available_revincludes[resource_type] = valid_params
        elif param_name == "include":
            self.metadata.available_includes[resource_type] = valid_params

    def get_patient_data(
        self, patient_id: str, pages: Optional[int] = -1, as_object: bool = False
    ):
        possible_revincludes = self.metadata.available_revincludes["Patient"]
        search_string = f"_id={patient_id}"
        c = 0
        for revinclude in possible_revincludes:
            if c > 10:
                break
            search_string += f"&_revinclude={revinclude}"
        res = self.get(
            resource_type="Patient",
            search_string=search_string,
            pages=pages,
        )
        res = self._process_result(res, "Patient", as_object)
        return res

    def _get(
        self,
        resource_type: str,
        id: str,
        raise_for_status: bool,
        headers: Optional[Dict[str, str]],
        token: Optional[str],
        token_type: Optional[str],
    ):
        url = build_fhir_get_url(
            base_url=self._base_url, resource_type=resource_type, id=id
        )
        result = _make_get_request(
            url=url,
            session=self._session,
            raise_for_status=raise_for_status,
            headers=headers,
            cache=self.cache,
            use_cache=self.use_cache,
            token=token,
            token_type=token_type,
        )

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
        url = build_fhir_search_url(
            base_url=self._base_url, resource_type=resource_type, search=search_string
        )
        result = _make_get_request(
            url=url,
            session=self._session,
            raise_for_status=raise_for_status,
            headers=headers,
            cache=self.cache,
            use_cache=self.use_cache,
            token=token,
            token_type=token_type,
        )
        next_link = _get_next_link(result, self._base_url)
        while pages > 1 or pages == -1:
            if next_link:
                next_page = _make_get_request(
                    url=next_link,
                    session=self._session,
                    raise_for_status=raise_for_status,
                    headers=headers,
                    token=token,
                    token_type=token_type,
                    cache=self.cache,
                    use_cache=self.use_cache,
                )
                next_link = _get_next_link(next_page, self._base_url)
                result["entry"] += next_page.get("entry", [])
                if pages > 0:  # -1 means all pages
                    pages -= 1
            else:
                break
        return result

    def _load_fhir_package(
        self, fhir_version: Optional[str], package_name: Optional[str] = None
    ) -> FhirPackage:
        """
        Load the FHIR package for the specified FHIR version.
        TODO: Add support for loading a specific package by name.
        """
        fhir_version = fhir_version or self._fhir_version
        loader = FhirPackageLoader()
        package = loader.load_package_from_version(fhir_version=fhir_version)
        return package

    def _get_metadata(self, num_try: int = 0):
        metadata = _make_get_request(
            url=join_urls(self._base_url, "metadata"),
            session=self._session,
            raise_for_status=False,
            cache=None,
            use_cache=False,
        )
        if self._package_context:
            metadata = {
                **metadata,
                **self._package_context.base_capability_statement,
            }
        self.metadata = ServerMetadata(CapabilityStatement.from_dict(metadata))

    def invalidate_cache(self):
        """
        Invalidates (clears) the cache.
        """
        if self.cache:
            self.cache.clear()


def _get_params_from_kwargs(**kwargs):
    params = {}
    for key, value in kwargs.items():
        if value:
            params[f"_{key}"] = value
    return params


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
