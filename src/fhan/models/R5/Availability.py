"""
Generated class for Availability. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Period import *
from fhan.models.R5.Element import *
from fhan.models.R5.Extension import *
from fhan.models.generator_models import BaseModel

    
    

class AvailableTime(BaseModel):
    """ Times the {item} is available.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? i.e. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  daysOfWeek:  list['str']  = None,  allDay:  'bool'  = None,  availableStartTime:  'str'  = None,  availableEndTime:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.daysOfWeek = daysOfWeek or []
        self.allDay = allDay 
        self.availableStartTime = availableStartTime 
        self.availableEndTime = availableEndTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Availability":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Availability":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class NotAvailableTime(BaseModel):
    """ Not available during this time due to provided reason.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available during this period
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "during": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  description:  'str'  = None,  during:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.description = description 
        self.during = during 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Availability":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Availability":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Availability(BaseModel):
    """ Availability Type: Availability data for an {item}.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param AvailableTime availableTime: Times the {item} is available
    :param NotAvailableTime notAvailableTime: Not available during this time due to provided reason
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "availableTime": {"class_name": "AvailableTime", "is_contained": True},
        
        
        "notAvailableTime": {"class_name": "NotAvailableTime", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  availableTime:  list['AvailableTime']  = None,  notAvailableTime:  list['NotAvailableTime']  = None, ):
        self.resourceType = resourceType or "Availability"
        self.id = id 
        self.extension = extension or []
        self.availableTime = availableTime or []
        self.notAvailableTime = notAvailableTime or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Availability":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Availability":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()