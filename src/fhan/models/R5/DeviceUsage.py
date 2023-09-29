"""
Generated class for DeviceUsage. 
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
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Adherence(BaseModel):
    """ This indicates how or if the device is being used.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: always | never | sometimes
    :param CodeableConcept reason: lost | stolen | prescribed | broken | burned | forgot
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  reason:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.reason = reason or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceUsage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceUsage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceUsage(DomainResource):
    """ A record of a device being used by a patient where the record is the result of a report from the patient or a clinician.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier for this record
    :param Reference basedOn: Fulfills plan, proposal or order
    :param str status: active | completed | not-done | entered-in-error +
    :param CodeableConcept category: The category of the statement - classifying how the statement is made
    :param Reference patient: Patient using device
    :param Reference derivedFrom: Supporting information
    :param Reference context: The encounter or episode of care that establishes the context for this device use statement
    :param Timing timingTiming: How often  the device was used
    :param Period timingPeriod: How often  the device was used
    :param str timingDateTime: How often  the device was used
    :param str dateAsserted: When the statement was made (and recorded)
    :param CodeableConcept usageStatus: The status of the device usage, for example always, sometimes, never. This is not the same as the status of the statement
    :param CodeableConcept usageReason: The reason for asserting the usage status - for example forgot, lost, stolen, broken
    :param Adherence adherence: How device is being used
    :param Reference informationSource: Who made the statement
    :param CodeableReference device: Code or Reference to device used
    :param CodeableReference reason: Why device was used
    :param CodeableReference bodySite: Target body site
    :param Annotation note: Addition details (comments, instructions)
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
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        
        
        "context": {"class_name": "Reference", "is_contained": False},
        
        
        "timingTiming": {"class_name": "Timing", "is_contained": False},
        
        
        "timingPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "usageStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "usageReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "adherence": {"class_name": "Adherence", "is_contained": True},
        
        
        "informationSource": {"class_name": "Reference", "is_contained": False},
        
        
        "device": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  basedOn:  list['Reference']  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  patient:  'Reference'  = None,  derivedFrom:  list['Reference']  = None,  context:  'Reference'  = None,  timingTiming:  'Timing'  = None,  timingPeriod:  'Period'  = None,  timingDateTime:  'str'  = None,  dateAsserted:  'str'  = None,  usageStatus:  'CodeableConcept'  = None,  usageReason:  list['CodeableConcept']  = None,  adherence:  'Adherence'  = None,  informationSource:  'Reference'  = None,  device:  'CodeableReference'  = None,  reason:  list['CodeableReference']  = None,  bodySite:  'CodeableReference'  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "DeviceUsage"
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
        self.status = status 
        self.category = category or []
        self.patient = patient 
        self.derivedFrom = derivedFrom or []
        self.context = context 
        self.timingTiming = timingTiming 
        self.timingPeriod = timingPeriod 
        self.timingDateTime = timingDateTime 
        self.dateAsserted = dateAsserted 
        self.usageStatus = usageStatus 
        self.usageReason = usageReason or []
        self.adherence = adherence 
        self.informationSource = informationSource 
        self.device = device 
        self.reason = reason or []
        self.bodySite = bodySite 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceUsage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceUsage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()