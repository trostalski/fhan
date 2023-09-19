"""
Generated class for CapabilityStatement. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class CapabilityStatement(ModelBase):
    """ A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
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
    :param BackboneElement software: Software that is covered by this capability statement
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name the software is known by
    :param str version: Version covered by this statement
    :param str releaseDate: Date this version was released
    :param BackboneElement implementation: If this describes a specific instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Describes this specific instance
    :param str url: Base URL for the installation
    :param Reference custodian: Organization that manages the data
    :param str fhirVersion: FHIR Version the system supports
    :param str format: formats supported (xml | json | ttl | mime type)
    :param str patchFormat: Patch formats supported
    :param str implementationGuide: Implementation guides supported
    :param BackboneElement rest: If the endpoint is a RESTful one
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: client | server
    :param str documentation: General description of implementation
    :param BackboneElement security: Information about security of implementation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool cors: Adds CORS Headers (http://enable-cors.org/)
    :param CodeableConcept service: OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates
    :param str description: General description of how security works
    :param BackboneElement resource: Resource served on the REST interface
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: A resource type that is supported
    :param str profile: Base System profile for all uses of resource
    :param str supportedProfile: Profiles for use cases supported
    :param str documentation: Additional information about the use of the resource type
    :param BackboneElement interaction: What operations are supported?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: read | vread | update | patch | delete | history-instance | history-type | create | search-type
    :param str documentation: Anything special about operation behavior
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
    :param BackboneElement searchParam: Search parameters supported by implementation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of search parameter
    :param str definition: Source of definition for parameter
    :param str type: number | date | string | token | reference | composite | quantity | uri | special
    :param str documentation: Server-specific usage
    :param BackboneElement operation: Definition of a resource operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name by which the operation/query is invoked
    :param str definition: The defined operation/query
    :param str documentation: Specific details about operation behavior
    :param BackboneElement interaction: What operations are supported?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: transaction | batch | search-system | history-system
    :param str documentation: Anything special about operation behavior
    :param BackboneElement searchParam: Search parameters supported by implementation
    :param BackboneElement operation: Definition of a resource operation
    :param str compartment: Compartments served/used by system
    :param BackboneElement messaging: If messaging is supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement endpoint: Where messages should be sent
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding protocol: http | ftp | mllp +
    :param str address: Network address or identifier of the end-point
    :param int reliableCache: Reliable Message Cache Length (min)
    :param str documentation: Messaging interface behavior details
    :param BackboneElement supportedMessage: Messages supported by this system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: sender | receiver
    :param str definition: Message supported by this system
    :param BackboneElement document: Document definition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: producer | consumer
    :param str documentation: Description of document support
    :param str profile: Constraint on the resources used in the document
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    kind: str = None
    
    instantiates: str = None
    
    imports: str = None
    
    software: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    version: str = None
    
    releaseDate: str = None
    
    implementation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    url: str = None
    
    custodian: "Reference" = None
    
    fhirVersion: str = None
    
    format: str = None
    
    patchFormat: str = None
    
    implementationGuide: str = None
    
    rest: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    documentation: str = None
    
    security: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    cors: bool = None
    
    service: "CodeableConcept" = None
    
    description: str = None
    
    resource: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    profile: str = None
    
    supportedProfile: str = None
    
    documentation: str = None
    
    interaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    documentation: str = None
    
    versioning: str = None
    
    readHistory: bool = None
    
    updateCreate: bool = None
    
    conditionalCreate: bool = None
    
    conditionalRead: str = None
    
    conditionalUpdate: bool = None
    
    conditionalDelete: str = None
    
    referencePolicy: str = None
    
    searchInclude: str = None
    
    searchRevInclude: str = None
    
    searchParam: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    definition: str = None
    
    type: str = None
    
    documentation: str = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    definition: str = None
    
    documentation: str = None
    
    interaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    documentation: str = None
    
    searchParam: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
    compartment: str = None
    
    messaging: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    endpoint: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    protocol: "Coding" = None
    
    address: str = None
    
    reliableCache: int = None
    
    documentation: str = None
    
    supportedMessage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    definition: str = None
    
    document: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    documentation: str = None
    
    profile: str = None
    