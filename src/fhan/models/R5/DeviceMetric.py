"""
Generated class for DeviceMetric. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Calibration(BaseModel):
    """ Describes the calibrations that have been performed or that are required to be performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: unspecified | offset | gain | two-point
    :param str state: not-calibrated | calibration-required | calibrated | unspecified
    :param str time: Describes the time last calibration has been performed
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  state:  'str'  = None,  time:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.state = state 
        self.time = time 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceMetric":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceMetric":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceMetric(DomainResource):
    """ Describes a measurement, calculation or setting capability of a device.  The DeviceMetric resource is derived from the ISO/IEEE 11073-10201 Domain Information Model standard, but is more widely applicable. 
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param CodeableConcept type: Identity of metric, for example Heart Rate or PEEP Setting
    :param CodeableConcept unit: Unit of Measure for the Metric
    :param Reference device: Describes the link to the Device
    :param str operationalStatus: on | off | standby | entered-in-error
    :param str color: Color name (from CSS4) or #RRGGBB code
    :param str category: measurement | setting | calculation | unspecified
    :param Quantity measurementFrequency: Indicates how often the metric is taken or recorded
    :param Calibration calibration: Describes the calibrations that have been performed or that are required to be performed
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "unit": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "measurementFrequency": {"class_name": "Quantity", "is_contained": False},
        
        
        "calibration": {"class_name": "Calibration", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  type:  'CodeableConcept'  = None,  unit:  'CodeableConcept'  = None,  device:  'Reference'  = None,  operationalStatus:  'str'  = None,  color:  'str'  = None,  category:  'str'  = None,  measurementFrequency:  'Quantity'  = None,  calibration:  list['Calibration']  = None, ):
        self.resourceType = resourceType or "DeviceMetric"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type 
        self.unit = unit 
        self.device = device 
        self.operationalStatus = operationalStatus 
        self.color = color 
        self.category = category 
        self.measurementFrequency = measurementFrequency 
        self.calibration = calibration or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceMetric":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceMetric":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()