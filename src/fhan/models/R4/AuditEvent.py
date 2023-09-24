"""
Generated class for AuditEvent. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Network(Element):
    """ Logical network location for application activity, if the activity has a network location.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str address: Identifier for the network access point of the user device
    :param str type: The type of network access point
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    address: str = None
    
    type: str = None
    

  
    
    
@dataclass
class Agent(Element):
    """ An actor taking an active role in the event or activity that is logged.:param str id: Unique id for inter-element referencing
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
    :param Network network: Logical network location for application activity
    :param CodeableConcept purposeOfUse: Reason given for this user
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    role:  list["CodeableConcept"] = [CodeableConcept()]
    
    who:  "Reference" = Reference()
    
    altId: str = None
    
    name: str = None
    
    requestor: bool = None
    
    location:  "Reference" = Reference()
    
    policy: str = None
    
    media:  "Coding" = Coding()
    
    network:  "Network" = Network()
    
    purposeOfUse:  list["CodeableConcept"] = [CodeableConcept()]
    

    
    
@dataclass
class Source(Element):
    """ The system that is reporting the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str site: Logical source location within the enterprise
    :param Reference observer: The identity of source detecting the event
    :param Coding type: The type of source where event originated
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    site: str = None
    
    observer:  "Reference" = Reference()
    
    type:  list["Coding"] = [Coding()]
    

    
        
    
    
@dataclass
class Detail(Element):
    """ Tagged value pairs for conveying additional information about the entity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Name of the property
    :param str valueString: Property value
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type: str = None
    
    valueString: str = None
    

  
    
    
@dataclass
class Entity(Element):
    """ Specific instances of data or objects that have been accessed.:param str id: Unique id for inter-element referencing
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
    :param Detail detail: Additional Information about the entity
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    what:  "Reference" = Reference()
    
    type:  "Coding" = Coding()
    
    role:  "Coding" = Coding()
    
    lifecycle:  "Coding" = Coding()
    
    securityLabel:  list["Coding"] = [Coding()]
    
    name: str = None
    
    description: str = None
    
    query: str = None
    
    detail:  list["Detail"] = [Detail()]
    

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
    :param Agent agent: Actor involved in the event
    :param Source source: Audit Event Reporter
    :param Entity entity: Data or objects used
    """

    resourceType: str = "AuditEvent"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    subtype: list["Coding"] = None
    
    action: str = None
    
    period: "Period" = None
    
    recorded: str = None
    
    outcome: str = None
    
    outcomeDesc: str = None
    
    purposeOfEvent: list["CodeableConcept"] = None
    
    agent: list["Agent"] = None
    
    source: "Source" = None
    
    entity: list["Entity"] = None
    