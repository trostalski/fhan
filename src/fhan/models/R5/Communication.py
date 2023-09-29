"""
Generated class for Communication. 
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
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Payload(BaseModel):
    """ Text, attachment(s), or resource(s) that was communicated to the recipient.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "Communication":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Communication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Communication(DomainResource):
    """ A clinical or business level record of information being transmitted or shared; e.g. an alert that was sent to a responsible provider, a public health agency communication to a provider/reporter in response to a case report for a reportable condition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Request fulfilled by this communication
    :param Reference partOf: Part of referenced event (e.g. Communication, Procedure)
    :param Reference inResponseTo: Reply to
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: Message category
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept medium: A channel of communication
    :param Reference subject: Focus of message
    :param CodeableConcept topic: Description of the purpose/content
    :param Reference about: Resources that pertain to this communication
    :param Reference encounter: The Encounter during which this Communication was created
    :param str sent: When sent
    :param str received: When received
    :param Reference recipient: Who the information is shared with
    :param Reference sender: Who shares the information
    :param CodeableReference reason: Indication for message
    :param Payload payload: Message payload
    :param Annotation note: Comments made about the communication
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
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        "inResponseTo": {"class_name": "Reference", "is_contained": False},
        
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "medium": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "about": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "recipient": {"class_name": "Reference", "is_contained": False},
        
        
        "sender": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "payload": {"class_name": "Payload", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  partOf:  list['Reference']  = None,  inResponseTo:  list['Reference']  = None,  status:  'str'  = None,  statusReason:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  priority:  'str'  = None,  medium:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  topic:  'CodeableConcept'  = None,  about:  list['Reference']  = None,  encounter:  'Reference'  = None,  sent:  'str'  = None,  received:  'str'  = None,  recipient:  list['Reference']  = None,  sender:  'Reference'  = None,  reason:  list['CodeableReference']  = None,  payload:  list['Payload']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "Communication"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.inResponseTo = inResponseTo or []
        self.status = status 
        self.statusReason = statusReason 
        self.category = category or []
        self.priority = priority 
        self.medium = medium or []
        self.subject = subject 
        self.topic = topic 
        self.about = about or []
        self.encounter = encounter 
        self.sent = sent 
        self.received = received 
        self.recipient = recipient or []
        self.sender = sender 
        self.reason = reason or []
        self.payload = payload or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Communication":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Communication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()