"""
Generated class for Specimen. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Feature(BaseModel):
    """ A physical feature or landmark on a specimen, highlighted for context by the collector of the specimen (e.g. surgeon), that identifies the type of feature as well as its meaning (e.g. the red ink indicating the resection margin of the right lobe of the excised prostate tissue or wire loop at radiologically suspected tumor location).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Highlighted feature
    :param str description: Information about the feature
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  description:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.description = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Collection(BaseModel):
    """ Details concerning the specimen collection.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Who collected the specimen
    :param str collectedDateTime: Collection time
    :param Period collectedPeriod: Collection time
    :param Duration duration: How long it took to collect specimen
    :param Quantity quantity: The quantity of specimen collected
    :param CodeableConcept method: Technique used to perform collection
    :param CodeableReference device: Device used to perform collection
    :param Reference procedure: The procedure that collects the specimen
    :param CodeableReference bodySite: Anatomical collection site
    :param CodeableConcept fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param Duration fastingStatusDuration: Whether or how long patient abstained from food and/or drink
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "collector": {"class_name": "Reference", "is_contained": False},
        
        
        
        "collectedPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "duration": {"class_name": "Duration", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "device": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "procedure": {"class_name": "Reference", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "fastingStatusCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "fastingStatusDuration": {"class_name": "Duration", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  collector:  'Reference'  = None,  collectedDateTime:  'str'  = None,  collectedPeriod:  'Period'  = None,  duration:  'Duration'  = None,  quantity:  'Quantity'  = None,  method:  'CodeableConcept'  = None,  device:  'CodeableReference'  = None,  procedure:  'Reference'  = None,  bodySite:  'CodeableReference'  = None,  fastingStatusCodeableConcept:  'CodeableConcept'  = None,  fastingStatusDuration:  'Duration'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.collector = collector 
        self.collectedDateTime = collectedDateTime 
        self.collectedPeriod = collectedPeriod 
        self.duration = duration 
        self.quantity = quantity 
        self.method = method 
        self.device = device 
        self.procedure = procedure 
        self.bodySite = bodySite 
        self.fastingStatusCodeableConcept = fastingStatusCodeableConcept 
        self.fastingStatusDuration = fastingStatusDuration 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Processing(BaseModel):
    """ Details concerning processing and processing steps for the specimen.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param CodeableConcept method: Indicates the treatment step  applied to the specimen
    :param Reference additive: Material used in the processing step
    :param str timeDateTime: Date and time of specimen processing
    :param Period timePeriod: Date and time of specimen processing
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "additive": {"class_name": "Reference", "is_contained": False},
        
        
        
        "timePeriod": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  method:  'CodeableConcept'  = None,  additive:  list['Reference']  = None,  timeDateTime:  'str'  = None,  timePeriod:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.method = method 
        self.additive = additive or []
        self.timeDateTime = timeDateTime 
        self.timePeriod = timePeriod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Container(BaseModel):
    """ The container holding the specimen.  The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference device: Device resource for the container
    :param Reference location: Where the container is
    :param Quantity specimenQuantity: Quantity of specimen within container
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "specimenQuantity": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  device:  'Reference'  = None,  location:  'Reference'  = None,  specimenQuantity:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.device = device 
        self.location = location 
        self.specimenQuantity = specimenQuantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Specimen(DomainResource):
    """ A sample to be used for analysis.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Identifier
    :param Identifier accessionIdentifier: Identifier assigned by the lab
    :param str status: available | unavailable | unsatisfactory | entered-in-error
    :param CodeableConcept type: Kind of material that forms the specimen
    :param Reference subject: Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance, a biologically-derived product, or a device
    :param str receivedTime: The time when specimen is received by the testing laboratory
    :param Reference parent: Specimen from which this specimen originated
    :param Reference request: Why the specimen was collected
    :param str combined: grouped | pooled
    :param CodeableConcept role: The role the specimen serves
    :param Feature feature: The physical feature of a specimen
    :param Collection collection: Collection details
    :param Processing processing: Processing and processing step details
    :param Container container: Direct container of specimen (tube/slide, etc.)
    :param CodeableConcept condition: State of the specimen
    :param Annotation note: Comments
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "accessionIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        
        "parent": {"class_name": "Reference", "is_contained": False},
        
        
        "request": {"class_name": "Reference", "is_contained": False},
        
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "feature": {"class_name": "Feature", "is_contained": True},
        
        
        "collection": {"class_name": "Collection", "is_contained": True},
        
        
        "processing": {"class_name": "Processing", "is_contained": True},
        
        
        "container": {"class_name": "Container", "is_contained": True},
        
        
        "condition": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  accessionIdentifier:  'Identifier'  = None,  status:  'str'  = None,  type:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  receivedTime:  'str'  = None,  parent:  list['Reference']  = None,  request:  list['Reference']  = None,  combined:  'str'  = None,  role:  list['CodeableConcept']  = None,  feature:  list['Feature']  = None,  collection:  'Collection'  = None,  processing:  list['Processing']  = None,  container:  list['Container']  = None,  condition:  list['CodeableConcept']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "Specimen"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.accessionIdentifier = accessionIdentifier 
        self.status = status 
        self.type = type 
        self.subject = subject 
        self.receivedTime = receivedTime 
        self.parent = parent or []
        self.request = request or []
        self.combined = combined 
        self.role = role or []
        self.feature = feature or []
        self.collection = collection 
        self.processing = processing or []
        self.container = container or []
        self.condition = condition or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()