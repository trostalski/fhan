"""
Generated class for ParticipantLiving. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.generator_models import BaseModel

class ParticipantLiving(BaseModel):
    """ Logical Model: A pattern followed by resources that represent the participant in some activity, process, or responsible for providing information about a resource.
    :param str birthDate: The date of birth for the {{title}}
    :param str gender: male | female | other | unknown
    :param Attachment photo: Image of the {{title}
    :param CodeableConcept communication: Language used by {{title}}
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        
        "photo": {"class_name": "Attachment", "is_contained": False},
        
        
        "communication": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  birthDate:  'str'  = None,  gender:  'str'  = None,  photo:  list['Attachment']  = None,  communication:  list['CodeableConcept']  = None, ):
        self.resourceType = resourceType or "ParticipantLiving"
        self.birthDate = birthDate 
        self.gender = gender 
        self.photo = photo or []
        self.communication = communication or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ParticipantLiving":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ParticipantLiving":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()