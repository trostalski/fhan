"""
Generated class for TerminologyCapabilities. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Element import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Software(Element):
    """ Software that is covered by this terminology capability statement.  It is used when the statement describes the capabilities of a particular software version, independent of an installation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name the software is known by
    :param str version: Version covered by this statement
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    name: str = None
    
    version: str = None
    

    
    
@dataclass
class Implementation(Element):
    """ Identifies a specific implementation instance that is described by the terminology capability statement - i.e. a particular installation, rather than the capabilities of a software program.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Describes this specific instance
    :param str url: Base URL for the implementation
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    description: str = None
    
    url: str = None
    

    
        
    
        
    
    
@dataclass
class Filter(Element):
    """ Filter Properties supported.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code of the property supported
    :param str op: Operations supported for the property
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    code: str = None
    
    op: str = None
    

  
    
    
@dataclass
class Version(Element):
    """ For the code system, a list of versions that are supported by the server.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Version identifier for this version
    :param bool isDefault: If this is the default version for this code system
    :param bool compositional: If compositional grammar is supported
    :param str language: Language Displays supported
    :param Filter filter: Filter Properties supported
    :param str property: Properties supported for $lookup
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    code: str = None
    
    isDefault: bool = None
    
    compositional: bool = None
    
    language: str = None
    
    filter:  list["Filter"] = [Filter()]
    
    property: str = None
    

  
    
    
@dataclass
class CodeSystem(Element):
    """ Identifies a code system that is supported by the server. If there is a no code system URL, then this declares the general assumptions a client can make about support for any CodeSystem resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: URI for the Code System
    :param Version version: Version of Code System supported
    :param bool subsumption: Whether subsumption is supported
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    uri: str = None
    
    version:  list["Version"] = [Version()]
    
    subsumption: bool = None
    

    
        
    
    
@dataclass
class Parameter(Element):
    """ Supported expansion parameter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Expansion Parameter name
    :param str documentation: Description of support for parameter
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    name: str = None
    
    documentation: str = None
    

  
    
    
@dataclass
class Expansion(Element):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html) operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool hierarchical: Whether the server can return nested value sets
    :param bool paging: Whether the server supports paging on expansion
    :param bool incomplete: Allow request for incomplete expansions?
    :param Parameter parameter: Supported expansion parameter
    :param str textFilter: Documentation about text searching works
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    hierarchical: bool = None
    
    paging: bool = None
    
    incomplete: bool = None
    
    parameter:  list["Parameter"] = [Parameter()]
    
    textFilter: str = None
    

    
    
@dataclass
class ValidateCode(Element):
    """ Information about the [ValueSet/$validate-code](valueset-operation-validate-code.html) operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translations: Whether translations are validated
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    translations: bool = None
    

    
    
@dataclass
class Translation(Element):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-translate.html) operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool needsMap: Whether the client must identify the map
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    needsMap: bool = None
    

    
    
@dataclass
class Closure(Element):
    """ Whether the $closure operation is supported.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool translation: If cross-system closure is supported
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
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

    resourceType: str = "TerminologyCapabilities"
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
    
    software: "Software" = None
    
    implementation: "Implementation" = None
    
    lockedDate: bool = None
    
    codeSystem: list["CodeSystem"] = None
    
    expansion: "Expansion" = None
    
    codeSearch: str = None
    
    validateCode: "ValidateCode" = None
    
    translation: "Translation" = None
    
    closure: "Closure" = None
    