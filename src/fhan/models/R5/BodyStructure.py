"""
Generated class for BodyStructure. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
        
    
    

class DistanceFromLandmark(BaseModel):
    """ The distance in centimeters a certain observation is made from a body landmark.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference device: Measurement device
    :param Quantity value: Measured distance from body landmark
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "device": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "value": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  device:  list['CodeableReference']  = None,  value:  list['Quantity']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.device = device or []
        self.value = value or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "BodyStructure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BodyStructure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class BodyLandmarkOrientation(BaseModel):
    """ Body locations in relation to a specific body landmark (tatoo, scar, other body structure).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept landmarkDescription: Body ]andmark description
    :param CodeableConcept clockFacePosition: Clockface orientation
    :param DistanceFromLandmark distanceFromLandmark: Landmark relative location
    :param CodeableConcept surfaceOrientation: Relative landmark surface orientation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "landmarkDescription": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "clockFacePosition": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "distanceFromLandmark": {"class_name": "DistanceFromLandmark", "is_contained": True},
        
        
        "surfaceOrientation": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  landmarkDescription:  list['CodeableConcept']  = None,  clockFacePosition:  list['CodeableConcept']  = None,  distanceFromLandmark:  list['DistanceFromLandmark']  = None,  surfaceOrientation:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.landmarkDescription = landmarkDescription or []
        self.clockFacePosition = clockFacePosition or []
        self.distanceFromLandmark = distanceFromLandmark or []
        self.surfaceOrientation = surfaceOrientation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "BodyStructure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BodyStructure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class IncludedStructure(BaseModel):
    """ The anatomical location(s) or region(s) of the specimen, lesion, or body structure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept structure: Code that represents the included structure
    :param CodeableConcept laterality: Code that represents the included structure laterality
    :param BodyLandmarkOrientation bodyLandmarkOrientation: Landmark relative location
    :param Reference spatialReference: Cartesian reference for structure
    :param CodeableConcept qualifier: Code that represents the included structure qualifier
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "structure": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "laterality": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "bodyLandmarkOrientation": {"class_name": "BodyLandmarkOrientation", "is_contained": True},
        
        
        "spatialReference": {"class_name": "Reference", "is_contained": False},
        
        
        "qualifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  structure:  'CodeableConcept'  = None,  laterality:  'CodeableConcept'  = None,  bodyLandmarkOrientation:  list['BodyLandmarkOrientation']  = None,  spatialReference:  list['Reference']  = None,  qualifier:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.structure = structure 
        self.laterality = laterality 
        self.bodyLandmarkOrientation = bodyLandmarkOrientation or []
        self.spatialReference = spatialReference or []
        self.qualifier = qualifier or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "BodyStructure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BodyStructure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BodyStructure(DomainResource):
    """ Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Bodystructure identifier
    :param bool active: Whether this record is in active use
    :param CodeableConcept morphology: Kind of Structure
    :param IncludedStructure includedStructure: Included anatomic location(s)
    :param ExcludedStructure excludedStructure: Excluded anatomic locations(s)
    :param str description: Text description
    :param Attachment image: Attached images
    :param Reference patient: Who this is about
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "morphology": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "includedStructure": {"class_name": "IncludedStructure", "is_contained": True},
        
        
        "excludedStructure": {"class_name": "ExcludedStructure", "is_contained": True},
        
        
        
        "image": {"class_name": "Attachment", "is_contained": False},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  active:  'bool'  = None,  morphology:  'CodeableConcept'  = None,  includedStructure:  list['IncludedStructure']  = None,  excludedStructure:  list['ExcludedStructure']  = None,  description:  'str'  = None,  image:  list['Attachment']  = None,  patient:  'Reference'  = None, ):
        self.resourceType = resourceType or "BodyStructure"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active 
        self.morphology = morphology 
        self.includedStructure = includedStructure or []
        self.excludedStructure = excludedStructure or []
        self.description = description 
        self.image = image or []
        self.patient = patient 
        

    @classmethod
    def from_dict(cls, data: dict) -> "BodyStructure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BodyStructure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()