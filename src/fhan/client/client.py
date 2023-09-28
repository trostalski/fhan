import requests
import logging

from fhan.client.utils.http_utils import make_get_request, join_urls
from fhan.core.fhir_package import FhirPackageLoader
from fhan.core.settings import ClientSettings
from fhan.client.get_handler import GetHandler, SearchHandler
from fhan.models.R4.CapabilityStatement import CapabilityStatement

logger = logging.getLogger(__name__)

DEFAULT_FHIR_VERSION = ClientSettings.fhir_version


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

    def revinclude_params_for_resource(self):
        pass


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
        fhir_version: str = DEFAULT_FHIR_VERSION,
        load_package: bool = False,
    ):
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._fhir_version = fhir_version
        self._sesssion = requests.Session()
        self._metadata = ServerMetadata(self._get_metadata())
        self.get = GetHandler(
            session=self._sesssion,
            base_url=self._base_url,
            available_resource_types=self._metadata.available_resource_types,
        )
        self.search = SearchHandler(
            session=self._sesssion,
            base_url=self._base_url,
            available_resource_types=self._metadata.available_resource_types,
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
        return FhirPackageLoader().load_package(
            version=self._fhir_version,
        )
