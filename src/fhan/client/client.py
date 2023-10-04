from importlib import import_module
from typing import Any
import requests
import logging
from fhan.client.generated.get_resource_mixin import GetResourceMixin
from fhan.client.generated.search_resource_mixin import SearchResourceMixin
from fhan.client.search_builder import SearchBuilder
from fhan.client.search_bundle import SearchBundle

from fhan.client.utils.http_utils import (
    build_fhir_get_url,
    build_fhir_search_url,
    make_get_request,
    join_urls,
)
from fhan.core.fhir_package import FhirPackageLoader
from fhan.core.settings import ClientSettings
from fhan.models.R4.CapabilityStatement import CapabilityStatement
from fhan.models.generator_models import BaseModel
from fhan.views.view import View

logger = logging.getLogger(__name__)

FHIR_VERSION = ClientSettings.fhir_version


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


class BaseHttpHandler:
    def __init__(
        self,
        session: requests.Session,
        base_url: str,
        metadata: ServerMetadata,
    ):
        super().__init__()
        self._session = session
        self._base_url = base_url
        self.metadata = metadata

    def __call__(self, url: str = "") -> Any:
        """Make a GET request relative from the base URL with
        a custom url. E.g.: client.get("Patient/1")"""

        url = join_urls(self._base_url, url)
        response = make_get_request(url, session=self._session)
        return response.json()


class SearchHandler(BaseHttpHandler, SearchResourceMixin):
    """Handles all search functionality."""

    def __init__(
        self,
        session: requests.Session,
        metadata: ServerMetadata,
        base_url: str,
    ):
        super().__init__(
            session=session,
            base_url=base_url,
            metadata=metadata,
        )

    def _search(self, resource_type: str, search: str, as_object: bool = False):
        url = build_fhir_search_url(
            base_url=self._base_url, resource_type=resource_type, search=search
        )
        result = make_get_request(url=url, session=self._session).json()
        if as_object:
            result = SearchBundle(result)
        return result

    def PatientView(self, patient_id: str, resource: str, view: View):
        """
        Create a view on resources on a patient.
        """
        # Get all patient revincludes available for the target resource from the server
        all_patient_revincludes: list[str] = self.metadata.available_revincludes[
            "Patient"
        ]
        filtered_revincludes = [
            r for r in all_patient_revincludes if r.startswith(resource)
        ]

        # Iteratively build the search string
        sb = SearchBuilder().Patient().param(value="_id").eq(value=patient_id)
        for revinclude in filtered_revincludes:
            sb = sb.AND().revinclude(value=revinclude, modifier="iterate")
        search_string = sb.build()

        # Execute the search and build the view
        search_bundle = self._search(resource_type="Patient", search=search_string)
        view_res = view(search_bundle)
        return view_res


class GetHandler(BaseHttpHandler, GetResourceMixin):
    def __init__(
        self,
        session: requests.Session,
        base_url: str,
        metadata: ServerMetadata,
    ):
        super().__init__(session=session, base_url=base_url, metadata=metadata)

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


def get_model_for_type(resource_type: str) -> BaseModel:
    """
    Get the model for a resource type.
    """
    module = import_module(f"fhan.models.{FHIR_VERSION}.{resource_type}")
    model = getattr(module, resource_type)
    return model


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
        load_package: bool = False,
    ):
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._fhir_version = fhir_version
        self._sesssion = requests.Session()
        self.metadata = ServerMetadata(self._get_metadata())
        self.get = GetHandler(
            session=self._sesssion,
            base_url=self._base_url,
            metadata=self.metadata,
        )
        self.search = SearchHandler(
            session=self._sesssion,
            base_url=self._base_url,
            metadata=self.metadata,
        )

        if load_package:
            self.package = self._load_package()
        else:
            self.package = None

    def _get_metadata(self):
        metadata = make_get_request(
            url=join_urls(self._base_url, "metadata"), session=self._sesssion
        ).json()
        return CapabilityStatement.from_dict(metadata)

    def _load_package(self):
        return FhirPackageLoader().load_package_from_version(
            version=self._fhir_version,
        )
