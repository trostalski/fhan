"""
Generated class for ArtifactAssessment. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Content(BaseModel):
    """ A component comment, classifier, or rating of the artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str informationType: comment | classifier | rating | container | response | change-request
    :param str summary: Brief summary of the content
    :param CodeableConcept type: What type of content
    :param CodeableConcept classifier: Rating, classifier, or assessment
    :param Quantity quantity: Quantitative rating
    :param Reference author: Who authored the content
    :param str path: What the comment is directed to
    :param RelatedArtifact relatedArtifact: Additional information
    :param bool freeToShare: Acceptable to publicly share the resource content
    :param Component component: Contained content
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        "component": {"class_name": "Component", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  informationType:  'str'  = None,  summary:  'str'  = None,  type:  'CodeableConcept'  = None,  classifier:  list['CodeableConcept']  = None,  quantity:  'Quantity'  = None,  author:  'Reference'  = None,  path:  list['str']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  freeToShare:  'bool'  = None,  component:  list['Component']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.informationType = informationType 
        self.summary = summary 
        self.type = type 
        self.classifier = classifier or []
        self.quantity = quantity 
        self.author = author 
        self.path = path or []
        self.relatedArtifact = relatedArtifact or []
        self.freeToShare = freeToShare 
        self.component = component or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ArtifactAssessment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ArtifactAssessment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ArtifactAssessment(DomainResource):
    """ This Resource provides one or more comments, classifiers or ratings about a Resource and supports attribution and rights management metadata for the added content.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Additional identifier for the artifact assessment
    :param str title: A short title for the assessment for use in displaying and selecting
    :param Reference citeAsReference: How to cite the comment or rating
    :param str citeAsMarkdown: How to cite the comment or rating
    :param str date: Date last changed
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the artifact assessment was approved by publisher
    :param str lastReviewDate: When the artifact assessment was last reviewed by the publisher
    :param Reference artifactReference: The artifact assessed, commented upon or rated
    :param str artifactCanonical: The artifact assessed, commented upon or rated
    :param str artifactUri: The artifact assessed, commented upon or rated
    :param Content content: Comment, classifier, or rating content
    :param str workflowStatus: submitted | triaged | waiting-for-input | resolved-no-change | resolved-change-required | deferred | duplicate | applied | published | entered-in-error
    :param str disposition: unresolved | not-persuasive | persuasive | persuasive-with-modification | not-persuasive-with-modification
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "citeAsReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        
        
        "artifactReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "content": {"class_name": "Content", "is_contained": True},
        
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  title:  'str'  = None,  citeAsReference:  'Reference'  = None,  citeAsMarkdown:  'str'  = None,  date:  'str'  = None,  copyright:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  artifactReference:  'Reference'  = None,  artifactCanonical:  'str'  = None,  artifactUri:  'str'  = None,  content:  list['Content']  = None,  workflowStatus:  'str'  = None,  disposition:  'str'  = None, ):
        self.resourceType = resourceType or "ArtifactAssessment"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.title = title 
        self.citeAsReference = citeAsReference 
        self.citeAsMarkdown = citeAsMarkdown 
        self.date = date 
        self.copyright = copyright 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.artifactReference = artifactReference 
        self.artifactCanonical = artifactCanonical 
        self.artifactUri = artifactUri 
        self.content = content or []
        self.workflowStatus = workflowStatus 
        self.disposition = disposition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ArtifactAssessment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ArtifactAssessment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()