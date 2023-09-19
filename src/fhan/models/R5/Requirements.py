"""
Generated class for Requirements. 
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
from fhan.models.R5.Reference import *


@dataclass
class Requirements:
    """ The Requirements resource is used to describe an actor - a human or an application that plays a role in data exchange, and that may have obligations associated with the role the actor plays.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this Requirements, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the Requirements (business identifier)
    :param str version: Business version of the Requirements
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this Requirements (computer friendly)
    :param str title: Name for this Requirements (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the requirements
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for Requirements (if applicable)
    :param str purpose: Why this Requirements is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str derivedFrom: Other set of Requirements this builds on
    :param str reference: External artifact (rule/document etc. that) created this set of requirements
    :param str actor: Actor for these requirements
    :param BackboneElement statement: Actual statement as markdown
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: Key that identifies this statement
    :param str label: Short Human label for this statement
    :param str conformance: SHALL | SHOULD | MAY | SHOULD-NOT
    :param bool conditionality: Set to true if requirements statement is conditional
    :param str requirement: The actual requirement
    :param str derivedFrom: Another statement this clarifies/restricts ([url#]key)
    :param str parent: A larger requirement that this requirement helps to refine and enable
    :param str satisfiedBy: Design artifact that satisfies this requirement
    :param str reference: External artifact (rule/document etc. that) created this requirement
    :param Reference source: Who asked for this statement
    
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
    
    derivedFrom: str = None
    
    reference: str = None
    
    actor: str = None
    
    statement: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    key: str = None
    
    label: str = None
    
    conformance: str = None
    
    conditionality: bool = None
    
    requirement: str = None
    
    derivedFrom: str = None
    
    parent: str = None
    
    satisfiedBy: str = None
    
    reference: str = None
    
    source: "Reference" = None
    