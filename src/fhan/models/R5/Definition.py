"""
Generated class for Definition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Coding import *
from fhan.models.generator_models import BaseModel

class Definition(BaseModel):
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param str url: Canonical identifier for this {{title}}, represented as an absolute URI (globally unique)
    :param Identifier identifier: Business identifier for {{title}}
    :param str version: Business version of the {{title}}
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this {{title}} (computer friendly)
    :param str title: Name for this {{title}} (human friendly)
    :param str derivedFromCanonical: Based on FHIR protocol or definition
    :param str derivedFromUri: Based on external protocol or definition
    :param str partOf: Part of referenced definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableReference subject: Type of individual the defined service is for
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the {{title}}
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the {{title}} was approved by publisher
    :param str lastReviewDate: When the {{title}} was last reviewed
    :param Period effectivePeriod: When the {{title}} is expected to be used
    :param CodeableConcept topic: Descriptive topics related to the content of the {{title}}. Topics provide a high-level categorization as well as keywords for the {{title}} that can be useful for filtering and searching
    :param CodeableConcept performerType: Desired kind of service performer
    :param CodeableConcept code: Service to be done
    :param CodeableReference product: Product to use/manipulate
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        
        "subject": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "product": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  derivedFromCanonical:  list['str']  = None,  derivedFromUri:  list['str']  = None,  partOf:  list['str']  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  subject:  list['CodeableReference']  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  performerType:  'CodeableConcept'  = None,  code:  'CodeableConcept'  = None,  product:  'CodeableReference'  = None, ):
        self.resourceType = resourceType or "Definition"
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.derivedFromCanonical = derivedFromCanonical or []
        self.derivedFromUri = derivedFromUri or []
        self.partOf = partOf or []
        self.status = status 
        self.experimental = experimental 
        self.subject = subject or []
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.topic = topic or []
        self.performerType = performerType 
        self.code = code 
        self.product = product 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Definition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Definition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()