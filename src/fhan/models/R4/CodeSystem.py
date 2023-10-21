"""
Generated class for CodeSystem. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class Filter(BaseModel):
    """A filter that can be used in a value set compose statement when selecting concepts using a filter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies the filter
    :param str description: How or why the filter is used
    :param str operator: = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    :param str value: What to use for the value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        description: "str" = None,
        operator: list["str"] = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.description = description
        self.operator = operator or []
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "CodeSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Property(BaseModel):
    """A property defines an additional slot through which additional information can be provided about a concept.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies the property on the concepts, and when referred to in operations
    :param str uri: Formal identifier for the property
    :param str description: Why the property is defined, and/or what it conveys
    :param str type: code | Coding | string | integer | boolean | dateTime | decimal
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        uri: "str" = None,
        description: "str" = None,
        type: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.uri = uri
        self.description = description
        self.type = type

    @classmethod
    def from_dict(cls, data: dict) -> "CodeSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Designation(BaseModel):
    """Additional representations for the concept - other languages, aliases, specialized purposes, used for particular purposes, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: Human language of the designation
    :param Coding use: Details how this designation would be used
    :param str value: The text value for this designation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "use": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        language: "str" = None,
        use: "Coding" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.language = language
        self.use = use
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "CodeSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Property(BaseModel):
    """A property value for this concept.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to CodeSystem.property.code
    :param str valueCode: Value of the property for this concept
    :param Coding valueCoding: Value of the property for this concept
    :param str valueString: Value of the property for this concept
    :param int valueInteger: Value of the property for this concept
    :param bool valueBoolean: Value of the property for this concept
    :param str valueDateTime: Value of the property for this concept
    :param float valueDecimal: Value of the property for this concept
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "valueCoding": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        valueCode: "str" = None,
        valueCoding: "Coding" = None,
        valueString: "str" = None,
        valueInteger: "int" = None,
        valueBoolean: "bool" = None,
        valueDateTime: "str" = None,
        valueDecimal: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.valueCode = valueCode
        self.valueCoding = valueCoding
        self.valueString = valueString
        self.valueInteger = valueInteger
        self.valueBoolean = valueBoolean
        self.valueDateTime = valueDateTime
        self.valueDecimal = valueDecimal

    @classmethod
    def from_dict(cls, data: dict) -> "CodeSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Concept(BaseModel):
    """Concepts that are in the code system. The concept definitions are inherently hierarchical, but the definitions must be consulted to determine what the meanings of the hierarchical relationships are.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies concept
    :param str display: Text to display to the user
    :param str definition: Formal definition
    :param Designation designation: Additional representations for the concept
    :param Property property: Property value for the concept
    :param Concept concept: Child Concepts (is-a/contains/categorizes)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "designation": {"class_name": "Designation", "is_contained": True},
        "property": {"class_name": "Property", "is_contained": True},
        "concept": {"class_name": "Concept", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        display: "str" = None,
        definition: "str" = None,
        designation: list["Designation"] = None,
        property: list["Property"] = None,
        concept: list["Concept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.display = display
        self.definition = definition
        self.designation = designation or []
        self.property = property or []
        self.concept = concept or []

    @classmethod
    def from_dict(cls, data: dict) -> "CodeSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CodeSystem(DomainResource):
    """The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system)
    :param Identifier identifier: Additional identifier for the code system (business identifier)
    :param str version: Business version of the code system (Coding.version)
    :param str name: Name for this code system (computer friendly)
    :param str title: Name for this code system (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the code system
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for code system (if applicable)
    :param str purpose: Why this code system is defined
    :param str copyright: Use and/or publishing restrictions
    :param bool caseSensitive: If code comparison is case sensitive
    :param str valueSet: Canonical reference to the value set with entire code system
    :param str hierarchyMeaning: grouped-by | is-a | part-of | classified-with
    :param bool compositional: If code system defines a compositional grammar
    :param bool versionNeeded: If definitions are not stable
    :param str content: not-present | example | fragment | complete | supplement
    :param str supplements: Canonical URL of Code System this adds designations and properties to
    :param int count: Total concepts in the code system
    :param Filter filter: Filter that can be used in a value set
    :param Property property: Additional information supplied about each concept
    :param Concept concept: Concepts in the code system
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "filter": {"class_name": "Filter", "is_contained": True},
        "property": {"class_name": "Property", "is_contained": True},
        "concept": {"class_name": "Concept", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        name: "str" = None,
        title: "str" = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        copyright: "str" = None,
        caseSensitive: "bool" = None,
        valueSet: "str" = None,
        hierarchyMeaning: "str" = None,
        compositional: "bool" = None,
        versionNeeded: "bool" = None,
        content: "str" = None,
        supplements: "str" = None,
        count: "int" = None,
        filter: list["Filter"] = None,
        property: list["Property"] = None,
        concept: list["Concept"] = None,
    ):
        self.resourceType = resourceType or "CodeSystem"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.name = name
        self.title = title
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.copyright = copyright
        self.caseSensitive = caseSensitive
        self.valueSet = valueSet
        self.hierarchyMeaning = hierarchyMeaning
        self.compositional = compositional
        self.versionNeeded = versionNeeded
        self.content = content
        self.supplements = supplements
        self.count = count
        self.filter = filter or []
        self.property = property or []
        self.concept = concept or []

    @classmethod
    def from_dict(cls, data: dict) -> "CodeSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
