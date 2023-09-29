"""
Generated class for Base. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.generator_models import BaseModel

class Base(BaseModel):
    """ Base Type: Base definition for all types defined in FHIR type system.
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        }
    def __init__(self, resourceType: str = None, ):
        self.resourceType = resourceType or "Base"
        

    @classmethod
    def from_dict(cls, data: dict) -> "Base":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Base":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()