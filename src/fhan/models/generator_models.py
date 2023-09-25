from urllib.parse import urlparse
from enum import Enum
import os
from importlib import import_module
import inspect

from fhan.core.data_types import PYTHON_KEYWORDS
from fhan.core.utils.path_utils import remove_n_parts_from_end
from fhan.core.data_types import get_python_type_for_primitive, is_primitive_type
from fhan.core.utils.path_utils import (
    is_choice_path,
    replace_choice_string,
    get_nth_part,
    is_root_path,
)


class StructureDefinitionKinds(Enum):
    PRIMITIVE_TYPE = "primitive-type"
    COMPLEX_TYPE = "complex-type"
    RESOURCE = "resource"
    LOGICAL = "logical"


class ModelBase:
    """Base class for all generated models."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class GeneratorElement:
    """Wrapper around a ElementDefinition with a parsed name and type"""

    def __init__(
        self,
        element_definition: dict,
        name: str,
        type: str,
        children: list["GeneratorElement"] = None,
    ):
        children = children or []
        self._element = element_definition
        self.id = element_definition["id"]
        self.type = type
        self.path: str = element_definition["path"]
        self.name = _escape_keyword(name) if name in PYTHON_KEYWORDS else name
        self.min, self.max = self._get_cardinalities()
        self.is_primitive = is_primitive_type(self.type)
        self.description = element_definition.get("definition", "")
        self.short = element_definition.get("short", "")
        self.python_type = (
            get_python_type_for_primitive(self.type) if self.is_primitive else None
        )
        self.base_class, self.base_import_string = _get_base_class(
            kind=StructureDefinitionKinds.COMPLEX_TYPE.value, type=self.type
        )
        (
            self.contained_children,
            self.defined_children,
        ) = _filter_contained_elements(children)

    @property
    def is_array(self):
        return self.max > 1

    @property
    def type_string(self):
        """Type used for the jinja template"""
        if self.is_primitive:  # primitive with python type
            return self.python_type.__name__
        if self.is_array:
            return f"list['{self.type}']"
        else:
            return f"'{self.type}'"

    def __eq__(self, __value: "GeneratorElement") -> bool:
        """Compares two GeneratorElements by their path, type, name and id.
        Primarily used to filter duplicate elements."""
        return (
            self.path == __value.path
            and self.type == __value.type
            and self.name == __value.name
            and self.id == __value.id
        )

    def _get_cardinalities(self) -> tuple[float, float]:
        """Returns the min and max cardinality of the ElementDefinition."""
        min = self._element.get("min", None)
        max = self._element.get("max", None)
        if max == "*":
            max = float("inf")
        return float(min), float(max)


class GeneratorStructureDefinition:
    """Represents a FHIR StructureDefinition that is used to generate downsream objects."""

    def __init__(self, structure_definition: dict):
        self._structure_definition = structure_definition
        self._element_definitions = structure_definition.get("snapshot", {}).get(
            "element", []
        )
        self.generator_elements = self._initialize_elements(self._element_definitions)
        (
            self.contained_elements,
            self.defined_elements,
        ) = _filter_contained_elements(self.generator_elements)
        self.kind = self._structure_definition["kind"]
        self.is_primitive = self.kind == StructureDefinitionKinds.PRIMITIVE_TYPE.value
        self.id = self._structure_definition["id"]
        self.has_snapshot = self._structure_definition.get("snapshot", None) is not None
        self.description = self._structure_definition.get("description", "")
        self.short = self._structure_definition.get("short", "")
        self.type = self._structure_definition["type"]
        self.base_class, self.base_import_string = _get_base_class(
            kind=self.kind, type=self.type
        )
        # TODO: For now structure definitions with same id and type are considered base classes, but this is might always true
        self.is_base = self.id == self.type

    @property
    def dependencies(self):
        """Unique list of dependencies for this StructureDefinition. Used to generate
        the import statements for the generated class."""
        complex_types = [e.type for e in self.generator_elements if not e.is_primitive]
        # avoid circles
        complex_types = [t for t in complex_types if t != self.type]
        return list(set(complex_types))

    def _initialize_elements(self, element_definitions) -> list[GeneratorElement]:
        """Parse elements from the StructureDefinition to explicitly resolve
        the element name and type."""
        parsed_elements = []
        for element_definition in element_definitions:
            if is_root_path(element_definition["id"]):
                continue
            parsed_elements.extend(self._parse_element(element_definition))
        return parsed_elements

    def _parse_element(self, element_definition: dict) -> list[GeneratorElement]:
        """Parse name and type of a single ElementDefinition. Choice elements are
        expanded into multiple elements with the choice string '[x]' being replaced
        by the type. Elements where the type can not be resolved are skipped."""
        result = []
        types = element_definition.get("type", [])
        element_name = get_nth_part(element_definition["id"], -1)
        choice_element_name = None
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
                choice_element_name = replace_choice_string(
                    path=element_name, replace=_capitalize_first_letter(type_code)
                )

            element = GeneratorElement(
                element_definition=element_definition,
                name=choice_element_name or element_name,
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


def _filter_contained_elements(
    elements: list[GeneratorElement],
) -> tuple[list[GeneratorElement], list[GeneratorElement]]:
    """Filters the given elements for Elements that are defined within the resource.
    They are treated separately in the template because the type is not knonw before
    parsing the StructureDefinition."""
    contained_generator_elements = []  # Elements of type BackboneElement or Element
    defined_generator_elements = []
    seen_elements = []
    for element in elements:
        if element in seen_elements:  # Can't use path because of choice elements
            continue
        seen_elements.append(element)  # Add the element to the set
        if element.type == "BackboneElement" or element.type == "Element":
            children = [
                e
                for e in elements
                if e.path.startswith(element.path)
                and e.path
                != element.path  # All children of the contained element without the element itself
            ]
            seen_elements.extend(children)  # Add children to the seen elements
            contained_element = GeneratorElement(
                element_definition=element._element,
                name=element.name,
                type=_capitalize_first_letter(element.name),
                children=children,
            )
            contained_generator_elements.append(contained_element)
            # Contained Element is now defined (type is known, itself), its children are not
            defined_generator_elements.append(contained_element)
        else:
            defined_generator_elements.append(element)
    return contained_generator_elements, defined_generator_elements


def _get_base_class(kind: str, type: str) -> tuple[str, str]:
    """Returns the base class according to the fhir spec
    and its import string for a StructureDefinition.
    If the base class is generated by the generator, the import string is None."""

    class_str = ModelBase.__name__
    import_str = _import_string_for_path(os.path.abspath(__file__))

    if kind == StructureDefinitionKinds.RESOURCE.value:
        if type == "Resource":
            return class_str, import_str
        if type == "DomainResource":
            return "Resource", None
        else:
            return "DomainResource", None
    else:
        return class_str, import_str


def _escape_keyword(name: str) -> str:
    """Escapes a Python keyword."""
    return f"_{name}"


def _import_string_for_path(path: str):
    """Returns the import string for the given path relative
    to src directory."""
    if "src/" in path:
        path = path.split("src/")[-1]
    if ".py" in path:
        path = path.split(".py")[0]
    import_str = path.replace("/", ".")
    return import_str


def _capitalize_first_letter(string: str) -> str:
    """Capitalize the first letter of a string. Used parse
    choice types."""
    return string[0].upper() + string[1:]
