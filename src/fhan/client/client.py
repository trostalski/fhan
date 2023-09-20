import requests
import logging
import urllib3

from fhan.core.settings import ClientSettings

logger = logging.getLogger(__name__)

DEFAULT_FHIR_VERSION = ClientSettings.default_fhir_version


class MetadataParser:
    def __init__(self, metadata: dict):
        self._metadata = metadata

    def _get_available_resource_types(self):
        pass


class GetHandler:
    def __init__(self, session: requests.Session, base_url: str):
        self._session = session
        self._base_url = base_url
        self._initialize()

    def _initialize(self):
        metadata = self._make_request("metadata", {})

    def _make_request(self, endpoint: str, params: dict):
        url = f"{self._base_url}/{endpoint}"
        res = self._session.get(url, params=params)
        res.raise_for_status()
        return res.json()


class Client:
    def __init__(self, base_url: str, fhir_version: str = DEFAULT_FHIR_VERSION):
        self._base_url = base_url if not base_url.endswith("/") else base_url[:-1]
        self._fhir_version = fhir_version
        self._sesssion = requests.Session()
        self.get = GetHandler(session=self._sesssion, base_url=self._base_url)


class GetClient:
    def __init__(self, client: Client):
        self._client = client


class FhirContext:
    pass
