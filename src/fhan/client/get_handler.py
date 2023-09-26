import requests
from typing import Any
from fhan.client.search_builder import SearchBuilder

from fhan.client.utils.http_utils import make_get_request, build_fhir_url, join_urls
from fhan.client.generated._resource_getter_mixin import ResourceGetterMixin
from fhan.views.view import View


class GetHandler(ResourceGetterMixin):
    def __init__(
        self, session: requests.Session, base_url: str, available_resource_types: list
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

    def _get(
        self,
        resource_type: str,
        id: str | list[str] | None = None,
        search: str = None,
    ):
        if resource_type not in self._available_resource_types:
            raise ValueError(
                f"Resource type {resource_type} is not available for this server."
            )

        url = build_fhir_url(
            base_url=self._base_url, resource_type=resource_type, id=id, search=search
        )
        response = make_get_request(url=url, session=self._session)
        return response.json()

    def PatientData(self, types: list[str]):
        pass

    def View(self, view: View):
        pass
