"""
Generated class for CompartmentDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *


@dataclass
class CompartmentDefinition:
    """ A compartment definition that defines how resources are accessed on a server.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this compartment definition, represented as a URI (globally unique)
    :param str version: Business version of the compartment definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this compartment definition (computer friendly)
    :param str title: Name for this compartment definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the compartment definition
    :param UsageContext useContext: The context that the content is intended to support
    :param str purpose: Why this compartment definition is defined
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device | EpisodeOfCare
    :param bool search: Whether the search syntax is supported
    :param BackboneElement resource: How a resource is related to the compartment
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Name of resource type
    :param str param: Search Parameter Name, or chained parameters
    :param str documentation: Additional documentation about the resource and compartment
    :param str startParam: Search Param for interpreting $everything.start
    :param str endParam: Search Param for interpreting $everything.end
    
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
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    purpose: str = None
    
    code: str = None
    
    search: bool = None
    
    resource: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    param: str = None
    
    documentation: str = None
    
    startParam: str = None
    
    endParam: str = None
    