import json
from urllib.parse import urlparse
from enum import Enum
import os

from fhan.core.data_types import PYTHON_KEYWORDS
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

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class GeneratorElement:
    """Wrapper around a ElementDefinition with a parsed name and type"""

    def __init__(self, element_definition: dict, name: str, type: str):
        self._element = element_definition
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

    @property
    def is_array(self):
        return self.max > 1

    def _get_cardinalities(self) -> tuple[float, float]:
        """Returns the min and max cardinality of the ElementDefinition."""
        min = self._element.get("min", None)
        max = self._element.get("max", None)
        if max == "*":
            max = float("inf")
        return float(min), float(max)


class GeneratorBackboneElement(GeneratorElement):
    def __init__(
        self,
        element_definition: dict,
        name: str,
        type: str,
        children: list[GeneratorElement],
    ):
        super().__init__(element_definition, name, type)
        self.children = children
        self.base_class, self.base_import_string = _get_base_class(
            kind=StructureDefinitionKinds.COMPLEX_TYPE.value, type=self.type
        )


class GeneratorStructureDefinition:
    """Represents a FHIR StructureDefinition that is used to generate downsream objects."""

    def __init__(self, structure_definition: dict):
        self._structure_definition = structure_definition
        self._element_definitions = structure_definition.get("snapshot", {}).get(
            "element", []
        )
        self.generator_elements = self._initialize_elements(self._element_definitions)
        (
            self.backbone_generator_elements,
            self.defined_generator_elements,
        ) = self._filter_backbone_generator_elements(self.generator_elements)
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

    @property
    def dependencies(self):
        """Unique list of dependencies for this StructureDefinition. Used to generate
        the import statements for the generated class."""
        complex_types = [e.type for e in self.generator_elements if not e.is_primitive]
        complex_types = [t for t in complex_types if t != self.type]
        if self.backbone_generator_elements:
            complex_types.append(self.backbone_generator_elements[0].base_class)
        return list(set(complex_types))

    def _initialize_elements(self, element_definitions) -> list[GeneratorElement]:
        """Parse elements from the StructureDefinition to explicitly resolve
        the element name and type."""
        parsed_elements = []
        [
            parsed_elements.extend(self._parse_element(element_definition))
            for element_definition in element_definitions
            if not is_root_path(
                element_definition["id"]
            )  # skip root element of StructureDefinition, they dont have a type
        ]
        return parsed_elements

    def _parse_element(self, element_definition: dict) -> list[GeneratorElement]:
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

    def _filter_backbone_generator_elements(
        self, elements: list[GeneratorElement]
    ) -> tuple[list[GeneratorBackboneElement], list[GeneratorElement]]:
        """Filters the given elements for BackboneElements and None-BackboneElements.
        BackboneElements are Elements that defined within a resource."""
        backbone_generator_elements = []
        defined_generator_elements = []
        for element in elements:
            if element.type == "BackboneElement":
                children = [
                    e
                    for e in self.generator_elements
                    if e.path.startswith(element.path)
                ]
                backbone_generator_elements.append(
                    GeneratorBackboneElement(
                        element_definition=element._element,
                        name=element.name,
                        type=element.type,
                        children=children,
                    )
                )
                # backbone element is now defined, its children are not
                defined_generator_elements.append(element)
            else:
                defined_generator_elements.append(element)
        return backbone_generator_elements, defined_generator_elements

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


def _get_base_class(kind: str, type: str) -> tuple[str, str]:
    """Returns the base class and its import string for a StructureDefinition.
    The base class is determined by the kind of the StructureDefinition.
    If the base class is generated by the generator, the import string is None."""

    class_str = ModelBase.__name__
    import_str = _import_string_for_path(os.path.abspath(__file__))

    if kind == StructureDefinitionKinds.RESOURCE.value:
        if type == "DomainResource":
            class_str = "Resource"
            import_str = None
    elif (
        kind == StructureDefinitionKinds.PRIMITIVE_TYPE.value
        or kind == StructureDefinitionKinds.COMPLEX_TYPE.value
    ):
        if type == "Element":
            class_str = None
            import_str = None
        else:
            class_str = "Element"
            import_str = None

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
