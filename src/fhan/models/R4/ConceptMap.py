"""
Generated class for ConceptMap. 
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
from fhan.models.R4.DomainResource import *


class DependsOn(BaseModel):
    """A set of additional dependencies for this mapping to hold. This mapping is only applicable if the specified element can be resolved, and it has the specified value.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str property: Reference to property mapping depends on
    :param str system: Code System (if necessary)
    :param str value: Value of the referenced element
    :param str display: Display for the code (if value is a code)
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
        property: "str" = None,
        system: "str" = None,
        value: "str" = None,
        display: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.property = property
        self.system = system
        self.value = value
        self.display = display

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Target(BaseModel):
    """A concept from the target value set that this concept maps to.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies the target element
    :param str display: Display for the code
    :param str equivalence: relatedto | equivalent | equal | wider | subsumes | narrower | specializes | inexact | unmatched | disjoint
    :param str comment: Description of status/issues in mapping
    :param DependsOn dependsOn: Other elements required for this mapping (from context)
    :param Product product: Other concepts that this mapping also produces
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "dependsOn": {"class_name": "DependsOn", "is_contained": True},
        "product": {"class_name": "Product", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        display: "str" = None,
        equivalence: "str" = None,
        comment: "str" = None,
        dependsOn: list["DependsOn"] = None,
        product: list["Product"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.display = display
        self.equivalence = equivalence
        self.comment = comment
        self.dependsOn = dependsOn or []
        self.product = product or []

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Element(BaseModel):
    """Mappings for an individual concept in the source to one or more concepts in the target.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies element being mapped
    :param str display: Display for the code
    :param Target target: Concept in target system for element
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Target", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        display: "str" = None,
        target: list["Target"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.display = display
        self.target = target or []

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Unmapped(BaseModel):
    """What to do when there is no mapping for the source concept. "Unmapped" does not include codes that are unmatched, and the unmapped element is ignored in a code is specified to have equivalence = unmatched.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: provided | fixed | other-map
    :param str code: Fixed code when mode = fixed
    :param str display: Display for the code
    :param str url: canonical reference to an additional ConceptMap to use for mapping if the source concept is unmapped
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
        mode: "str" = None,
        code: "str" = None,
        display: "str" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode
        self.code = code
        self.display = display
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Group(BaseModel):
    """A group of mappings that all have the same source and target system.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str source: Source system where concepts to be mapped are defined
    :param str sourceVersion: Specific version of the  code system
    :param str target: Target system that the concepts are to be mapped to
    :param str targetVersion: Specific version of the  code system
    :param Element element: Mappings for a concept from the source set
    :param Unmapped unmapped: What to do when there is no mapping for the source concept
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "element": {"class_name": "Element", "is_contained": True},
        "unmapped": {"class_name": "Unmapped", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        source: "str" = None,
        sourceVersion: "str" = None,
        target: "str" = None,
        targetVersion: "str" = None,
        element: list["Element"] = None,
        unmapped: "Unmapped" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.source = source
        self.sourceVersion = sourceVersion
        self.target = target
        self.targetVersion = targetVersion
        self.element = element or []
        self.unmapped = unmapped

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ConceptMap(DomainResource):
    """A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this concept map, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the concept map
    :param str version: Business version of the concept map
    :param str name: Name for this concept map (computer friendly)
    :param str title: Name for this concept map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the concept map
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for concept map (if applicable)
    :param str purpose: Why this concept map is defined
    :param str copyright: Use and/or publishing restrictions
    :param str sourceUri: The source value set that contains the concepts that are being mapped
    :param str sourceCanonical: The source value set that contains the concepts that are being mapped
    :param str targetUri: The target value set which provides context for the mappings
    :param str targetCanonical: The target value set which provides context for the mappings
    :param Group group: Same source and target systems
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
        "group": {"class_name": "Group", "is_contained": True},
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
        identifier: "Identifier" = None,
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
        sourceUri: "str" = None,
        sourceCanonical: "str" = None,
        targetUri: "str" = None,
        targetCanonical: "str" = None,
        group: list["Group"] = None,
    ):
        self.resourceType = resourceType or "ConceptMap"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier
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
        self.sourceUri = sourceUri
        self.sourceCanonical = sourceCanonical
        self.targetUri = targetUri
        self.targetCanonical = targetCanonical
        self.group = group or []

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
