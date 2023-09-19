"""
Generated class for AuditEvent. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class AuditEvent:
    """ A record of an event relevant for purposes such as operations, privacy, security, maintenance, and performance analysis.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept category: Type/identifier of event
    :param CodeableConcept code: Specific type of event
    :param str action: Type of action performed during the event
    :param str severity: emergency | alert | critical | error | warning | notice | informational | debug
    :param Period occurredPeriod: When the activity occurred
    :param str occurredPeriod: When the activity occurred
    :param str recorded: Time when the event was recorded
    :param BackboneElement outcome: Whether the event succeeded or failed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding code: Whether the event succeeded or failed
    :param CodeableConcept detail: Additional outcome detail
    :param CodeableConcept authorization: Authorization related to the event
    :param Reference basedOn: Workflow authorization within which this event occurred
    :param Reference patient: The patient is the subject of the data used/created/updated/deleted during the activity
    :param Reference encounter: Encounter within which this event occurred or which the event is tightly associated
    :param BackboneElement agent: Actor involved in the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How agent participated
    :param CodeableConcept role: Agent role in the event
    :param Reference who: Identifier of who
    :param bool requestor: Whether user is initiator
    :param Reference location: The agent location when the event occurred
    :param str policy: Policy that authorized the agent participation in the event
    :param Reference networkReference: This agent network location for the activity
    :param str networkReference: This agent network location for the activity
    :param str networkReference: This agent network location for the activity
    :param CodeableConcept authorization: Allowable authorization for this agent
    :param BackboneElement source: Audit Event Reporter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference site: Logical source location within the enterprise
    :param Reference observer: The identity of source detecting the event
    :param CodeableConcept type: The type of source where event originated
    :param BackboneElement entity: Data or objects used
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference what: Specific instance of resource
    :param CodeableConcept role: What role the entity played
    :param CodeableConcept securityLabel: Security labels on the entity
    :param str query: Query parameters
    :param BackboneElement detail: Additional Information about the entity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Name of the property
    :param Quantity valueQuantity: Property value
    :param CodeableConcept valueQuantity: Property value
    :param str valueQuantity: Property value
    :param bool valueQuantity: Property value
    :param int valueQuantity: Property value
    :param Range valueQuantity: Property value
    :param Ratio valueQuantity: Property value
    :param str valueQuantity: Property value
    :param str valueQuantity: Property value
    :param Period valueQuantity: Property value
    :param str valueQuantity: Property value
    :param BackboneElement agent: Actor involved in the event
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    action: str = None
    
    severity: str = None
    
    occurredPeriod: "Period" = None
    
    occurredPeriod: str = None
    
    recorded: str = None
    
    outcome: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "Coding" = None
    
    detail: "CodeableConcept" = None
    
    authorization: "CodeableConcept" = None
    
    basedOn: "Reference" = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    agent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    role: "CodeableConcept" = None
    
    who: "Reference" = None
    
    requestor: bool = None
    
    location: "Reference" = None
    
    policy: str = None
    
    networkReference: "Reference" = None
    
    networkReference: str = None
    
    networkReference: str = None
    
    authorization: "CodeableConcept" = None
    
    source: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    site: "Reference" = None
    
    observer: "Reference" = None
    
    type: "CodeableConcept" = None
    
    entity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    what: "Reference" = None
    
    role: "CodeableConcept" = None
    
    securityLabel: "CodeableConcept" = None
    
    query: str = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "CodeableConcept" = None
    
    valueQuantity: str = None
    
    valueQuantity: bool = None
    
    valueQuantity: int = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: "Ratio" = None
    
    valueQuantity: str = None
    
    valueQuantity: str = None
    
    valueQuantity: "Period" = None
    
    valueQuantity: str = None
    
    agent: "BackboneElement" = None
    