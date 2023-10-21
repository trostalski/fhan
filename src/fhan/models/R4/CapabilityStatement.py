"""
Generated class for CapabilityStatement. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Software(BaseModel):
    """Software that is covered by this capability statement.  It is used when the capability statement describes the capabilities of a particular software version, independent of an installation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name the software is known by
    :param str version: Version covered by this statement
    :param str releaseDate: Date this version was released
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
        releaseDate: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.version = version
        self.releaseDate = releaseDate

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Implementation(BaseModel):
    """Identifies a specific implementation instance that is described by the capability statement - i.e. a particular installation, rather than the capabilities of a software program.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Describes this specific instance
    :param str url: Base URL for the installation
    :param Reference custodian: Organization that manages the data
    :param str implementationGuide: Implementation guides supported
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "custodian": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        url: "str" = None,
        custodian: "Reference" = None,
        implementationGuide: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.url = url
        self.custodian = custodian
        self.implementationGuide = implementationGuide or []

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Security(BaseModel):
    """Information about security implementation from an interface perspective - what a client needs to know.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool cors: Adds CORS Headers (http://enable-cors.org/)
    :param CodeableConcept service: OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates
    :param str description: General description of how security works
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "service": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        cors: "bool" = None,
        service: list["CodeableConcept"] = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.cors = cors
        self.service = service or []
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Interaction(BaseModel):
    """Identifies a restful operation supported by the solution.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: read | vread | update | patch | delete | history-instance | history-type | create | search-type
    :param str documentation: Anything special about operation behavior
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
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SearchParam(BaseModel):
    """Search parameters for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of search parameter
    :param str definition: Source of definition for parameter
    :param str type: number | date | string | token | reference | composite | quantity | uri | special
    :param str documentation: Server-specific usage
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
        definition: "str" = None,
        type: "str" = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.definition = definition
        self.type = type
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Operation(BaseModel):
    """Definition of an operation or a named query together with its parameters and their meaning and type. Consult the definition of the operation for details about how to invoke the operation, and the parameters.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name by which the operation/query is invoked
    :param str definition: The defined operation/query
    :param str documentation: Specific details about operation behavior
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
        definition: "str" = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.definition = definition
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Resource(BaseModel):
    """A specification of the restful capabilities of the solution for a specific resource type.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: A resource type that is supported
    :param str profile: Base System profile for all uses of resource
    :param str supportedProfile: Profiles for use cases supported
    :param str documentation: Additional information about the use of the resource type
    :param Interaction interaction: What operations are supported?
    :param str versioning: no-version | versioned | versioned-update
    :param bool readHistory: Whether vRead can return past versions
    :param bool updateCreate: If update can commit to a new identity
    :param bool conditionalCreate: If allows/uses conditional create
    :param str conditionalRead: not-supported | modified-since | not-match | full-support
    :param bool conditionalUpdate: If allows/uses conditional update
    :param str conditionalDelete: not-supported | single | multiple - how conditional delete is supported
    :param str referencePolicy: literal | logical | resolves | enforced | local
    :param str searchInclude: _include values supported by the server
    :param str searchRevInclude: _revinclude values supported by the server
    :param SearchParam searchParam: Search parameters supported by implementation
    :param Operation operation: Definition of a resource operation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "interaction": {"class_name": "Interaction", "is_contained": True},
        "searchParam": {"class_name": "SearchParam", "is_contained": True},
        "operation": {"class_name": "Operation", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        profile: "str" = None,
        supportedProfile: list["str"] = None,
        documentation: "str" = None,
        interaction: list["Interaction"] = None,
        versioning: "str" = None,
        readHistory: "bool" = None,
        updateCreate: "bool" = None,
        conditionalCreate: "bool" = None,
        conditionalRead: "str" = None,
        conditionalUpdate: "bool" = None,
        conditionalDelete: "str" = None,
        referencePolicy: list["str"] = None,
        searchInclude: list["str"] = None,
        searchRevInclude: list["str"] = None,
        searchParam: list["SearchParam"] = None,
        operation: list["Operation"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.profile = profile
        self.supportedProfile = supportedProfile or []
        self.documentation = documentation
        self.interaction = interaction or []
        self.versioning = versioning
        self.readHistory = readHistory
        self.updateCreate = updateCreate
        self.conditionalCreate = conditionalCreate
        self.conditionalRead = conditionalRead
        self.conditionalUpdate = conditionalUpdate
        self.conditionalDelete = conditionalDelete
        self.referencePolicy = referencePolicy or []
        self.searchInclude = searchInclude or []
        self.searchRevInclude = searchRevInclude or []
        self.searchParam = searchParam or []
        self.operation = operation or []

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Interaction(BaseModel):
    """A specification of restful operations supported by the system.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: transaction | batch | search-system | history-system
    :param str documentation: Anything special about operation behavior
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
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Rest(BaseModel):
    """A definition of the restful capabilities of the solution, if any.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: client | server
    :param str documentation: General description of implementation
    :param Security security: Information about security of implementation
    :param Resource resource: Resource served on the REST interface
    :param Interaction interaction: What operations are supported?
    :param SearchParam searchParam: Search parameters for searching all resources
    :param Operation operation: Definition of a system level operation
    :param str compartment: Compartments served/used by system
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "security": {"class_name": "Security", "is_contained": True},
        "resource": {"class_name": "Resource", "is_contained": True},
        "interaction": {"class_name": "Interaction", "is_contained": True},
        "searchParam": {"class_name": "SearchParam", "is_contained": True},
        "operation": {"class_name": "Operation", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        mode: "str" = None,
        documentation: "str" = None,
        security: "Security" = None,
        resource: list["Resource"] = None,
        interaction: list["Interaction"] = None,
        searchParam: list["SearchParam"] = None,
        operation: list["Operation"] = None,
        compartment: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode
        self.documentation = documentation
        self.security = security
        self.resource = resource or []
        self.interaction = interaction or []
        self.searchParam = searchParam or []
        self.operation = operation or []
        self.compartment = compartment or []

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Endpoint(BaseModel):
    """An endpoint (network accessible address) to which messages and/or replies are to be sent.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding protocol: http | ftp | mllp +
    :param str address: Network address or identifier of the end-point
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "protocol": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        protocol: "Coding" = None,
        address: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.protocol = protocol
        self.address = address

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SupportedMessage(BaseModel):
    """References to message definitions for messages this system can send or receive.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: sender | receiver
    :param str definition: Message supported by this system
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
        definition: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode
        self.definition = definition

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Messaging(BaseModel):
    """A description of the messaging capabilities of the solution.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Endpoint endpoint: Where messages should be sent
    :param int reliableCache: Reliable Message Cache Length (min)
    :param str documentation: Messaging interface behavior details
    :param SupportedMessage supportedMessage: Messages supported by this system
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "endpoint": {"class_name": "Endpoint", "is_contained": True},
        "supportedMessage": {"class_name": "SupportedMessage", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        endpoint: list["Endpoint"] = None,
        reliableCache: "int" = None,
        documentation: "str" = None,
        supportedMessage: list["SupportedMessage"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.endpoint = endpoint or []
        self.reliableCache = reliableCache
        self.documentation = documentation
        self.supportedMessage = supportedMessage or []

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Document(BaseModel):
    """A document definition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: producer | consumer
    :param str documentation: Description of document support
    :param str profile: Constraint on the resources used in the document
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
        documentation: "str" = None,
        profile: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode
        self.documentation = documentation
        self.profile = profile

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CapabilityStatement(DomainResource):
    """A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this capability statement, represented as a URI (globally unique)
    :param str version: Business version of the capability statement
    :param str name: Name for this capability statement (computer friendly)
    :param str title: Name for this capability statement (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the capability statement
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for capability statement (if applicable)
    :param str purpose: Why this capability statement is defined
    :param str copyright: Use and/or publishing restrictions
    :param str kind: instance | capability | requirements
    :param str instantiates: Canonical URL of another capability statement this implements
    :param str imports: Canonical URL of another capability statement this adds to
    :param Software software: Software that is covered by this capability statement
    :param Implementation implementation: If this describes a specific instance
    :param str fhirVersion: FHIR Version the system supports
    :param str format: formats supported (xml | json | ttl | mime type)
    :param str patchFormat: Patch formats supported
    :param Rest rest: If the endpoint is a RESTful one
    :param Messaging messaging: If messaging is supported
    :param Document document: Document definition
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
        "rest": {"class_name": "Rest", "is_contained": True},
        "messaging": {"class_name": "Messaging", "is_contained": True},
        "document": {"class_name": "Document", "is_contained": True},
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
        instantiates: list["str"] = None,
        imports: list["str"] = None,
        software: "Software" = None,
        implementation: "Implementation" = None,
        fhirVersion: "str" = None,
        format: list["str"] = None,
        patchFormat: list["str"] = None,
        rest: list["Rest"] = None,
        messaging: list["Messaging"] = None,
        document: list["Document"] = None,
    ):
        self.resourceType = resourceType or "CapabilityStatement"
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
        self.instantiates = instantiates or []
        self.imports = imports or []
        self.software = software
        self.implementation = implementation
        self.fhirVersion = fhirVersion
        self.format = format or []
        self.patchFormat = patchFormat or []
        self.rest = rest or []
        self.messaging = messaging or []
        self.document = document or []

    @classmethod
    def from_dict(cls, data: dict) -> "CapabilityStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CapabilityStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
