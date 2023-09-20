"""
Generated class for StructureDefinition. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.ElementDefinition import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import ModelBase

@dataclass
class mapping(Element):
    """ An external specification that the content is mapped to.
    :param BackboneElement mapping: External specification that the content is mapped to
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identity: Internal id when this mapping is used
    :param str uri: Identifies what this mapping refers to
    :param str name: Names what this mapping refers to
    :param str comment: Versions, Issues, Scope limitations etc.
    """
    mapping: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identity: str = None
    
    uri: str = None
    
    name: str = None
    
    comment: str = None
    
@dataclass
class context(Element):
    """ Identifies the types of resource or data type elements to which the extension can be applied.
    :param BackboneElement context: If an extension, where it can be used in instances
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: fhirpath | element | extension
    :param str expression: Where the extension can be used in instances
    :param str contextInvariant: FHIRPath invariants - when the extension can be used
    """
    context: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    expression: str = None
    
    contextInvariant: str = None
    
@dataclass
class snapshot(Element):
    """ A snapshot view is expressed in a standalone form that can be used and interpreted without considering the base StructureDefinition.
    :param BackboneElement snapshot: Snapshot view of the structure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param ElementDefinition element: Definition of elements in the resource (if no StructureDefinition)
    """
    snapshot: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    element: list["ElementDefinition"] = None
    
@dataclass
class differential(Element):
    """ A differential view is expressed relative to the base StructureDefinition - a statement of differences that it applies.
    :param BackboneElement differential: Differential view of the structure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param ElementDefinition element: Definition of elements in the resource (if no StructureDefinition)
    """
    differential: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    element: list["ElementDefinition"] = None
    


@dataclass
class StructureDefinition(ModelBase):
    """ A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this structure definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the structure definition
    :param str version: Business version of the structure definition
    :param str name: Name for this structure definition (computer friendly)
    :param str title: Name for this structure definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the structure definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for structure definition (if applicable)
    :param str purpose: Why this structure definition is defined
    :param str copyright: Use and/or publishing restrictions
    :param Coding keyword: Assist with indexing and finding
    :param str fhirVersion: FHIR Version this StructureDefinition targets
    :param BackboneElement mapping: External specification that the content is mapped to
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identity: Internal id when this mapping is used
    :param str uri: Identifies what this mapping refers to
    :param str name: Names what this mapping refers to
    :param str comment: Versions, Issues, Scope limitations etc.
    :param str kind: primitive-type | complex-type | resource | logical
    :param bool abstract: Whether the structure is abstract
    :param BackboneElement context: If an extension, where it can be used in instances
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: fhirpath | element | extension
    :param str expression: Where the extension can be used in instances
    :param str contextInvariant: FHIRPath invariants - when the extension can be used
    :param str type: Type defined or constrained by this structure
    :param str baseDefinition: Definition that this type is constrained/specialized from
    :param str derivation: specialization | constraint - How relates to base definition
    :param BackboneElement snapshot: Snapshot view of the structure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param ElementDefinition element: Definition of elements in the resource (if no StructureDefinition)
    :param BackboneElement differential: Differential view of the structure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param ElementDefinition element: Definition of elements in the resource (if no StructureDefinition)
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
    
    identifier: list["Identifier"] = None
    
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
    
    keyword: list["Coding"] = None
    
    fhirVersion: str = None
    
    mapping: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identity: str = None
    
    uri: str = None
    
    name: str = None
    
    comment: str = None
    
    kind: str = None
    
    abstract: bool = None
    
    context: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    expression: str = None
    
    contextInvariant: str = None
    
    type: str = None
    
    baseDefinition: str = None
    
    derivation: str = None
    
    snapshot: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    element: list["ElementDefinition"] = None
    
    differential: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    element: list["ElementDefinition"] = None
    