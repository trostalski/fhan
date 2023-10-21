"""
Generated class for TerminologyCapabilities. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Software(BaseModel):
    """Software that is covered by this terminology capability statement.  It is used when the statement describes the capabilities of a particular software version, independent of an installation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name the software is known by
    :param str version: Version covered by this statement
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
        name: "str" = None,
        version: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.version = version

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Implementation(BaseModel):
    """Identifies a specific implementation instance that is described by the terminology capability statement - i.e. a particular installation, rather than the capabilities of a software program.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Describes this specific instance
    :param str url: Base URL for the implementation
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
        description: "str" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Filter(BaseModel):
    """Filter Properties supported.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code of the property supported
    :param str op: Operations supported for the property
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
        op: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.op = op or []

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Version(BaseModel):
    """For the code system, a list of versions that are supported by the server.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Version identifier for this version
    :param bool isDefault: If this is the default version for this code system
    :param bool compositional: If compositional grammar is supported
    :param str language: Language Displays supported
    :param Filter filter: Filter Properties supported
    :param str property: Properties supported for $lookup
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "filter": {"class_name": "Filter", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        isDefault: "bool" = None,
        compositional: "bool" = None,
        language: list["str"] = None,
        filter: list["Filter"] = None,
        property: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.isDefault = isDefault
        self.compositional = compositional
        self.language = language or []
        self.filter = filter or []
        self.property = property or []

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CodeSystem(BaseModel):
    """Identifies a code system that is supported by the server. If there is a no code system URL, then this declares the general assumptions a client can make about support for any CodeSystem resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: URI for the Code System
    :param Version version: Version of Code System supported
    :param bool subsumption: Whether subsumption is supported
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "version": {"class_name": "Version", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        uri: "str" = None,
        version: list["Version"] = None,
        subsumption: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.uri = uri
        self.version = version or []
        self.subsumption = subsumption

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Parameter(BaseModel):
    """Supported expansion parameter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Expansion Parameter name
    :param str documentation: Description of support for parameter
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
        name: "str" = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Expansion(BaseModel):
    """Information about the [ValueSet/$expand](valueset-operation-expand.html) operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool hierarchical: Whether the server can return nested value sets
    :param bool paging: Whether the server supports paging on expansion
    :param bool incomplete: Allow request for incomplete expansions?
    :param Parameter parameter: Supported expansion parameter
    :param str textFilter: Documentation about text searching works
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "parameter": {"class_name": "Parameter", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        hierarchical: "bool" = None,
        paging: "bool" = None,
        incomplete: "bool" = None,
        parameter: list["Parameter"] = None,
        textFilter: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.hierarchical = hierarchical
        self.paging = paging
        self.incomplete = incomplete
        self.parameter = parameter or []
        self.textFilter = textFilter

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ValidateCode(BaseModel):
    """Information about the [ValueSet/$validate-code](valueset-operation-validate-code.html) operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translations: Whether translations are validated
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
        translations: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.translations = translations

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Translation(BaseModel):
    """Information about the [ConceptMap/$translate](conceptmap-operation-translate.html) operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool needsMap: Whether the client must identify the map
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
        needsMap: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.needsMap = needsMap

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Closure(BaseModel):
    """Whether the $closure operation is supported.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translation: If cross-system closure is supported
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
        translation: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.translation = translation

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class TerminologyCapabilities(DomainResource):
    """A TerminologyCapabilities resource documents a set of capabilities (behaviors) of a FHIR Terminology Server that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this terminology capabilities, represented as a URI (globally unique)
    :param str version: Business version of the terminology capabilities
    :param str name: Name for this terminology capabilities (computer friendly)
    :param str title: Name for this terminology capabilities (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the terminology capabilities
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for terminology capabilities (if applicable)
    :param str purpose: Why this terminology capabilities is defined
    :param str copyright: Use and/or publishing restrictions
    :param str kind: instance | capability | requirements
    :param Software software: Software that is covered by this terminology capability statement
    :param Implementation implementation: If this describes a specific instance
    :param bool lockedDate: Whether lockedDate is supported
    :param CodeSystem codeSystem: A code system supported by the server
    :param Expansion expansion: Information about the [ValueSet/$expand](valueset-operation-expand.html) operation
    :param str codeSearch: explicit | all
    :param ValidateCode validateCode: Information about the [ValueSet/$validate-code](valueset-operation-validate-code.html) operation
    :param Translation translation: Information about the [ConceptMap/$translate](conceptmap-operation-translate.html) operation
    :param Closure closure: Information about the [ConceptMap/$closure](conceptmap-operation-closure.html) operation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "software": {"class_name": "Software", "is_contained": True},
        "implementation": {"class_name": "Implementation", "is_contained": True},
        "codeSystem": {"class_name": "CodeSystem", "is_contained": True},
        "expansion": {"class_name": "Expansion", "is_contained": True},
        "validateCode": {"class_name": "ValidateCode", "is_contained": True},
        "translation": {"class_name": "Translation", "is_contained": True},
        "closure": {"class_name": "Closure", "is_contained": True},
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
        kind: "str" = None,
        software: "Software" = None,
        implementation: "Implementation" = None,
        lockedDate: "bool" = None,
        codeSystem: list["CodeSystem"] = None,
        expansion: "Expansion" = None,
        codeSearch: "str" = None,
        validateCode: "ValidateCode" = None,
        translation: "Translation" = None,
        closure: "Closure" = None,
    ):
        self.resourceType = resourceType or "TerminologyCapabilities"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
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
        self.kind = kind
        self.software = software
        self.implementation = implementation
        self.lockedDate = lockedDate
        self.codeSystem = codeSystem or []
        self.expansion = expansion
        self.codeSearch = codeSearch
        self.validateCode = validateCode
        self.translation = translation
        self.closure = closure

    @classmethod
    def from_dict(cls, data: dict) -> "TerminologyCapabilities":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TerminologyCapabilities":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
