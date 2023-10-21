"""
Generated class for OperationDefinition. 
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


class Binding(BaseModel):
    """Binds to a value set if this parameter is coded (code, Coding, CodeableConcept).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str strength: required | extensible | preferred | example
    :param str valueSet: Source of value set
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
        strength: "str" = None,
        valueSet: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.strength = strength
        self.valueSet = valueSet

    @classmethod
    def from_dict(cls, data: dict) -> "OperationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ReferencedFrom(BaseModel):
    """Identifies other resource parameters within the operation invocation that are expected to resolve to this resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str source: Referencing parameter
    :param str sourceId: Element id of reference
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
        source: "str" = None,
        sourceId: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.source = source
        self.sourceId = sourceId

    @classmethod
    def from_dict(cls, data: dict) -> "OperationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Parameter(BaseModel):
    """The parameters for the operation/query.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name in Parameters.parameter.name or in URL
    :param str use: in | out
    :param int min: Minimum Cardinality
    :param str max: Maximum Cardinality (a number or *)
    :param str documentation: Description of meaning/use
    :param str type: What type this parameter has
    :param str targetProfile: If type is Reference | canonical, allowed targets
    :param str searchType: number | date | string | token | reference | composite | quantity | uri | special
    :param Binding binding: ValueSet details if this is coded
    :param ReferencedFrom referencedFrom: References to this parameter
    :param Part part: Parts of a nested Parameter
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "binding": {"class_name": "Binding", "is_contained": True},
        "referencedFrom": {"class_name": "ReferencedFrom", "is_contained": True},
        "part": {"class_name": "Part", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        use: "str" = None,
        min: "int" = None,
        max: "str" = None,
        documentation: "str" = None,
        type: "str" = None,
        targetProfile: list["str"] = None,
        searchType: "str" = None,
        binding: "Binding" = None,
        referencedFrom: list["ReferencedFrom"] = None,
        part: list["Part"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.use = use
        self.min = min
        self.max = max
        self.documentation = documentation
        self.type = type
        self.targetProfile = targetProfile or []
        self.searchType = searchType
        self.binding = binding
        self.referencedFrom = referencedFrom or []
        self.part = part or []

    @classmethod
    def from_dict(cls, data: dict) -> "OperationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Overload(BaseModel):
    """Defines an appropriate combination of parameters to use when invoking this operation, to help code generators when generating overloaded parameter sets for this operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str parameterName: Name of parameter to include in overload
    :param str comment: Comments to go on overload
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
        parameterName: list["str"] = None,
        comment: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.parameterName = parameterName or []
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "OperationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class OperationDefinition(DomainResource):
    """A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this operation definition, represented as a URI (globally unique)
    :param str version: Business version of the operation definition
    :param str name: Name for this operation definition (computer friendly)
    :param str title: Name for this operation definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: operation | query
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the operation definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for operation definition (if applicable)
    :param str purpose: Why this operation definition is defined
    :param bool affectsState: Whether content is changed by the operation
    :param str code: Name used to invoke the operation
    :param str comment: Additional information about use
    :param str base: Marks this as a profile of the base
    :param str resource: Types this operation applies to
    :param bool system: Invoke at the system level?
    :param bool type: Invoke at the type level?
    :param bool instance: Invoke on an instance?
    :param str inputProfile: Validation information for in parameters
    :param str outputProfile: Validation information for out parameters
    :param Parameter parameter: Parameters for the operation/query
    :param Overload overload: Define overloaded variants for when  generating code
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
        "parameter": {"class_name": "Parameter", "is_contained": True},
        "overload": {"class_name": "Overload", "is_contained": True},
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
        kind: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        affectsState: "bool" = None,
        code: "str" = None,
        comment: "str" = None,
        base: "str" = None,
        resource: list["str"] = None,
        system: "bool" = None,
        type: "bool" = None,
        instance: "bool" = None,
        inputProfile: "str" = None,
        outputProfile: "str" = None,
        parameter: list["Parameter"] = None,
        overload: list["Overload"] = None,
    ):
        self.resourceType = resourceType or "OperationDefinition"
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
        self.kind = kind
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.affectsState = affectsState
        self.code = code
        self.comment = comment
        self.base = base
        self.resource = resource or []
        self.system = system
        self.type = type
        self.instance = instance
        self.inputProfile = inputProfile
        self.outputProfile = outputProfile
        self.parameter = parameter or []
        self.overload = overload or []

    @classmethod
    def from_dict(cls, data: dict) -> "OperationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
