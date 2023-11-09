import logging
import os
from typing import Any, BinaryIO, Collection, Iterator, Literal, Optional, Tuple
import json
import tarfile
import requests
import io
import time
from dataclasses import dataclass

from fhan.core.settings import BaseSettings
from fhan.core.exceptions import FhirContextException


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class IgDependency:
    """The URL and version of a package dependency."""

    url: str
    version: str


@dataclass(frozen=True)
class PackageMaintainer:
    """The name and email of a package maintainer."""

    name: str
    email: str


@dataclass(frozen=True)
class PackageInfo:
    """Metadata parsed from a package's package.json file.
    See documentation for the package.json file at:
    https://confluence.hl7.org/pages/viewpage.action?pageId=35718629#NPMPackageSpecification-Packagemanifest
    """

    name: str
    version: str
    description: Optional[str] = None
    canonical: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    fhirVersions: Optional[list[str]] = None
    dependencies: Collection["IgDependency"] = ()
    keywords: tuple[str] = ()
    author: Optional[str] = None
    maintainers: list["PackageMaintainer"] = ()
    jurisdiction: Optional[str] = None
    license: Optional[str] = None


class FhirPackageLoader:
    """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""

    def __init__(self):
        pass

    def load_package_from_version(
        self, fhir_version: Literal["R4", "R4B", "R5"]
    ) -> "FhirPackage":
        """Loads a FHIR package for a specified FHIR version."""
        version_urls = BaseSettings.fhir_version_package_urls
        if fhir_version not in version_urls:
            raise FhirContextException(
                f"Unsupported version: {fhir_version}. Supported versions: {version_urls.keys()}"
            )
        url = version_urls[fhir_version]
        return self.load_package_from_npm(url, name=fhir_version)

    def load_package_from_npm(self, url: str, name: str = None):
        """Loads a FHIR npm package from an URL."""
        with requests.get(url, stream=True) as res:
            res.raise_for_status()
            package_bytes = res.content
            package_buffer = io.BytesIO(package_bytes)
        return FhirPackage.from_npm_file(npm_file=package_buffer, name=name)

    def load_from_simplifier(self, name: str, version: str):
        """Loads a FHIR npm package from simplifier.net."""
        url = f"https://packages.simplifier.net/{name}/{version}"
        return self.load_package_from_npm(url, name=name)


class FhirPackage:
    """Represents a FHIR package. In case a FHIR base version is loaded,
    the name should be equivalent to the FHIR version (e.g. "R4")."""

    def __init__(
        self,
        package_info: PackageInfo,
        code_systems: list[dict],
        search_parameters: list[dict],
        structure_definitions: list[dict],
        value_sets: list[dict],
        capability_statements: list[dict],
        name: str = None,
    ):
        self.package_info = package_info
        self.code_systems = code_systems
        self.search_parameters = search_parameters
        self.structure_definitions = structure_definitions
        self.value_sets = value_sets
        self.capability_statements = capability_statements
        self.name = name

    @classmethod
    def from_npm_file(cls, npm_file: BinaryIO, name: str = None):
        """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""
        package_info = None
        code_systems = []
        search_parameters = []
        structure_definitions = []
        value_sets = []
        capability_statements = []
        for filename, content in _read_fhir_package_npm(npm_file):
            content_json = json.loads(content)
            resource_type = content_json.get("resourceType")
            if os.path.basename(filename) == "package.json":
                package_info = _parse_package_info(content_json)
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
            package_info,
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

    @property
    def base_capability_statement(self) -> Optional[dict]:
        """Packages might contain multiple capability statements.
        This method returns the base capability statement identified by the id.
        """
        for cs in self.capability_statements:
            if cs["id"] == "base":
                return cs
        return None

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
                    # using utf-8-sig to remove dealing with BOM, https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig
                    yield member.name, content.read().decode("utf-8-sig")
            else:
                # logger.info("Skipping  entry: %s.", member.name)
                continue


def _parse_package_info(json_obj: dict[str, Any]) -> "PackageInfo":
    """Creates an PackageInfo object given the contents of a package.json file."""
    return PackageInfo(
        name=json_obj["name"],
        version=json_obj["version"],
        canonical=json_obj.get("canonical"),
        title=json_obj.get("title"),
        description=json_obj.get("description"),
        dependencies=tuple(
            IgDependency(url=url, version=version)
            for url, version in json_obj.get("dependencies", {}).items()
        ),
        author=json_obj.get("author"),
        fhirVersions=json_obj.get("fhirVersions"),
        jurisdiction=json_obj.get("jurisdiction"),
        keywords=json_obj.get("keywords"),
        license=json_obj.get("license"),
        maintainers=[
            PackageMaintainer(
                name=maintainer.get("name", ""), email=maintainer.get("email", "")
            )
            for maintainer in json_obj.get("maintainers", [])
        ],
        url=json_obj.get("url"),
    )
