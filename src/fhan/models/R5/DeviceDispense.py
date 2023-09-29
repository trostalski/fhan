"""
Generated class for DeviceDispense. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Performer(BaseModel):
    """ Indicates who or what performed the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Who performed the dispense and what they did
    :param Reference actor: Individual who was performing
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDispense":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceDispense(DomainResource):
    """ Indicates that a device is to be or has been dispensed for a named person/patient.  This includes a description of the product (supply) provided and the instructions for using the device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this dispensation
    :param Reference basedOn: The order or request that this dispense is fulfilling
    :param Reference partOf: The bigger event that this dispense is a part of
    :param str status: preparation | in-progress | cancelled | on-hold | completed | entered-in-error | stopped | declined | unknown
    :param CodeableReference statusReason: Why a dispense was or was not performed
    :param CodeableConcept category: Type of device dispense
    :param CodeableReference device: What device was supplied
    :param Reference subject: Who the dispense is for
    :param Reference receiver: Who collected the device or where the medication was delivered
    :param Reference encounter: Encounter associated with event
    :param Reference supportingInformation: Information that supports the dispensing of the device
    :param Performer performer: Who performed event
    :param Reference location: Where the dispense occurred
    :param CodeableConcept type: Trial fill, partial fill, emergency fill, etc
    :param Quantity quantity: Amount dispensed
    :param str preparedDate: When product was packaged and reviewed
    :param str whenHandedOver: When product was given out
    :param Reference destination: Where the device was sent or should be sent
    :param Annotation note: Information about the dispense
    :param str usageInstruction: Full representation of the usage instructions
    :param Reference eventHistory: A list of relevant lifecycle events
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
        
        
        
        "statusReason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "device": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "receiver": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        "destination": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        
        "eventHistory": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  basedOn:  list['Reference']  = None,  partOf:  list['Reference']  = None,  status:  'str'  = None,  statusReason:  'CodeableReference'  = None,  category:  list['CodeableConcept']  = None,  device:  'CodeableReference'  = None,  subject:  'Reference'  = None,  receiver:  'Reference'  = None,  encounter:  'Reference'  = None,  supportingInformation:  list['Reference']  = None,  performer:  list['Performer']  = None,  location:  'Reference'  = None,  type:  'CodeableConcept'  = None,  quantity:  'Quantity'  = None,  preparedDate:  'str'  = None,  whenHandedOver:  'str'  = None,  destination:  'Reference'  = None,  note:  list['Annotation']  = None,  usageInstruction:  'str'  = None,  eventHistory:  list['Reference']  = None, ):
        self.resourceType = resourceType or "DeviceDispense"
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
        self.partOf = partOf or []
        self.status = status 
        self.statusReason = statusReason 
        self.category = category or []
        self.device = device 
        self.subject = subject 
        self.receiver = receiver 
        self.encounter = encounter 
        self.supportingInformation = supportingInformation or []
        self.performer = performer or []
        self.location = location 
        self.type = type 
        self.quantity = quantity 
        self.preparedDate = preparedDate 
        self.whenHandedOver = whenHandedOver 
        self.destination = destination 
        self.note = note or []
        self.usageInstruction = usageInstruction 
        self.eventHistory = eventHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDispense":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()