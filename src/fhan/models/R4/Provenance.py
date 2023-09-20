"""
Generated class for Provenance. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Signature import *
from fhan.models.generator_models import ModelBase

@dataclass
class agent(Element):
    """ An actor taking a role in an activity  for which it can be assigned some degree of responsibility for the activity taking place.
    :param BackboneElement agent: Actor involved
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How the agent participated
    :param CodeableConcept role: What the agents role was
    :param Reference who: Who participated
    :param Reference onBehalfOf: Who the agent is representing
    :param BackboneElement agent: Actor involved
    """
    agent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    role: list["CodeableConcept"] = None
    
    who: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    agent: list["BackboneElement"] = None
    
@dataclass
class entity(Element):
    """ An entity used in this activity.
    :param BackboneElement entity: An entity used in this activity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str role: derivation | revision | quotation | source | removal
    :param Reference what: Identity of entity
    """
    entity: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    role: str = None
    
    what: "Reference" = None
    
@dataclass
class agent(Element):
    """ An actor taking a role in an activity  for which it can be assigned some degree of responsibility for the activity taking place.
    :param BackboneElement agent: Actor involved
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How the agent participated
    :param CodeableConcept role: What the agents role was
    :param Reference who: Who participated
    :param Reference onBehalfOf: Who the agent is representing
    :param BackboneElement agent: Actor involved
    """
    agent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    role: list["CodeableConcept"] = None
    
    who: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    agent: list["BackboneElement"] = None
    


@dataclass
class Provenance(ModelBase):
    """ Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can themselves become important records with their own provenance. Provenance statement indicates clinical significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact security, privacy, and trust policies.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference target: Target Reference(s) (usually version specific)
    :param Period occurredPeriod: When the activity occurred
    :param str occurredPeriod: When the activity occurred
    :param str recorded: When the activity was recorded / updated
    :param str policy: Policy or plan the activity was defined by
    :param Reference location: Where the activity occurred, if relevant
    :param CodeableConcept reason: Reason the activity is occurring
    :param CodeableConcept activity: Activity that occurred
    :param BackboneElement agent: Actor involved
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How the agent participated
    :param CodeableConcept role: What the agents role was
    :param Reference who: Who participated
    :param Reference onBehalfOf: Who the agent is representing
    :param BackboneElement entity: An entity used in this activity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str role: derivation | revision | quotation | source | removal
    :param Reference what: Identity of entity
    :param BackboneElement agent: Actor involved
    :param Signature signature: Signature on target
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    target: list["Reference"] = None
    
    occurredPeriod: "Period" = None
    
    occurredPeriod: str = None
    
    recorded: str = None
    
    policy: str = None
    
    location: "Reference" = None
    
    reason: list["CodeableConcept"] = None
    
    activity: "CodeableConcept" = None
    
    agent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    role: list["CodeableConcept"] = None
    
    who: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    entity: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    role: str = None
    
    what: "Reference" = None
    
    agent: list["BackboneElement"] = None
    
    signature: list["Signature"] = None
    