"""
Generated class for AuditEvent. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Coding import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class AuditEvent(ModelBase):
    """ Defines the elements to be supported within the AuditEvent resource in order to conform with the Electronic Health Record System Functional Model Record Lifecycle Event standard
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding type: Type/identifier of event
    :param Coding subtype: More specific type/id for the event
    :param str action: Type of action performed during the event
    :param Period period: When the activity occurred
    :param str recorded: Time when the event was recorded
    :param str outcome: Whether the event succeeded or failed
    :param str outcomeDesc: Description of the event outcome
    :param CodeableConcept purposeOfEvent: The purposeOfUse of the event
    :param BackboneElement agent: Actor involved in the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How agent participated
    :param CodeableConcept role: Agent role in the event
    :param Reference who: Identifier of who
    :param str altId: Alternative User identity
    :param str name: Human friendly name for the agent
    :param bool requestor: Whether user is initiator
    :param Reference location: Where
    :param str policy: Policy that authorized event
    :param Coding media: Type of media
    :param BackboneElement network: Logical network location for application activity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str address: Identifier for the network access point of the user device
    :param str type: The type of network access point
    :param CodeableConcept purposeOfUse: Reason given for this user
    :param BackboneElement source: Audit Event Reporter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str site: Logical source location within the enterprise
    :param Reference observer: The identity of source detecting the event
    :param Coding type: The type of source where event originated
    :param BackboneElement entity: Data or objects used
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference what: Specific instance of resource
    :param Coding type: Type of entity involved
    :param Coding role: What role the entity played
    :param Coding lifecycle: Life-cycle stage for the entity
    :param Coding securityLabel: Security labels on the entity
    :param str name: Descriptor for entity
    :param str description: Descriptive text
    :param str query: Query parameters
    :param BackboneElement detail: Additional Information about the entity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Name of the property
    :param str valuestring: Property value
    :param str valuestring: Property value
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "Coding" = None
    
    subtype: "Coding" = None
    
    action: str = None
    
    period: "Period" = None
    
    recorded: str = None
    
    outcome: str = None
    
    outcomeDesc: str = None
    
    purposeOfEvent: "CodeableConcept" = None
    
    agent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    role: "CodeableConcept" = None
    
    who: "Reference" = None
    
    altId: str = None
    
    name: str = None
    
    requestor: bool = None
    
    location: "Reference" = None
    
    policy: str = None
    
    media: "Coding" = None
    
    network: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    address: str = None
    
    type: str = None
    
    purposeOfUse: "CodeableConcept" = None
    
    source: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    site: str = None
    
    observer: "Reference" = None
    
    type: "Coding" = None
    
    entity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    what: "Reference" = None
    
    type: "Coding" = None
    
    role: "Coding" = None
    
    lifecycle: "Coding" = None
    
    securityLabel: "Coding" = None
    
    name: str = None
    
    description: str = None
    
    query: str = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    valuestring: str = None
    
    valuestring: str = None
    