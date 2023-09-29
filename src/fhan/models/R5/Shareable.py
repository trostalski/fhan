"""
Generated class for Shareable. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Coding import *
from fhan.models.generator_models import BaseModel

class Shareable(BaseModel):
    """ Logical Model: A pattern to be followed by [canonical resources](canonicalresource.html) that meet minimal requirements for sharing via registries or similar mechanisms.
    :param str url: Canonical identifier for this {{title}}, represented as a URI (globally unique)
    :param str version: Business version of the {{title}}
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this {{title}} (computer friendly)
    :param str title: Name for this {{title}} (human-friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str publisher: Name of the publisher (or steward) (organization or individual)
    :param str description: Natural language description of the {{title}}
    :param CodeableConcept knowledgeRepresentationLevel: narrative | semi-structured | structured | executable
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        "knowledgeRepresentationLevel": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  url:  'str'  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  publisher:  'str'  = None,  description:  'str'  = None,  knowledgeRepresentationLevel:  list['CodeableConcept']  = None, ):
        self.resourceType = resourceType or "Shareable"
        self.url = url 
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.status = status 
        self.experimental = experimental 
        self.publisher = publisher 
        self.description = description 
        self.knowledgeRepresentationLevel = knowledgeRepresentationLevel or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Shareable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Shareable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()