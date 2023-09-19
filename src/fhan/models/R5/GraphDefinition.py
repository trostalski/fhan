"""
Generated class for GraphDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *


@dataclass
class GraphDefinition:
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
    :param Identifier identifier: Additional identifier for the GraphDefinition (business identifier)
    :param str version: Business version of the graph definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this graph definition (computer friendly)
    :param str title: Name for this graph definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the graph definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for graph definition (if applicable)
    :param str purpose: Why this graph definition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str start: Starting Node
    :param BackboneElement node: Potential target for the link
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str nodeId: Internal ID - target for link references
    :param str description: Why this node is specified
    :param str type: Type of resource this link refers to
    :param str profile: Profile for the target resource
    :param BackboneElement link: Links this graph makes rules about
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Why this link is specified
    :param int min: Minimum occurrences for this link
    :param str max: Maximum occurrences for this link
    :param str sourceId: Source Node for this link
    :param str path: Path in the resource that contains the link
    :param str sliceName: Which slice (if profiled)
    :param str targetId: Target Node for this link
    :param str params: Criteria for reverse lookup
    :param BackboneElement compartment: Compartment Consistency Rules
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str use: where | requires
    :param str rule: identical | matching | different | custom
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device | EpisodeOfCare
    :param str expression: Custom rule, as a FHIRPath expression
    :param str description: Documentation for FHIRPath expression
    
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
    
    identifier: "Identifier" = None
    
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
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    start: str = None
    
    node: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    nodeId: str = None
    
    description: str = None
    
    type: str = None
    
    profile: str = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    min: int = None
    
    max: str = None
    
    sourceId: str = None
    
    path: str = None
    
    sliceName: str = None
    
    targetId: str = None
    
    params: str = None
    
    compartment: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    use: str = None
    
    rule: str = None
    
    code: str = None
    
    expression: str = None
    
    description: str = None
    