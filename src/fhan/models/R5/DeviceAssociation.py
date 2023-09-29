"""
Generated class for DeviceAssociation. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Operation(BaseModel):
    """ The details about the device when it is in use to describe its operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept status: Device operational condition
    :param Reference operator: The individual performing the action enabled by the device
    :param Period period: Begin and end dates and times for the device's operation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "operator": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  status:  'CodeableConcept'  = None,  operator:  list['Reference']  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status 
        self.operator = operator or []
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceAssociation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceAssociation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceAssociation(DomainResource):
    """ A record of association of a device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param Reference device: Reference to the devices associated with the patient or group
    :param CodeableConcept category: Describes the relationship between the device and subject
    :param CodeableConcept status: implanted | explanted | attached | entered-in-error | unknown
    :param CodeableConcept statusReason: The reasons given for the current association status
    :param Reference subject: The individual, group of individuals or device that the device is on or associated with
    :param Reference bodyStructure: Current anatomical location of the device in/on subject
    :param Period period: Begin and end dates and times for the device association
    :param Operation operation: The details about the device when it is in use to describe its operation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "bodyStructure": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "operation": {"class_name": "Operation", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  device:  'Reference'  = None,  category:  list['CodeableConcept']  = None,  status:  'CodeableConcept'  = None,  statusReason:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  bodyStructure:  'Reference'  = None,  period:  'Period'  = None,  operation:  list['Operation']  = None, ):
        self.resourceType = resourceType or "DeviceAssociation"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.device = device 
        self.category = category or []
        self.status = status 
        self.statusReason = statusReason or []
        self.subject = subject 
        self.bodyStructure = bodyStructure 
        self.period = period 
        self.operation = operation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceAssociation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceAssociation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()