"""
Generated class for ChargeItemDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.MonetaryComponent import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Applicability(BaseModel):
    """ Expressions that describe applicability criteria for the billing code.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Expression condition: Boolean-valued expression
    :param Period effectivePeriod: When the charge item definition is expected to be used
    :param RelatedArtifact relatedArtifact: Reference to / quotation of the external source of the group of properties
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "condition": {"class_name": "Expression", "is_contained": False},
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  condition:  'Expression'  = None,  effectivePeriod:  'Period'  = None,  relatedArtifact:  'RelatedArtifact'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.condition = condition 
        self.effectivePeriod = effectivePeriod 
        self.relatedArtifact = relatedArtifact 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class PropertyGroup(BaseModel):
    """ Group of properties which are applicable under the same conditions. If no applicability rules are established for the group, then all properties always apply.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Applicability applicability: Conditions under which the priceComponent is applicable
    :param MonetaryComponent priceComponent: Components of total line item price
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "applicability": {"class_name": "Applicability", "is_contained": True},
        
        
        "priceComponent": {"class_name": "MonetaryComponent", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  applicability:  list['Applicability']  = None,  priceComponent:  list['MonetaryComponent']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.applicability = applicability or []
        self.priceComponent = priceComponent or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ChargeItemDefinition(DomainResource):
    """ The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this charge item definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the charge item definition
    :param str version: Business version of the charge item definition
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this charge item definition (computer friendly)
    :param str title: Name for this charge item definition (human friendly)
    :param str derivedFromUri: Underlying externally-defined charge item definition
    :param str partOf: A larger definition of which this particular definition is a component or step
    :param str replaces: Completed or terminated request(s) whose function is taken by this new request
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the charge item definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for charge item definition (if applicable)
    :param str purpose: Why this charge item definition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the charge item definition was approved by publisher
    :param str lastReviewDate: When the charge item definition was last reviewed by the publisher
    :param CodeableConcept code: Billing code or product type this definition applies to
    :param Reference instance: Instances this definition applies to
    :param Applicability applicability: Whether or not the billing code is applicable
    :param PropertyGroup propertyGroup: Group of properties which are applicable under the same conditions
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "instance": {"class_name": "Reference", "is_contained": False},
        
        
        "applicability": {"class_name": "Applicability", "is_contained": True},
        
        
        "propertyGroup": {"class_name": "PropertyGroup", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  derivedFromUri:  list['str']  = None,  partOf:  list['str']  = None,  replaces:  list['str']  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  code:  'CodeableConcept'  = None,  instance:  list['Reference']  = None,  applicability:  list['Applicability']  = None,  propertyGroup:  list['PropertyGroup']  = None, ):
        self.resourceType = resourceType or "ChargeItemDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.derivedFromUri = derivedFromUri or []
        self.partOf = partOf or []
        self.replaces = replaces or []
        self.status = status 
        self.experimental = experimental 
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
        self.code = code 
        self.instance = instance or []
        self.applicability = applicability or []
        self.propertyGroup = propertyGroup or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()