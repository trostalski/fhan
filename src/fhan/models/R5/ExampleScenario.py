"""
Generated class for ExampleScenario. 
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
class ExampleScenario:
    """ A walkthrough of a workflow showing the interaction between systems and the instances shared, possibly including the evolution of instances over time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this example scenario, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the example scenario
    :param str version: Business version of the example scenario
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: To be removed?
    :param str title: Name for this example scenario (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the ExampleScenario
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for example scenario (if applicable)
    :param str purpose: The purpose of the example, e.g. to illustrate a scenario
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param BackboneElement actor: Individual involved in exchange
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: ID or acronym of the actor
    :param str type: person | system
    :param str title: Label for actor when rendering
    :param str description: Details about actor
    :param BackboneElement instance: Data used in the scenario
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: ID or acronym of the instance
    :param Coding structureType: Data structure for example
    :param str structureVersion: E.g. 4.0.1
    :param str structureProfilecanonical: Rules instance adheres to
    :param str structureProfilecanonical: Rules instance adheres to
    :param str title: Label for instance
    :param str description: Human-friendly description of the instance
    :param Reference content: Example instance data
    :param BackboneElement version: Snapshot of instance that changes
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: ID or acronym of the version
    :param str title: Label for instance version
    :param str description: Details about version
    :param Reference content: Example instance version data
    :param BackboneElement containedInstance: Resources contained in the instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str instanceReference: Key of contained instance
    :param str versionReference: Key of contained instance version
    :param BackboneElement process: Major process within scenario
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for procss
    :param str description: Human-friendly description of the process
    :param str preConditions: Status before process starts
    :param str postConditions: Status after successful completion
    :param BackboneElement step: Event within of the process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: Sequential number of the step
    :param BackboneElement process: Major process within scenario
    :param str workflow: Step is nested workflow
    :param BackboneElement operation: Step is simple action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: Kind of action
    :param str title: Label for step
    :param str initiator: Who starts the operation
    :param str receiver: Who receives the operation
    :param str description: Human-friendly description of the operation
    :param bool initiatorActive: Initiator stays active?
    :param bool receiverActive: Receiver stays active?
    :param BackboneElement request: Resources contained in the instance
    :param BackboneElement response: Resources contained in the instance
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: Human-readable description of option
    :param BackboneElement step: Event within of the process
    :param bool pause: Pause in the flow?
    
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
    
    actor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    key: str = None
    
    type: str = None
    
    title: str = None
    
    description: str = None
    
    instance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    key: str = None
    
    structureType: "Coding" = None
    
    structureVersion: str = None
    
    structureProfilecanonical: str = None
    
    structureProfilecanonical: str = None
    
    title: str = None
    
    description: str = None
    
    content: "Reference" = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    key: str = None
    
    title: str = None
    
    description: str = None
    
    content: "Reference" = None
    
    containedInstance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    instanceReference: str = None
    
    versionReference: str = None
    
    process: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    description: str = None
    
    preConditions: str = None
    
    postConditions: str = None
    
    step: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    number: str = None
    
    process: "BackboneElement" = None
    
    workflow: str = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "Coding" = None
    
    title: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    request: "BackboneElement" = None
    
    response: "BackboneElement" = None
    
    alternative: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    description: str = None
    
    step: "BackboneElement" = None
    
    pause: bool = None
    