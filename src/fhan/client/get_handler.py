import requests
from importlib import import_module
from typing import Any
from fhan.client.search_bundle import SearchBundle

from fhan.client.utils.http_utils import (
    make_get_request,
    join_urls,
    build_fhir_get_url,
    build_fhir_search_url,
)
from fhan.views.view import View
from fhan.models.generator_models import BaseModel
from fhan.client.generated.get_resource_mixin import GetResourceMixin
from fhan.client.generated.search_resource_mixin import SearchResourceMixin
from fhan.core.settings import BaseSettings

FHIR_VERSION = BaseSettings.fhir_version


class BaseHttpHandler:
    def __init__(
        self,
        session: requests.Session,
        base_url: str,
        available_resource_types: list[str],
    ):
        super().__init__()
        self._session = session
        self._base_url = base_url
        self._available_resource_types = available_resource_types

    def __call__(self, url: str = "") -> Any:
        """Make a GET request relative from the base URL with
        a custom url. E.g.: client.get("Patient/1")"""

        url = join_urls(self._base_url, url)
        response = make_get_request(url, session=self._session)
        return response.json()


class SearchHandler(BaseHttpHandler, SearchResourceMixin):
    def __init__(
        self,
        session: requests.Session,
        base_url: str,
        available_resource_types: list[str],
    ):
        super().__init__(
            session=session,
            base_url=base_url,
            available_resource_types=available_resource_types,
        )

    def _search(self, resource_type: str, search: str, as_object: bool = False):
        url = build_fhir_search_url(
            base_url=self._base_url, resource_type=resource_type, search=search
        )
        result = make_get_request(url=url, session=self._session).json()
        if as_object:
            result = SearchBundle(result)
        return result


class GetHandler(BaseHttpHandler, GetResourceMixin):
    def __init__(
        self,
        session: requests.Session,
        base_url: str,
        available_resource_types: list[str],
    ):
        super().__init__(
            session=session,
            base_url=base_url,
            available_resource_types=available_resource_types,
        )

    def _get(
        self,
        resource_type: str,
        id: str | list[str] | None = None,
        as_object: bool = False,
    ):
        url = build_fhir_get_url(
            base_url=self._base_url, resource_type=resource_type, id=id
        )
        result = make_get_request(url=url, session=self._session).json()
        if as_object:
            klass = get_model_for_type(resource_type)
            result = klass.from_dict(result)
        return result

    def PatientData(self, types: list[str]):
        """
        Get all resources of the specified types for a patient.
        """

    def View(self, view: View):
        """
        Create a search query from a view and execute it.
        """


def get_model_for_type(resource_type: str) -> BaseModel:
    """
    Get the model for a resource type.
    """
    module = import_module(f"fhan.models.{FHIR_VERSION}.{resource_type}")
    model = getattr(module, resource_type)
    return model
