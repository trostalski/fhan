import logging
from typing import BinaryIO, Iterator, Literal, Tuple
import json
import tarfile

logger = logging.getLogger(__name__)


class FhirPackage:
    """Represents a FHIR package."""

    def __init__(
        self,
        code_systems: list[dict],
        search_parameters: list[dict],
        structure_definitions: list[dict],
        value_sets: list[dict],
    ):
        self._code_systems = code_systems
        self._search_parameters = search_parameters
        self._structure_definitions = structure_definitions
        self._value_sets = value_sets

    @classmethod
    def from_npm(cls, npm_file: BinaryIO):
        """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""
        code_systems = []
        search_parameters = []
        structure_definitions = []
        value_sets = []
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
            else:
                # logger.info("Skipping file: %s.", filename)
                continue

        return cls(code_systems, search_parameters, structure_definitions, value_sets)

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
        return [sd for sd in self._structure_definitions if sd["kind"] == kind]


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
