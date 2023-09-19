"""
Generated class for Provenance. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Signature import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Reference import *


@dataclass
class Provenance:
    """ Guidance on using Provenance for related history elements to provide key events that have happened over the lifespan of the resource  - see the use of this pattern in the [Request Pattern](request.html#history)
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference target: Resource version
    :param str occurreddateTime: When the activity occurred
    :param str recorded: When the activity was recorded / updated
    :param str policy: Policy or plan the activity was defined by
    :param Reference location: Where the activity occurred, if relevant
    :param CodeableReference authorization: Authorization (purposeOfUse) related to the event
    :param CodeableConcept activity: Record activity
    :param Reference basedOn: Workflow authorization within which this event occurred
    :param Reference patient: The patient is the subject of the data created/updated (.target) by the activity
    :param Reference encounter: Encounter within which this event occurred or which the event is tightly associated
    :param BackboneElement agent: Who was involved with change
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How the agent participated
    :param CodeableConcept role: What the agents role was
    :param Reference who: The agent that participated in the event
    :param Reference onBehalfOf: The agent that delegated
    :param BackboneElement agent:Author: Author
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How the agent participated
    :param CodeableConcept role: What the agents role was
    :param Reference who: Author Reference
    :param Reference onBehalfOf: The agent that delegated
    :param BackboneElement entity: An entity used in this activity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str role: revision | quotation | source | instantiates | removal
    :param Reference what: Identity of entity
    :param BackboneElement agent: Who was involved with change
    :param Signature signature: Signature on target
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    target: "Reference" = None
    
    occurreddateTime: str = None
    
    recorded: str = None
    
    policy: str = None
    
    location: "Reference" = None
    
    authorization: "CodeableReference" = None
    
    activity: "CodeableConcept" = None
    
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
    
    onBehalfOf: "Reference" = None
    
    agent:Author: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    role: "CodeableConcept" = None
    
    who: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    entity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: str = None
    
    what: "Reference" = None
    
    agent: "BackboneElement" = None
    
    signature: "Signature" = None
    