"""
Generated class for EvidenceVariable. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class DefinitionByTypeAndValue(BaseModel):
    """ Defines the characteristic using both a type and value[x] elements.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Expresses the type of characteristic
    :param CodeableConcept method: Method for how the characteristic value was determined
    :param Reference device: Device used for determining characteristic
    :param CodeableConcept valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param bool valueBoolean: Defines the characteristic when coupled with characteristic.type
    :param Quantity valueQuantity: Defines the characteristic when coupled with characteristic.type
    :param Range valueRange: Defines the characteristic when coupled with characteristic.type
    :param Reference valueReference: Defines the characteristic when coupled with characteristic.type
    :param str valueId: Defines the characteristic when coupled with characteristic.type
    :param CodeableConcept offset: Reference point for valueQuantity or valueRange
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "offset": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  method:  list['CodeableConcept']  = None,  device:  'Reference'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueBoolean:  'bool'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueReference:  'Reference'  = None,  valueId:  'str'  = None,  offset:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.method = method or []
        self.device = device 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueBoolean = valueBoolean 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueReference = valueReference 
        self.valueId = valueId 
        self.offset = offset 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class DefinitionByCombination(BaseModel):
    """ Defines the characteristic as a combination of two or more characteristics.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: all-of | any-of | at-least | at-most | statistical | net-effect | dataset
    :param int threshold: Provides the value of "n" when "at-least" or "at-most" codes are used
    :param Characteristic characteristic: A defining factor of the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  threshold:  'int'  = None,  characteristic:  list['Characteristic']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.threshold = threshold 
        self.characteristic = characteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class TimeFromEvent(BaseModel):
    """ Timing in which the characteristic is determined.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Human readable description
    :param Annotation note: Used for footnotes or explanatory notes
    :param CodeableConcept eventCodeableConcept: The event used as a base point (reference point) in time
    :param Reference eventReference: The event used as a base point (reference point) in time
    :param str eventDateTime: The event used as a base point (reference point) in time
    :param str eventId: The event used as a base point (reference point) in time
    :param Quantity quantity: Used to express the observation at a defined amount of time before or after the event
    :param Range range: Used to express the observation within a period before and/or after the event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "eventCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "eventReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "range": {"class_name": "Range", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  eventCodeableConcept:  'CodeableConcept'  = None,  eventReference:  'Reference'  = None,  eventDateTime:  'str'  = None,  eventId:  'str'  = None,  quantity:  'Quantity'  = None,  range:  'Range'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.note = note or []
        self.eventCodeableConcept = eventCodeableConcept 
        self.eventReference = eventReference 
        self.eventDateTime = eventDateTime 
        self.eventId = eventId 
        self.quantity = quantity 
        self.range = range 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Characteristic(BaseModel):
    """ A defining factor of the EvidenceVariable. Multiple characteristics are applied with "and" semantics.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Label for internal linking
    :param str description: Natural language description of the characteristic
    :param Annotation note: Used for footnotes or explanatory notes
    :param bool exclude: Whether the characteristic is an inclusion criterion or exclusion criterion
    :param Reference definitionReference: Defines the characteristic (without using type and value) by a Reference
    :param str definitionCanonical: Defines the characteristic (without using type and value) by a Canonical
    :param CodeableConcept definitionCodeableConcept: Defines the characteristic (without using type and value) by a CodeableConcept
    :param Expression definitionExpression: Defines the characteristic (without using type and value) by an expression
    :param str definitionId: Defines the characteristic (without using type and value) by an id
    :param DefinitionByTypeAndValue definitionByTypeAndValue: Defines the characteristic using type and value
    :param DefinitionByCombination definitionByCombination: Used to specify how two or more characteristics are combined
    :param Quantity instancesQuantity: Number of occurrences meeting the characteristic
    :param Range instancesRange: Number of occurrences meeting the characteristic
    :param Quantity durationQuantity: Length of time in which the characteristic is met
    :param Range durationRange: Length of time in which the characteristic is met
    :param TimeFromEvent timeFromEvent: Timing in which the characteristic is determined
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        
        "definitionReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "definitionCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "definitionExpression": {"class_name": "Expression", "is_contained": False},
        
        
        
        "definitionByTypeAndValue": {"class_name": "DefinitionByTypeAndValue", "is_contained": True},
        
        
        "definitionByCombination": {"class_name": "DefinitionByCombination", "is_contained": True},
        
        
        "instancesQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "instancesRange": {"class_name": "Range", "is_contained": False},
        
        
        "durationQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "durationRange": {"class_name": "Range", "is_contained": False},
        
        
        "timeFromEvent": {"class_name": "TimeFromEvent", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  exclude:  'bool'  = None,  definitionReference:  'Reference'  = None,  definitionCanonical:  'str'  = None,  definitionCodeableConcept:  'CodeableConcept'  = None,  definitionExpression:  'Expression'  = None,  definitionId:  'str'  = None,  definitionByTypeAndValue:  'DefinitionByTypeAndValue'  = None,  definitionByCombination:  'DefinitionByCombination'  = None,  instancesQuantity:  'Quantity'  = None,  instancesRange:  'Range'  = None,  durationQuantity:  'Quantity'  = None,  durationRange:  'Range'  = None,  timeFromEvent:  list['TimeFromEvent']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.description = description 
        self.note = note or []
        self.exclude = exclude 
        self.definitionReference = definitionReference 
        self.definitionCanonical = definitionCanonical 
        self.definitionCodeableConcept = definitionCodeableConcept 
        self.definitionExpression = definitionExpression 
        self.definitionId = definitionId 
        self.definitionByTypeAndValue = definitionByTypeAndValue 
        self.definitionByCombination = definitionByCombination 
        self.instancesQuantity = instancesQuantity 
        self.instancesRange = instancesRange 
        self.durationQuantity = durationQuantity 
        self.durationRange = durationRange 
        self.timeFromEvent = timeFromEvent or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Category(BaseModel):
    """ A grouping for ordinal or polychotomous variables.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Description of the grouping
    :param CodeableConcept valueCodeableConcept: Definition of the grouping
    :param Quantity valueQuantity: Definition of the grouping
    :param Range valueRange: Definition of the grouping
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class EvidenceVariable(DomainResource):
    """ The EvidenceVariable resource describes an element that knowledge (Evidence) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence variable, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the evidence variable
    :param str version: Business version of the evidence variable
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this evidence variable (computer friendly)
    :param str title: Name for this evidence variable (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the evidence variable
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param str purpose: Why this EvidenceVariable is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the resource was approved by publisher
    :param str lastReviewDate: When the resource was last reviewed by the publisher
    :param Period effectivePeriod: When the resource is expected to be used
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param bool actual: Actual or conceptual
    :param Characteristic characteristic: A defining factor of the EvidenceVariable
    :param str handling: continuous | dichotomous | ordinal | polychotomous
    :param Category category: A grouping for ordinal or polychotomous variables
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
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        
        
        "category": {"class_name": "Category", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  shortTitle:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  useContext:  list['UsageContext']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  actual:  'bool'  = None,  characteristic:  list['Characteristic']  = None,  handling:  'str'  = None,  category:  list['Category']  = None, ):
        self.resourceType = resourceType or "EvidenceVariable"
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
        self.shortTitle = shortTitle 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.note = note or []
        self.useContext = useContext or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        self.actual = actual 
        self.characteristic = characteristic or []
        self.handling = handling 
        self.category = category or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()