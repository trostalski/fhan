"""
Generated class for Requirements. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Statement(BaseModel):
    """ The actual statement of requirement, in markdown format.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: Key that identifies this statement
    :param str label: Short Human label for this statement
    :param str conformance: SHALL | SHOULD | MAY | SHOULD-NOT
    :param bool conditionality: Set to true if requirements statement is conditional
    :param str requirement: The actual requirement
    :param str derivedFrom: Another statement this clarifies/restricts ([url#]key)
    :param str parent: A larger requirement that this requirement helps to refine and enable
    :param str satisfiedBy: Design artifact that satisfies this requirement
    :param str reference: External artifact (rule/document etc. that) created this requirement
    :param Reference source: Who asked for this statement
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  key:  'str'  = None,  label:  'str'  = None,  conformance:  list['str']  = None,  conditionality:  'bool'  = None,  requirement:  'str'  = None,  derivedFrom:  'str'  = None,  parent:  'str'  = None,  satisfiedBy:  list['str']  = None,  reference:  list['str']  = None,  source:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.key = key 
        self.label = label 
        self.conformance = conformance or []
        self.conditionality = conditionality 
        self.requirement = requirement 
        self.derivedFrom = derivedFrom 
        self.parent = parent 
        self.satisfiedBy = satisfiedBy or []
        self.reference = reference or []
        self.source = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Requirements":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Requirements":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Requirements(DomainResource):
    """ The Requirements resource is used to describe an actor - a human or an application that plays a role in data exchange, and that may have obligations associated with the role the actor plays.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this Requirements, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the Requirements (business identifier)
    :param str version: Business version of the Requirements
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this Requirements (computer friendly)
    :param str title: Name for this Requirements (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the requirements
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for Requirements (if applicable)
    :param str purpose: Why this Requirements is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str derivedFrom: Other set of Requirements this builds on
    :param str reference: External artifact (rule/document etc. that) created this set of requirements
    :param str actor: Actor for these requirements
    :param Statement statement: Actual statement as markdown
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
        
        
        
        
        
        
        
        
        "statement": {"class_name": "Statement", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  derivedFrom:  list['str']  = None,  reference:  list['str']  = None,  actor:  list['str']  = None,  statement:  list['Statement']  = None, ):
        self.resourceType = resourceType or "Requirements"
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
        self.derivedFrom = derivedFrom or []
        self.reference = reference or []
        self.actor = actor or []
        self.statement = statement or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Requirements":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Requirements":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()