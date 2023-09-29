"""
Generated class for EvidenceReport. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Characteristic(BaseModel):
    """ Characteristic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Characteristic code
    :param Reference valueReference: Characteristic value
    :param CodeableConcept valueCodeableConcept: Characteristic value
    :param bool valueBoolean: Characteristic value
    :param Quantity valueQuantity: Characteristic value
    :param Range valueRange: Characteristic value
    :param bool exclude: Is used to express not the characteristic
    :param Period period: Timeframe for the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  valueReference:  'Reference'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueBoolean:  'bool'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  exclude:  'bool'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueReference = valueReference 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueBoolean = valueBoolean 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.exclude = exclude 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Subject(BaseModel):
    """ Specifies the subject or focus of the report. Answers "What is this report about?".:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Characteristic characteristic: Characteristic
    :param Annotation note: Footnotes and/or explanatory notes
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  characteristic:  list['Characteristic']  = None,  note:  list['Annotation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.characteristic = characteristic or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Target(BaseModel):
    """ The target composition/document of this relationship.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Target of the relationship URL
    :param Identifier identifier: Target of the relationship Identifier
    :param str display: Target of the relationship Display
    :param Reference resource: Target of the relationship Resource reference
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "resource": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  'Identifier'  = None,  display:  'str'  = None,  resource:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier 
        self.display = display 
        self.resource = resource 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class RelatesTo(BaseModel):
    """ Relationships that this composition has with other compositions or documents that already exist.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | amends | appends | transforms | replacedWith | amendedWith | appendedWith | transformedWith
    :param Target target: Target of the relationship
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "target": {"class_name": "Target", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  target:  'Target'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.target = target 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Section(BaseModel):
    """ The root of the sections that make up the composition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param CodeableConcept focus: Classification of section (recommended)
    :param Reference focusReference: Classification of section by Resource
    :param Reference author: Who and/or what authored the section
    :param Narrative text: Text summary of the section, for human interpretation
    :param str mode: working | snapshot | changes
    :param CodeableConcept orderedBy: Order of section entries
    :param CodeableConcept entryClassifier: Extensible classifiers as content
    :param Reference entryReference: Reference to resources as content
    :param Quantity entryQuantity: Quantity as content
    :param CodeableConcept emptyReason: Why the section is empty
    :param Section section: Nested Section
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "focus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "focusReference": {"class_name": "Reference", "is_contained": False},
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        
        "orderedBy": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "entryClassifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "entryReference": {"class_name": "Reference", "is_contained": False},
        
        
        "entryQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "emptyReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "section": {"class_name": "Section", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  focus:  'CodeableConcept'  = None,  focusReference:  'Reference'  = None,  author:  list['Reference']  = None,  text:  'Narrative'  = None,  mode:  'str'  = None,  orderedBy:  'CodeableConcept'  = None,  entryClassifier:  list['CodeableConcept']  = None,  entryReference:  list['Reference']  = None,  entryQuantity:  list['Quantity']  = None,  emptyReason:  'CodeableConcept'  = None,  section:  list['Section']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.focus = focus 
        self.focusReference = focusReference 
        self.author = author or []
        self.text = text 
        self.mode = mode 
        self.orderedBy = orderedBy 
        self.entryClassifier = entryClassifier or []
        self.entryReference = entryReference or []
        self.entryQuantity = entryQuantity or []
        self.emptyReason = emptyReason 
        self.section = section or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class EvidenceReport(DomainResource):
    """ The EvidenceReport Resource is a specialized container for a collection of resources and codeable concepts, adapted to support compositions of Evidence, EvidenceVariable, and Citation resources and related concepts.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this EvidenceReport, represented as a globally unique URI
    :param str status: draft | active | retired | unknown
    :param UsageContext useContext: The context that the content is intended to support
    :param Identifier identifier: Unique identifier for the evidence report
    :param Identifier relatedIdentifier: Identifiers for articles that may relate to more than one evidence report
    :param Reference citeAsReference: Citation for this report
    :param str citeAsMarkdown: Citation for this report
    :param CodeableConcept type: Kind of report
    :param Annotation note: Used for footnotes and annotations
    :param RelatedArtifact relatedArtifact: Link, description or reference to artifact associated with the report
    :param Subject subject: Focus of the report
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatesTo relatesTo: Relationships to other compositions/documents
    :param Section section: Composition is broken into sections
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "relatedIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "citeAsReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "subject": {"class_name": "Subject", "is_contained": True},
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        
        
        "section": {"class_name": "Section", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  status:  'str'  = None,  useContext:  list['UsageContext']  = None,  identifier:  list['Identifier']  = None,  relatedIdentifier:  list['Identifier']  = None,  citeAsReference:  'Reference'  = None,  citeAsMarkdown:  'str'  = None,  type:  'CodeableConcept'  = None,  note:  list['Annotation']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  subject:  'Subject'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatesTo:  list['RelatesTo']  = None,  section:  list['Section']  = None, ):
        self.resourceType = resourceType or "EvidenceReport"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.status = status 
        self.useContext = useContext or []
        self.identifier = identifier or []
        self.relatedIdentifier = relatedIdentifier or []
        self.citeAsReference = citeAsReference 
        self.citeAsMarkdown = citeAsMarkdown 
        self.type = type 
        self.note = note or []
        self.relatedArtifact = relatedArtifact or []
        self.subject = subject 
        self.publisher = publisher 
        self.contact = contact or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatesTo = relatesTo or []
        self.section = section or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EvidenceReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()