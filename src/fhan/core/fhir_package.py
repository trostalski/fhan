import logging
from typing import BinaryIO, Iterator, Literal, Tuple
import json
import tarfile
import requests
import io

from fhan.core.settings import BaseSettings


logger = logging.getLogger(__name__)


class FhirPackageLoader:
    """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""

    def __init__(self):
        pass

    def load_package(
        self,
        url: str = None,
        version: Literal["R4", "R4B", "R5"] = None,
    ):
        """Loads a FHIR package for a specified FHIR version."""
        if not url and not version:
            raise ValueError("Either version or url must be specified.")
        if url:
            url = url
        elif version:
            version_urls = BaseSettings.fhir_version_package_urls
            if version not in version_urls:
                raise ValueError(
                    f"Unsupported version: {version}. Supported versions: {version_urls.keys()}"
                )
            url = version_urls[version]
        return self._load_package_from_npm(url, name=version)

    def _load_package_from_npm(self, url: str, name: str = None):
        """Loads a FHIR npm package from an URL."""
        with requests.get(url, stream=True) as res:
            res.raise_for_status()
            package_bytes = res.content
            package_buffer = io.BytesIO(package_bytes)
        return FhirPackage.from_npm_file(npm_file=package_buffer, name=name)


class FhirPackage:
    """Represents a FHIR package. In case a FHIR base version is loaded,
    the name should be equivalent to the FHIR version (e.g. "R4")."""

    def __init__(
        self,
        code_systems: list[dict],
        search_parameters: list[dict],
        structure_definitions: list[dict],
        value_sets: list[dict],
        capability_statements: list[dict],
        name: str = None,
    ):
        self.code_systems = code_systems
        self.search_parameters = search_parameters
        self.structure_definitions = structure_definitions
        self.value_sets = value_sets
        self.capability_statements = capability_statements
        self.name = name

    @classmethod
    def from_npm_file(cls, npm_file: BinaryIO, name: str = None):
        """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""
        code_systems = []
        search_parameters = []
        structure_definitions = []
        value_sets = []
        capability_statements = []
        for filename, content in _read_fhir_package_npm(npm_file):
            content_json = json.loads(content)
            resource_type = content_json.get("resourceType")
            if resource_type == "CodeSystem":
                code_systems.append(content_json)
            elif resource_type == "SearchParameter":
                search_parameters.append(content_json)
            elif resource_type == "StructureDefinition":
                structure_definitions.append(content_json)
            elif resource_type == "ValueSet":
                value_sets.append(content_json)
            elif resource_type == "CapabilityStatement":
                capability_statements.append(content_json)
            else:
                # logger.info("Skipping file: %s.", filename)
                continue

        return cls(
            code_systems,
            search_parameters,
            structure_definitions,
            value_sets,
            capability_statements,
            name,
        )

    def get_codesystem_by_url(self, url: str):
        for cs in self.code_systems:
            if cs["url"] == url:
                return cs
        return None

    @property
    def resource_structure_definitions(self):
        return self._get_structure_definitions_by_kind("resource")

    @property
    def complex_type_structure_definitions(self):
        return self._get_structure_definitions_by_kind("complex-type")

    @property
    def primitive_type_structure_definitions(self):
        return self._get_structure_definitions_by_kind("primitive-type")

    @property
    def logical_structure_definitions(self):
        return self._get_structure_definitions_by_kind("logical")

    def _get_structure_definitions_by_kind(
        self, kind: Literal["resource", "complex-type", "primitive-type", "logical"]
    ):
        return [sd for sd in self.structure_definitions if sd["kind"] == kind]


def _read_fhir_package_npm(npm_file: BinaryIO) -> Iterator[Tuple[str, str]]:
    """Yields the file entries for JSON resources in `npm_file` and their contents."""
    with tarfile.open(fileobj=npm_file, mode="r:gz") as f:
        for member in f.getmembers():
            if member.name.endswith(".json"):
                content = f.extractfile(member)
                if content is not None:
                    yield member.name, content.read().decode("utf-8")
            else:
                # logger.info("Skipping  entry: %s.", member.name)
                continue
