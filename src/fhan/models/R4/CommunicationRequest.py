"""
Generated class for CommunicationRequest. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Payload(Element):
    """ Text, attachment(s), or resource(s) to be communicated to the recipient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str contentString: Message part content
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    contentString: str = None
    

@dataclass
class CommunicationRequest(ModelBase):
    """ A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param Reference basedOn: Fulfills plan or proposal
    :param Reference replaces: Request(s) replaced by this request
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: Message category
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param CodeableConcept medium: A channel of communication
    :param Reference subject: Focus of message
    :param Reference about: Resources that pertain to this communication request
    :param Reference encounter: Encounter created as part of
    :param Payload payload: Message payload
    :param str occurrenceDateTime: When scheduled
    :param str authoredOn: When request transitioned to being actionable
    :param Reference requester: Who/what is requesting service
    :param Reference recipient: Message recipient
    :param Reference sender: Message sender
    :param CodeableConcept reasonCode: Why is communication needed?
    :param Reference reasonReference: Why is communication needed?
    :param Annotation note: Comments made about communication request
    """

    resourceType: str = "CommunicationRequest"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    basedOn: list[Reference] = Reference() 
    
    replaces: list[Reference] = Reference() 
    
    groupIdentifier: "Identifier" = Identifier()
    
    status: str = None
    
    statusReason: "CodeableConcept" = CodeableConcept()
    
    category: list[CodeableConcept] = CodeableConcept() 
    
    priority: str = None
    
    doNotPerform: bool = None
    
    medium: list[CodeableConcept] = CodeableConcept() 
    
    subject: "Reference" = Reference()
    
    about: list[Reference] = Reference() 
    
    encounter: "Reference" = Reference()
    
    payload: list[Payload] = Payload() 
    
    occurrenceDateTime: str = None
    
    authoredOn: str = None
    
    requester: "Reference" = Reference()
    
    recipient: list[Reference] = Reference() 
    
    sender: "Reference" = Reference()
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    