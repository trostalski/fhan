"""
Generated class for ValueSet. 
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


class Designation(BaseModel):
    """Additional representations for this concept when used in this value set - other languages, aliases, specialized purposes, used for particular purposes, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: Human language of the designation
    :param Coding use: Types of uses of designations
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
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Concept(BaseModel):
    """Specifies a concept to be included or excluded.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code or expression from system
    :param str display: Text to display for this code for this value set in this valueset
    :param Designation designation: Additional representations for this concept
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "designation": {"class_name": "Designation", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        display: "str" = None,
        designation: list["Designation"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.display = display
        self.designation = designation or []

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Filter(BaseModel):
    """Select concepts by specify a matching criterion based on the properties (including relationships) defined by the system, or on filters defined by the system. If multiple filters are specified, they SHALL all be true.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str property: A property/filter defined by the code system
    :param str op: = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    :param str value: Code from the system, or regex criteria, or boolean value for exists
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
        op: "str" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.property = property
        self.op = op
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Include(BaseModel):
    """Include one or more codes from a code system or other value set(s).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: The system the codes come from
    :param str version: Specific version of the code system referred to
    :param Concept concept: A concept defined in the system
    :param Filter filter: Select codes/concepts by their properties (including relationships)
    :param str valueSet: Select the contents included in this value set
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "concept": {"class_name": "Concept", "is_contained": True},
        "filter": {"class_name": "Filter", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        system: "str" = None,
        version: "str" = None,
        concept: list["Concept"] = None,
        filter: list["Filter"] = None,
        valueSet: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.system = system
        self.version = version
        self.concept = concept or []
        self.filter = filter or []
        self.valueSet = valueSet or []

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Compose(BaseModel):
    """A set of criteria that define the contents of the value set by including or excluding codes selected from the specified code system(s) that the value set draws from. This is also known as the Content Logical Definition (CLD).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lockedDate: Fixed date for references with no specified version (transitive)
    :param bool inactive: Whether inactive codes are in the value set
    :param Include include: Include one or more codes from a code system or other value set(s)
    :param Exclude exclude: Explicitly exclude codes from a code system or other value sets
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "include": {"class_name": "Include", "is_contained": True},
        "exclude": {"class_name": "Exclude", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        lockedDate: "str" = None,
        inactive: "bool" = None,
        include: list["Include"] = None,
        exclude: list["Exclude"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.lockedDate = lockedDate
        self.inactive = inactive
        self.include = include or []
        self.exclude = exclude or []

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Parameter(BaseModel):
    """A parameter that controlled the expansion process. These parameters may be used by users of expanded value sets to check whether the expansion is suitable for a particular purpose, or to pick the correct expansion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name as assigned by the client or server
    :param str valueString: Value of the named parameter
    :param bool valueBoolean: Value of the named parameter
    :param int valueInteger: Value of the named parameter
    :param float valueDecimal: Value of the named parameter
    :param str valueUri: Value of the named parameter
    :param str valueCode: Value of the named parameter
    :param str valueDateTime: Value of the named parameter
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
        valueString: "str" = None,
        valueBoolean: "bool" = None,
        valueInteger: "int" = None,
        valueDecimal: "float" = None,
        valueUri: "str" = None,
        valueCode: "str" = None,
        valueDateTime: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.valueString = valueString
        self.valueBoolean = valueBoolean
        self.valueInteger = valueInteger
        self.valueDecimal = valueDecimal
        self.valueUri = valueUri
        self.valueCode = valueCode
        self.valueDateTime = valueDateTime

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Contains(BaseModel):
    """The codes that are contained in the value set expansion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: System value for the code
    :param bool abstract: If user cannot select this entry
    :param bool inactive: If concept is inactive in the code system
    :param str version: Version in which this code/display is defined
    :param str code: Code - if blank, this is not a selectable code
    :param str display: User display for the concept
    :param Designation designation: Additional representations for this item
    :param Contains contains: Codes contained under this entry
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "designation": {"class_name": "Designation", "is_contained": True},
        "contains": {"class_name": "Contains", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        system: "str" = None,
        abstract: "bool" = None,
        inactive: "bool" = None,
        version: "str" = None,
        code: "str" = None,
        display: "str" = None,
        designation: list["Designation"] = None,
        contains: list["Contains"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.system = system
        self.abstract = abstract
        self.inactive = inactive
        self.version = version
        self.code = code
        self.display = display
        self.designation = designation or []
        self.contains = contains or []

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Expansion(BaseModel):
    """A value set can also be "expanded", where the value set is turned into a simple collection of enumerated codes. This element holds the expansion, if it has been performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identifier: Identifies the value set expansion (business identifier)
    :param str timestamp: Time ValueSet expansion happened
    :param int total: Total number of codes in the expansion
    :param int offset: Offset at which this resource starts
    :param Parameter parameter: Parameter that controlled the expansion process
    :param Contains contains: Codes in the value set
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "parameter": {"class_name": "Parameter", "is_contained": True},
        "contains": {"class_name": "Contains", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "str" = None,
        timestamp: "str" = None,
        total: "int" = None,
        offset: "int" = None,
        parameter: list["Parameter"] = None,
        contains: list["Contains"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.timestamp = timestamp
        self.total = total
        self.offset = offset
        self.parameter = parameter or []
        self.contains = contains or []

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ValueSet(DomainResource):
    """A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this value set, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the value set (business identifier)
    :param str version: Business version of the value set
    :param str name: Name for this value set (computer friendly)
    :param str title: Name for this value set (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the value set
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for value set (if applicable)
    :param bool immutable: Indicates whether or not any change to the content logical definition may occur
    :param str purpose: Why this value set is defined
    :param str copyright: Use and/or publishing restrictions
    :param Compose compose: Content logical definition of the value set (CLD)
    :param Expansion expansion: Used when the value set is "expanded"
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
        "compose": {"class_name": "Compose", "is_contained": True},
        "expansion": {"class_name": "Expansion", "is_contained": True},
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
        immutable: "bool" = None,
        purpose: "str" = None,
        copyright: "str" = None,
        compose: "Compose" = None,
        expansion: "Expansion" = None,
    ):
        self.resourceType = resourceType or "ValueSet"
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
        self.immutable = immutable
        self.purpose = purpose
        self.copyright = copyright
        self.compose = compose
        self.expansion = expansion

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
