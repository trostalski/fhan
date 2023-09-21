import requests
import logging

from fhan.core.settings import ClientSettings
from fhan.client.get_handler import GetHandler
from fhan.client.utils.http_utils import make_get_request, join_urls

logger = logging.getLogger(__name__)

DEFAULT_FHIR_VERSION = ClientSettings.default_fhir_version


class MetadataParser:
    """
    Parses the metadata from a FHIR server.
    """

    def __init__(self, metadata: dict):
        self._metadata = metadata
        self.available_resource_types = self._get_available_resource_types()

    def _get_available_resource_types(self):
        available_resource_types = []
        rests = self._metadata["rest"]
        for rest in rests:
            for resource in rest["resource"]:
                available_resource_types.append(resource["type"])
        available_resource_types = list(set(available_resource_types))
        return available_resource_types


class Client:
    """
    Client for interacting with a FHIR server.
    """

    def __init__(self, base_url: str, fhir_version: str = DEFAULT_FHIR_VERSION):
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._fhir_version = fhir_version
        self._sesssion = requests.Session()
        self._metadata = MetadataParser(self._get_metadata())
        self.get = GetHandler(
            session=self._sesssion,
            base_url=self._base_url,
            available_resource_types=self._metadata.available_resource_types,
        )

    def _get_metadata(self):
        metadata = make_get_request(
            url=join_urls(self._base_url, "metadata"), session=self._sesssion
        ).json()
        return metadata
