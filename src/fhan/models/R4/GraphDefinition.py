"""
Generated class for GraphDefinition. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
        
    
        
    
    
@dataclass
class Compartment(Element):
    """ Compartment Consistency Rules.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str use: condition | requirement
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device
    :param str rule: identical | matching | different | custom
    :param str expression: Custom rule, as a FHIRPath expression
    :param str description: Documentation for FHIRPath expression
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    use: str = None
    
    code: str = None
    
    rule: str = None
    
    expression: str = None
    
    description: str = None
    

  
    
    
@dataclass
class Target(Element):
    """ Potential target for the link.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Type of resource this link refers to
    :param str params: Criteria for reverse lookup
    :param str profile: Profile for the target resource
    :param Compartment compartment: Compartment Consistency Rules
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    type: str = None
    
    params: str = None
    
    profile: str = None
    compartment: list[Compartment] = None
    

  
    
    
@dataclass
class Link(Element):
    """ Links this graph makes rules about.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: Path in the resource that contains the link
    :param str sliceName: Which slice (if profiled)
    :param int min: Minimum occurrences for this link
    :param str max: Maximum occurrences for this link
    :param str description: Why this link is specified
    :param Target target: Potential target for the link
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    path: str = None
    
    sliceName: str = None
    
    min: int = None
    
    max: str = None
    
    description: str = None
    target: list[Target] = None
    

@dataclass
class GraphDefinition(ModelBase):
    """ A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this graph definition, represented as a URI (globally unique)
    :param str version: Business version of the graph definition
    :param str name: Name for this graph definition (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the graph definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for graph definition (if applicable)
    :param str purpose: Why this graph definition is defined
    :param str start: Type of resource at which the graph starts
    :param str profile: Profile on base resource
    :param Link link: Links this graph makes rules about
    """

    resourceType: str = "GraphDefinition"
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
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    purpose: str = None
    
    start: str = None
    
    profile: str = None
    
    link: list["Link"] = None
    