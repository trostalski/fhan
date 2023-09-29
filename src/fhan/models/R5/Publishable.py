"""
Generated class for Publishable. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.generator_models import BaseModel

class Publishable(BaseModel):
    """ Logical Model: A pattern to be followed by resources that represent a publishable knowledge artifact such as a ValueSet, Profile, Library, Decision Support Rule, or Quality Measure.
    :param Identifier identifier: Additional identifier for the {{title}}
    :param str date: Date last changed
    :param ContactDetail contact: Contact details for the publisher
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the {{title}} was approved by publisher
    :param str lastReviewDate: When the {{title}} was last reviewed
    :param Period effectivePeriod: When the {{title}} is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the {{title}}
    :param ContactDetail editor: Who edited the {{title}}
    :param ContactDetail reviewer: Who reviewed the {{title}}
    :param ContactDetail endorser: Who endorsed the {{title}}
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  identifier:  list['Identifier']  = None,  date:  'str'  = None,  contact:  list['ContactDetail']  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None, ):
        self.resourceType = resourceType or "Publishable"
        self.identifier = identifier or []
        self.date = date 
        self.contact = contact or []
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.topic = topic or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Publishable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Publishable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()