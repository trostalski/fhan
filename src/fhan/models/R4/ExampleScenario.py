"""
Generated class for ExampleScenario. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class actor(Element):
    """ Actor participating in the resource.
    :param BackboneElement actor: Actor participating in the resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actorId: ID or acronym of the actor
    :param str type: person | entity
    :param str name: The name of the actor as shown in the page
    :param str description: The description of the actor
    """
    actor: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    actorId: str = None
    
    type: str = None
    
    name: str = None
    
    description: str = None
    
@dataclass
class instance(Element):
    """ Each resource and each version that is present in the workflow.
    :param BackboneElement instance: Each resource and each version that is present in the workflow
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: The id of the resource for referencing
    :param str resourceType: The type of the resource
    :param str name: A short name for the resource instance
    :param str description: Human-friendly description of the resource instance
    :param BackboneElement version: A specific version of the resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str versionId: The identifier of a specific version of a resource
    :param str description: The description of the resource version
    :param BackboneElement containedInstance: Resources contained in the instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    :param BackboneElement request: Resources contained in the instance
    :param BackboneElement response: Resources contained in the instance
    """
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    resourceType: str = None
    
    name: str = None
    
    description: str = None
    
    version: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    versionId: str = None
    
    description: str = None
    
    containedInstance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    versionId: str = None
    
    request: list["BackboneElement"] = None
    
    response: list["BackboneElement"] = None
    
@dataclass
class version(Element):
    """ A specific version of the resource.
    :param BackboneElement version: A specific version of the resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str versionId: The identifier of a specific version of a resource
    :param str description: The description of the resource version
    """
    version: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    versionId: str = None
    
    description: str = None
    
@dataclass
class containedInstance(Element):
    """ Resources contained in the instance (e.g. the observations contained in a bundle).
    :param BackboneElement containedInstance: Resources contained in the instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    :param BackboneElement request: Resources contained in the instance
    :param BackboneElement response: Resources contained in the instance
    """
    containedInstance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    versionId: str = None
    
    request: list["BackboneElement"] = None
    
    response: list["BackboneElement"] = None
    
@dataclass
class process(Element):
    """ Each major process - a group of operations.
    :param BackboneElement process: Each major process - a group of operations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: The diagram title of the group of operations
    :param str description: A longer description of the group of operations
    :param str preConditions: Description of initial status before the process starts
    :param str postConditions: Description of final status after the process ends
    :param BackboneElement step: Each step of the process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement process: Each major process - a group of operations
    :param bool pause: If there is a pause in the flow
    :param BackboneElement operation: Each interaction or action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    :param BackboneElement step: Each step of the process
    """
    process: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    preConditions: str = None
    
    postConditions: str = None
    
    step: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    process: list["BackboneElement"] = None
    
    pause: bool = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    alternative: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    step: list["BackboneElement"] = None
    
@dataclass
class step(Element):
    """ Each step of the process.
    :param BackboneElement step: Each step of the process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool pause: If there is a pause in the flow
    :param BackboneElement operation: Each interaction or action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    :param BackboneElement step: Each step of the process
    """
    step: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    pause: bool = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    alternative: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    step: list["BackboneElement"] = None
    
@dataclass
class process(Element):
    """ Each major process - a group of operations.
    :param BackboneElement process: Each major process - a group of operations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: The diagram title of the group of operations
    :param str description: A longer description of the group of operations
    :param str preConditions: Description of initial status before the process starts
    :param str postConditions: Description of final status after the process ends
    :param BackboneElement step: Each step of the process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement process: Each major process - a group of operations
    :param bool pause: If there is a pause in the flow
    :param BackboneElement operation: Each interaction or action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    :param BackboneElement step: Each step of the process
    """
    process: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    preConditions: str = None
    
    postConditions: str = None
    
    step: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    process: list["BackboneElement"] = None
    
    pause: bool = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    alternative: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    step: list["BackboneElement"] = None
    
@dataclass
class operation(Element):
    """ Each interaction or action.
    :param BackboneElement operation: Each interaction or action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
@dataclass
class request(Element):
    """ Resources contained in the instance (e.g. the observations contained in a bundle).
    :param BackboneElement containedInstance: Resources contained in the instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    :param BackboneElement request: Resources contained in the instance
    :param BackboneElement response: Resources contained in the instance
    """
    containedInstance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    versionId: str = None
    
    request: list["BackboneElement"] = None
    
    response: list["BackboneElement"] = None
    
@dataclass
class response(Element):
    """ Resources contained in the instance (e.g. the observations contained in a bundle).
    :param BackboneElement containedInstance: Resources contained in the instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    :param BackboneElement request: Resources contained in the instance
    :param BackboneElement response: Resources contained in the instance
    """
    containedInstance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    versionId: str = None
    
    request: list["BackboneElement"] = None
    
    response: list["BackboneElement"] = None
    
@dataclass
class alternative(Element):
    """ Indicates an alternative step that can be taken instead of the operations on the base step in exceptional/atypical circumstances.
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    """
    alternative: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
@dataclass
class step(Element):
    """ Each step of the process.
    :param BackboneElement step: Each step of the process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool pause: If there is a pause in the flow
    :param BackboneElement operation: Each interaction or action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    :param BackboneElement step: Each step of the process
    """
    step: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    pause: bool = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    alternative: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    step: list["BackboneElement"] = None
    


@dataclass
class ExampleScenario(ModelBase):
    """ Example of workflow instance.
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
    :param str name: Name for this example scenario (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for example scenario (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str purpose: The purpose of the example, e.g. to illustrate a scenario
    :param BackboneElement actor: Actor participating in the resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actorId: ID or acronym of the actor
    :param str type: person | entity
    :param str name: The name of the actor as shown in the page
    :param str description: The description of the actor
    :param BackboneElement instance: Each resource and each version that is present in the workflow
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: The id of the resource for referencing
    :param str resourceType: The type of the resource
    :param str name: A short name for the resource instance
    :param str description: Human-friendly description of the resource instance
    :param BackboneElement version: A specific version of the resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str versionId: The identifier of a specific version of a resource
    :param str description: The description of the resource version
    :param BackboneElement containedInstance: Resources contained in the instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    :param BackboneElement process: Each major process - a group of operations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: The diagram title of the group of operations
    :param str description: A longer description of the group of operations
    :param str preConditions: Description of initial status before the process starts
    :param str postConditions: Description of final status after the process ends
    :param BackboneElement step: Each step of the process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement process: Each major process - a group of operations
    :param bool pause: If there is a pause in the flow
    :param BackboneElement operation: Each interaction or action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    :param BackboneElement request: Resources contained in the instance
    :param BackboneElement response: Resources contained in the instance
    :param BackboneElement alternative: Alternate non-typical step action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    :param BackboneElement step: Each step of the process
    :param str workflow: Another nested workflow
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
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    copyright: str = None
    
    purpose: str = None
    
    actor: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    actorId: str = None
    
    type: str = None
    
    name: str = None
    
    description: str = None
    
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    resourceType: str = None
    
    name: str = None
    
    description: str = None
    
    version: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    versionId: str = None
    
    description: str = None
    
    containedInstance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    resourceId: str = None
    
    versionId: str = None
    
    process: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    preConditions: str = None
    
    postConditions: str = None
    
    step: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    process: list["BackboneElement"] = None
    
    pause: bool = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    request: list["BackboneElement"] = None
    
    response: list["BackboneElement"] = None
    
    alternative: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    title: str = None
    
    description: str = None
    
    step: list["BackboneElement"] = None
    
    workflow: str = None
    