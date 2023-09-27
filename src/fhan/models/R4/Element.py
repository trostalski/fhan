"""
Generated class for Element. 
Time: 2023-09-27 19:27:05
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel

class Element(BaseModel):
    """ Base StructureDefinition for Element Type: Base definition for all elements in a resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    """
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None, ):
        self.resourceType = resourceType or "Element"
        self.id = id 
        self.extension = extension or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Element":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Element":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()