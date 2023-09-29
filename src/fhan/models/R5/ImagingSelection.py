"""
Generated class for ImagingSelection. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Performer(BaseModel):
    """ Selector of the instances – human or machine.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performer
    :param Reference actor: Author (human or machine)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingSelection":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ImagingSelection":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class ImageRegion2D(BaseModel):
    """ Each imaging selection instance or frame list might includes an image region, specified by a region type and a set of 2D coordinates.
       If the parent imagingSelection.instance contains a subset element of type frame, the image region applies to all frames in the subset list.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str regionType: point | polyline | interpolated | circle | ellipse
    :param float coordinate: Specifies the coordinates that define the image region
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  regionType:  'str'  = None,  coordinate:  list['float']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.regionType = regionType 
        self.coordinate = coordinate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingSelection":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ImagingSelection":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ImageRegion3D(BaseModel):
    """ Each imaging selection might includes a 3D image region, specified by a region type and a set of 3D coordinates.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str regionType: point | multipoint | polyline | polygon | ellipse | ellipsoid
    :param float coordinate: Specifies the coordinates that define the image region
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  regionType:  'str'  = None,  coordinate:  list['float']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.regionType = regionType 
        self.coordinate = coordinate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingSelection":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ImagingSelection":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Instance(BaseModel):
    """ Each imaging selection includes one or more selected DICOM SOP instances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param int number: DICOM Instance Number
    :param Coding sopClass: DICOM SOP Class UID
    :param str subset: The selected subset of the SOP Instance
    :param ImageRegion2D imageRegion2D: A specific 2D region in a DICOM image / frame
    :param ImageRegion3D imageRegion3D: A specific 3D region in a DICOM frame of reference
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "sopClass": {"class_name": "Coding", "is_contained": False},
        
        
        
        "imageRegion2D": {"class_name": "ImageRegion2D", "is_contained": True},
        
        
        "imageRegion3D": {"class_name": "ImageRegion3D", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  uid:  'str'  = None,  number:  'int'  = None,  sopClass:  'Coding'  = None,  subset:  list['str']  = None,  imageRegion2D:  list['ImageRegion2D']  = None,  imageRegion3D:  list['ImageRegion3D']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.uid = uid 
        self.number = number 
        self.sopClass = sopClass 
        self.subset = subset or []
        self.imageRegion2D = imageRegion2D or []
        self.imageRegion3D = imageRegion3D or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingSelection":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ImagingSelection":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ImagingSelection(DomainResource):
    """ A selection of DICOM SOP instances and/or frames within a single Study and Series. This might include additional specifics such as an image region, an Observation UID or a Segmentation Number, allowing linkage to an Observation Resource or transferring this information along with the ImagingStudy Resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for Imaging Selection
    :param str status: available | entered-in-error | unknown
    :param Reference subject: Subject of the selected instances
    :param str issued: Date / Time when this imaging selection was created
    :param Performer performer: Selector of the instances (human or machine)
    :param Reference basedOn: Associated request
    :param CodeableConcept category: Classifies the imaging selection
    :param CodeableConcept code: Imaging Selection purpose text or code
    :param str studyUid: DICOM Study Instance UID
    :param Reference derivedFrom: The imaging study from which the imaging selection is derived
    :param Reference endpoint: The network service providing retrieval for the images referenced in the imaging selection
    :param str seriesUid: DICOM Series Instance UID
    :param int seriesNumber: DICOM Series Number
    :param str frameOfReferenceUid: The Frame of Reference UID for the selected images
    :param CodeableReference bodySite: Body part examined
    :param Reference focus: Related resource that is the focus for the imaging selection
    :param Instance instance: The selected instances
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        
        
        "endpoint": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "bodySite": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "instance": {"class_name": "Instance", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  subject:  'Reference'  = None,  issued:  'str'  = None,  performer:  list['Performer']  = None,  basedOn:  list['Reference']  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  studyUid:  'str'  = None,  derivedFrom:  list['Reference']  = None,  endpoint:  list['Reference']  = None,  seriesUid:  'str'  = None,  seriesNumber:  'int'  = None,  frameOfReferenceUid:  'str'  = None,  bodySite:  'CodeableReference'  = None,  focus:  list['Reference']  = None,  instance:  list['Instance']  = None, ):
        self.resourceType = resourceType or "ImagingSelection"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.subject = subject 
        self.issued = issued 
        self.performer = performer or []
        self.basedOn = basedOn or []
        self.category = category or []
        self.code = code 
        self.studyUid = studyUid 
        self.derivedFrom = derivedFrom or []
        self.endpoint = endpoint or []
        self.seriesUid = seriesUid 
        self.seriesNumber = seriesNumber 
        self.frameOfReferenceUid = frameOfReferenceUid 
        self.bodySite = bodySite 
        self.focus = focus or []
        self.instance = instance or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingSelection":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ImagingSelection":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()