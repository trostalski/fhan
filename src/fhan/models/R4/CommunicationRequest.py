"""
Generated class for CommunicationRequest. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Payload(ModelBase):
    """ Text, attachment(s), or resource(s) to be communicated to the recipient.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str contentString: Message part content
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  contentString: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.contentString: str = contentString 
        

class CommunicationRequest(DomainResource):
    """ A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique identifier
    :param list['Reference'] basedOn: Fulfills plan or proposal
    :param list['Reference'] replaces: Request(s) replaced by this request
    :param 'Identifier' groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param list['CodeableConcept'] category: Message category
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param list['CodeableConcept'] medium: A channel of communication
    :param 'Reference' subject: Focus of message
    :param list['Reference'] about: Resources that pertain to this communication request
    :param 'Reference' encounter: Encounter created as part of
    :param list['Payload'] payload: Message payload
    :param str occurrenceDateTime: When scheduled
    :param str authoredOn: When request transitioned to being actionable
    :param 'Reference' requester: Who/what is requesting service
    :param list['Reference'] recipient: Message recipient
    :param 'Reference' sender: Message sender
    :param list['CodeableConcept'] reasonCode: Why is communication needed?
    :param list['Reference'] reasonReference: Why is communication needed?
    :param list['Annotation'] note: Comments made about communication request
    """
    def __init__(self, resourceType: str = "CommunicationRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: list['Reference'] = None,  replaces: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  priority: str = None,  doNotPerform: bool = None,  medium: list['CodeableConcept'] = None,  subject: 'Reference' = None,  about: list['Reference'] = None,  encounter: 'Reference' = None,  payload: list['Payload'] = None,  occurrenceDateTime: str = None,  authoredOn: str = None,  requester: 'Reference' = None,  recipient: list['Reference'] = None,  sender: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "CommunicationRequest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: list['Reference'] = basedOn or []
        self.replaces: list['Reference'] = replaces or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.category: list['CodeableConcept'] = category or []
        self.priority: str = priority 
        self.doNotPerform: bool = doNotPerform 
        self.medium: list['CodeableConcept'] = medium or []
        self.subject: 'Reference' = subject 
        self.about: list['Reference'] = about or []
        self.encounter: 'Reference' = encounter 
        self.payload: list['Payload'] = payload or []
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.recipient: list['Reference'] = recipient or []
        self.sender: 'Reference' = sender 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        