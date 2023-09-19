import logging
import json
from urllib.parse import urlparse
from dataclasses import dataclass
from enum import Enum

from fhan.core.data_types import get_python_type_for_primitive, is_primitive_type
from fhan.core.utils.path_utils import (
    is_choice_path,
    replace_choice_string,
    get_nth_part,
    is_root_path,
)

logger = logging.getLogger(__name__)


class StructureDefinitionKinds(Enum):
    PRIMITIVE_TYPE = "primitive-type"
    COMPLEX_TYPE = "complext-type"
    RESOURCE = "resource"
    LOGICAL = "logical"


class ModelBase:
    """Base class for all generated models."""

    def __init__(self, **kwargs):
        self._attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._attributes})"

    def __str__(self):
        return str(self._attributes)

    def to_dict(self):
        return self._attributes

    def to_json(self):
        return json.dumps(self._attributes)


class GeneratorElement:
    """Wrapper around a ElementDefinition with a parsed name and type"""

    def __init__(self, element_definition: dict, name: str, type: str):
        self._element = element_definition
        self.type = type
        self.name = name
        self.path = element_definition["path"]
        self.min = element_definition.get("min", None)
        self.max = element_definition.get("max", None)
        is_primitive = is_primitive_type(self.type)
        self.is_primitive = is_primitive
        self.is_complex = not is_primitive
        self.python_type = (
            get_python_type_for_primitive(self.type) if is_primitive else None
        )
        self.description = element_definition.get("definition", "")
        self.short = element_definition.get("short", "")


class GeneratorStructureDefinition:
    """Represents a FHIR StructureDefinition that is used to generate downsream objects."""

    def __init__(self, structure_definition: dict):
        self._structure_definition = structure_definition
        self.elements = self._initialize_elements()
        self.kind = self._structure_definition["kind"]
        self.is_primitive = self.kind == StructureDefinitionKinds.PRIMITIVE_TYPE
        self.id = self._structure_definition["id"]
        self.has_snapshot = self._structure_definition.get("snapshot", None) is not None
        self.description = self._structure_definition.get("description", "")
        self.short = self._structure_definition.get("short", "")
        self.type = self._structure_definition["type"]
        self.base_class = self._get_base_class(type)

    @property
    def dependencies(self):
        complex_types = [e.type for e in self.elements if e.is_complex]
        complex_types = [t for t in complex_types if t != self.type]
        return list(set(complex_types))

    def _initialize_elements(self) -> list[GeneratorElement]:
        """Parse elements from the StructureDefinition to explicitly resolve
        the element name and type."""
        elements = self._structure_definition.get("snapshot", {}).get("element", [])
        parsed_elements = []
        [
            parsed_elements.extend(self._parse_element(element))
            for element in elements
            if not is_root_path(element["id"])
        ]
        return parsed_elements

    def _parse_element(self, element_definition: dict):
        """Parse name and type of a single ElementDefinition. Choice elements are
        expanded into multiple elements with the choice string '[x]' being replaced
        by the type. Elements where the type can not be resolved are skipped."""
        result = []
        types = element_definition.get("type", [])
        element_name = get_nth_part(element_definition["id"], -1)
        is_choice = is_choice_path(element_definition["path"])

        # Try to resolve missing types once
        if not types:
            element = self._resolve_missing_type(element_definition)
            if element:
                element_definition.update(element)
                types = element_definition.get("type", [])

        for type_info in types:
            type_code = type_info["code"]

            # Handle choice elements
            if is_choice:
                element_name = replace_choice_string(element_name, type_code)

            element = GeneratorElement(
                element_definition=element_definition,
                name=element_name,
                type=type_code,
            )
            result.append(element)

        return result

    def _resolve_missing_type(self, element_definition: dict):
        """Try to find an ElementDefinition with resolved type."""
        if element_definition.get("contentReference"):
            # try to resolve the type by resolving the content reference
            return self._resolve_content_reference(element_definition)
        return None

    def _resolve_content_reference(self, element_definition: dict):
        """Returns an ElementDefinition by resolving the content reference.
        More info: https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.contentReference
        """
        referenced_element = None
        content_reference_uri = element_definition.get("contentReference", None)
        parsed_uri = urlparse(content_reference_uri)
        if parsed_uri.fragment:
            # try to resolve the referenced element within local StructureDefinition
            referenced_element = self._get_original_element_by_id(parsed_uri.fragment)
        # TODO try to resolve the referenced element from another StructureDefinition
        return referenced_element

    def _get_original_element_by_id(self, id: str):
        """Get an ElementDefinition from the original input StructureDefinition."""
        elements = self._structure_definition["snapshot"]["element"]
        for element in elements:
            if element["id"] == id:
                return element
        return None

    def _get_base_class(self, type: str) -> str:
        """Returns the base class for the StructureDefinition."""
        if self.kind == StructureDefinitionKinds.RESOURCE:
            if type == "Base":
                return ModelBase.__name__
            elif type == "Resource":
                return "Base"
            elif type == "DomainResource":
                return "Resource"
            else:
                return "DomainResource"
        elif (
            self.kind == StructureDefinitionKinds.PRIMITIVE_TYPE
            or self.kind == StructureDefinitionKinds.COMPLEX_TYPE
        ):
            return "Element"
        else:
            return ModelBase.__name__
