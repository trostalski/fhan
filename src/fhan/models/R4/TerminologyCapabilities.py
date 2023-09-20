"""
Generated class for TerminologyCapabilities. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class software(Element):
    """ Software that is covered by this terminology capability statement.  It is used when the statement describes the capabilities of a particular software version, independent of an installation.
    :param BackboneElement software: Software that is covered by this terminology capability statement
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name the software is known by
    :param str version: Version covered by this statement
    """
    software: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    version: str = None
    
@dataclass
class implementation(Element):
    """ Identifies a specific implementation instance that is described by the terminology capability statement - i.e. a particular installation, rather than the capabilities of a software program.
    :param BackboneElement implementation: If this describes a specific instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Describes this specific instance
    :param str url: Base URL for the implementation
    """
    implementation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    url: str = None
    
@dataclass
class codeSystem(Element):
    """ Identifies a code system that is supported by the server. If there is a no code system URL, then this declares the general assumptions a client can make about support for any CodeSystem resource.
    :param BackboneElement codeSystem: A code system supported by the server
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: URI for the Code System
    :param BackboneElement version: Version of Code System supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Version identifier for this version
    :param bool isDefault: If this is the default version for this code system
    :param bool compositional: If compositional grammar is supported
    :param str language: Language Displays supported
    :param BackboneElement filter: Filter Properties supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code of the property supported
    :param str op: Operations supported for the property
    :param str property: Properties supported for $lookup
    :param bool subsumption: Whether subsumption is supported
    """
    codeSystem: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uri: str = None
    
    version: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    isDefault: bool = None
    
    compositional: bool = None
    
    language: str = None
    
    filter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    op: str = None
    
    property: str = None
    
    subsumption: bool = None
    
@dataclass
class version(Element):
    """ For the code system, a list of versions that are supported by the server.
    :param BackboneElement version: Version of Code System supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Version identifier for this version
    :param bool isDefault: If this is the default version for this code system
    :param bool compositional: If compositional grammar is supported
    :param str language: Language Displays supported
    :param BackboneElement filter: Filter Properties supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code of the property supported
    :param str op: Operations supported for the property
    :param str property: Properties supported for $lookup
    """
    version: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    isDefault: bool = None
    
    compositional: bool = None
    
    language: str = None
    
    filter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    op: str = None
    
    property: str = None
    
@dataclass
class filter(Element):
    """ Filter Properties supported.
    :param BackboneElement filter: Filter Properties supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code of the property supported
    :param str op: Operations supported for the property
    """
    filter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    op: str = None
    
@dataclass
class expansion(Element):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html) operation.
    :param BackboneElement expansion: Information about the [ValueSet/$expand](valueset-operation-expand.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool hierarchical: Whether the server can return nested value sets
    :param bool paging: Whether the server supports paging on expansion
    :param bool incomplete: Allow request for incomplete expansions?
    :param BackboneElement parameter: Supported expansion parameter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Expansion Parameter name
    :param str documentation: Description of support for parameter
    :param str textFilter: Documentation about text searching works
    """
    expansion: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    hierarchical: bool = None
    
    paging: bool = None
    
    incomplete: bool = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    documentation: str = None
    
    textFilter: str = None
    
@dataclass
class parameter(Element):
    """ Supported expansion parameter.
    :param BackboneElement parameter: Supported expansion parameter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Expansion Parameter name
    :param str documentation: Description of support for parameter
    """
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    documentation: str = None
    
@dataclass
class validateCode(Element):
    """ Information about the [ValueSet/$validate-code](valueset-operation-validate-code.html) operation.
    :param BackboneElement validateCode: Information about the [ValueSet/$validate-code](valueset-operation-validate-code.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translations: Whether translations are validated
    """
    validateCode: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    translations: bool = None
    
@dataclass
class translation(Element):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-translate.html) operation.
    :param BackboneElement translation: Information about the [ConceptMap/$translate](conceptmap-operation-translate.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool needsMap: Whether the client must identify the map
    """
    translation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    needsMap: bool = None
    
@dataclass
class closure(Element):
    """ Whether the $closure operation is supported.
    :param BackboneElement closure: Information about the [ConceptMap/$closure](conceptmap-operation-closure.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translation: If cross-system closure is supported
    """
    closure: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    translation: bool = None
    


@dataclass
class TerminologyCapabilities(ModelBase):
    """ A TerminologyCapabilities resource documents a set of capabilities (behaviors) of a FHIR Terminology Server that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
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
    :param BackboneElement software: Software that is covered by this terminology capability statement
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name the software is known by
    :param str version: Version covered by this statement
    :param BackboneElement implementation: If this describes a specific instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Describes this specific instance
    :param str url: Base URL for the implementation
    :param bool lockedDate: Whether lockedDate is supported
    :param BackboneElement codeSystem: A code system supported by the server
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: URI for the Code System
    :param BackboneElement version: Version of Code System supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Version identifier for this version
    :param bool isDefault: If this is the default version for this code system
    :param bool compositional: If compositional grammar is supported
    :param str language: Language Displays supported
    :param BackboneElement filter: Filter Properties supported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code of the property supported
    :param str op: Operations supported for the property
    :param str property: Properties supported for $lookup
    :param bool subsumption: Whether subsumption is supported
    :param BackboneElement expansion: Information about the [ValueSet/$expand](valueset-operation-expand.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool hierarchical: Whether the server can return nested value sets
    :param bool paging: Whether the server supports paging on expansion
    :param bool incomplete: Allow request for incomplete expansions?
    :param BackboneElement parameter: Supported expansion parameter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Expansion Parameter name
    :param str documentation: Description of support for parameter
    :param str textFilter: Documentation about text searching works
    :param str codeSearch: explicit | all
    :param BackboneElement validateCode: Information about the [ValueSet/$validate-code](valueset-operation-validate-code.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translations: Whether translations are validated
    :param BackboneElement translation: Information about the [ConceptMap/$translate](conceptmap-operation-translate.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool needsMap: Whether the client must identify the map
    :param BackboneElement closure: Information about the [ConceptMap/$closure](conceptmap-operation-closure.html) operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translation: If cross-system closure is supported
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    purpose: str = None
    
    copyright: str = None
    
    kind: str = None
    
    software: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    version: str = None
    
    implementation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    url: str = None
    
    lockedDate: bool = None
    
    codeSystem: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uri: str = None
    
    version: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    isDefault: bool = None
    
    compositional: bool = None
    
    language: str = None
    
    filter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: str = None
    
    op: str = None
    
    property: str = None
    
    subsumption: bool = None
    
    expansion: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    hierarchical: bool = None
    
    paging: bool = None
    
    incomplete: bool = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    documentation: str = None
    
    textFilter: str = None
    
    codeSearch: str = None
    
    validateCode: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    translations: bool = None
    
    translation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    needsMap: bool = None
    
    closure: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    translation: bool = None
    