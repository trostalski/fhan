"""
Generated class for DeviceRequest. 
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
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Parameter(BaseModel):
    """ Specific parameters for the ordered item.  For example, the prism value for lenses.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Device detail
    :param CodeableConcept valueCodeableConcept: Value of detail
    :param Quantity valueQuantity: Value of detail
    :param Range valueRange: Value of detail
    :param bool valueBoolean: Value of detail
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueBoolean:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueBoolean = valueBoolean 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceRequest(DomainResource):
    """ Represents a request a device to be provided to a specific patient. The device may be an implantable device to be subsequently implanted, or an external assistive device, such as a walker, to be delivered and subsequently be used.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Request identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Reference replaces: What request replaces
    :param Identifier groupIdentifier: Identifier of composite request
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if the request is to stop or not to start using the device
    :param CodeableReference code: Device requested
    :param int quantity: Quantity of devices to supply
    :param Parameter parameter: Device details
    :param Reference subject: Focus of request
    :param Reference encounter: Encounter motivating request
    :param str occurrenceDateTime: Desired time or schedule for use
    :param Period occurrencePeriod: Desired time or schedule for use
    :param Timing occurrenceTiming: Desired time or schedule for use
    :param str authoredOn: When recorded
    :param Reference requester: Who/what submitted the device request
    :param CodeableReference performer: Requested Filler
    :param CodeableReference reason: Coded/Linked Reason for request
    :param bool asNeeded: PRN status of request
    :param CodeableConcept asNeededFor: Device usage reason
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Additional clinical information
    :param Annotation note: Notes or comments
    :param Reference relevantHistory: Request provenance
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
        
        
        
        
        
        
        "code": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        "requester": {"class_name": "Reference", "is_contained": False},
        
        
        "performer": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "asNeededFor": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "insurance": {"class_name": "Reference", "is_contained": False},
        
        
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "relevantHistory": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  replaces:  list['Reference']  = None,  groupIdentifier:  'Identifier'  = None,  status:  'str'  = None,  intent:  'str'  = None,  priority:  'str'  = None,  doNotPerform:  'bool'  = None,  code:  'CodeableReference'  = None,  quantity:  'int'  = None,  parameter:  list['Parameter']  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceTiming:  'Timing'  = None,  authoredOn:  'str'  = None,  requester:  'Reference'  = None,  performer:  'CodeableReference'  = None,  reason:  list['CodeableReference']  = None,  asNeeded:  'bool'  = None,  asNeededFor:  'CodeableConcept'  = None,  insurance:  list['Reference']  = None,  supportingInfo:  list['Reference']  = None,  note:  list['Annotation']  = None,  relevantHistory:  list['Reference']  = None, ):
        self.resourceType = resourceType or "DeviceRequest"
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
        self.replaces = replaces or []
        self.groupIdentifier = groupIdentifier 
        self.status = status 
        self.intent = intent 
        self.priority = priority 
        self.doNotPerform = doNotPerform 
        self.code = code 
        self.quantity = quantity 
        self.parameter = parameter or []
        self.subject = subject 
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceTiming = occurrenceTiming 
        self.authoredOn = authoredOn 
        self.requester = requester 
        self.performer = performer 
        self.reason = reason or []
        self.asNeeded = asNeeded 
        self.asNeededFor = asNeededFor 
        self.insurance = insurance or []
        self.supportingInfo = supportingInfo or []
        self.note = note or []
        self.relevantHistory = relevantHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()