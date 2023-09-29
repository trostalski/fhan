"""
Generated class for CommunicationRequest. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Payload(BaseModel):
    """ Text, attachment(s), or resource(s) to be communicated to the recipient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Message part content
    :param Reference contentReference: Message part content
    :param CodeableConcept contentCodeableConcept: Message part content
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "contentAttachment": {"class_name": "Attachment", "is_contained": False},
        
        
        "contentReference": {"class_name": "Reference", "is_contained": False},
        
        
        "contentCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  contentAttachment:  'Attachment'  = None,  contentReference:  'Reference'  = None,  contentCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.contentAttachment = contentAttachment 
        self.contentReference = contentReference 
        self.contentCodeableConcept = contentCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "CommunicationRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "CommunicationRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CommunicationRequest(DomainResource):
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
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Message category
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param CodeableConcept medium: A channel of communication
    :param Reference subject: Focus of message
    :param Reference about: Resources that pertain to this communication request
    :param Reference encounter: The Encounter during which this CommunicationRequest was created
    :param Payload payload: Message payload
    :param str occurrenceDateTime: When scheduled
    :param Period occurrencePeriod: When scheduled
    :param str authoredOn: When request transitioned to being actionable
    :param Reference requester: Who asks for the information to be shared
    :param Reference recipient: Who to share the information with
    :param Reference informationProvider: Who should share the information
    :param CodeableReference reason: Why is communication needed?
    :param Annotation note: Comments made about communication request
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "replaces": {"class_name": "Reference", "is_contained": False},
        
        
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "medium": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "about": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "payload": {"class_name": "Payload", "is_contained": True},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "requester": {"class_name": "Reference", "is_contained": False},
        
        
        "recipient": {"class_name": "Reference", "is_contained": False},
        
        
        "informationProvider": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  basedOn:  list['Reference']  = None,  replaces:  list['Reference']  = None,  groupIdentifier:  'Identifier'  = None,  status:  'str'  = None,  statusReason:  'CodeableConcept'  = None,  intent:  'str'  = None,  category:  list['CodeableConcept']  = None,  priority:  'str'  = None,  doNotPerform:  'bool'  = None,  medium:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  about:  list['Reference']  = None,  encounter:  'Reference'  = None,  payload:  list['Payload']  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  authoredOn:  'str'  = None,  requester:  'Reference'  = None,  recipient:  list['Reference']  = None,  informationProvider:  list['Reference']  = None,  reason:  list['CodeableReference']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "CommunicationRequest"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.replaces = replaces or []
        self.groupIdentifier = groupIdentifier 
        self.status = status 
        self.statusReason = statusReason 
        self.intent = intent 
        self.category = category or []
        self.priority = priority 
        self.doNotPerform = doNotPerform 
        self.medium = medium or []
        self.subject = subject 
        self.about = about or []
        self.encounter = encounter 
        self.payload = payload or []
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.authoredOn = authoredOn 
        self.requester = requester 
        self.recipient = recipient or []
        self.informationProvider = informationProvider or []
        self.reason = reason or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CommunicationRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "CommunicationRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()