"""
Generated class for RelatedArtifact. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *
from fhan.models.generator_models import BaseModel

class RelatedArtifact(BaseModel):
    """ RelatedArtifact Type: Related artifacts such as additional documentation, justification, or bibliographic references.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of | part-of | amends | amended-with | appends | appended-with | cites | cited-by | comments-on | comment-in | contains | contained-in | corrects | correction-in | replaces | replaced-with | retracts | retracted-by | signs | similar-to | supports | supported-with | transforms | transformed-into | transformed-with | documents | specification-of | created-with | cite-as
    :param CodeableConcept classifier: Additional classifiers
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param Attachment document: What document is being referenced
    :param str resource: What artifact is being referenced
    :param Reference resourceReference: What artifact, if not a conformance resource
    :param str publicationStatus: draft | active | retired | unknown
    :param str publicationDate: Date of publication of the artifact being referred to
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "document": {"class_name": "Attachment", "is_contained": False},
        
        
        
        "resourceReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  type:  'str'  = None,  classifier:  list['CodeableConcept']  = None,  label:  'str'  = None,  display:  'str'  = None,  citation:  'str'  = None,  document:  'Attachment'  = None,  resource:  'str'  = None,  resourceReference:  'Reference'  = None,  publicationStatus:  'str'  = None,  publicationDate:  'str'  = None, ):
        self.resourceType = resourceType or "RelatedArtifact"
        self.id = id 
        self.extension = extension or []
        self.type = type 
        self.classifier = classifier or []
        self.label = label 
        self.display = display 
        self.citation = citation 
        self.document = document 
        self.resource = resource 
        self.resourceReference = resourceReference 
        self.publicationStatus = publicationStatus 
        self.publicationDate = publicationDate 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RelatedArtifact":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RelatedArtifact":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()