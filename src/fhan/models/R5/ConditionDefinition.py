"""
Generated class for ConditionDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
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


    
    

class Observation(BaseModel):
    """ Observations particularly relevant to this condition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Category that is relevant
    :param CodeableConcept code: Code for relevant Observation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  'CodeableConcept'  = None,  code:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category 
        self.code = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConditionDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConditionDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Medication(BaseModel):
    """ Medications particularly relevant for this condition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Category that is relevant
    :param CodeableConcept code: Code for relevant Medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  'CodeableConcept'  = None,  code:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category 
        self.code = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConditionDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConditionDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Precondition(BaseModel):
    """ An observation that suggests that this condition applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: sensitive | specific
    :param CodeableConcept code: Code for relevant Observation
    :param CodeableConcept valueCodeableConcept: Value of Observation
    :param Quantity valueQuantity: Value of Observation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  code:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.code = code 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConditionDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConditionDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Questionnaire(BaseModel):
    """ Questionnaire for this condition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str purpose: preadmit | diff-diagnosis | outcome
    :param Reference reference: Specific Questionnaire
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  purpose:  'str'  = None,  reference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.purpose = purpose 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConditionDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConditionDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Plan(BaseModel):
    """ Plan that is appropriate.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Use for the plan
    :param Reference reference: The actual plan
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  role:  'CodeableConcept'  = None,  reference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConditionDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConditionDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ConditionDefinition(DomainResource):
    """ A definition of a condition and information relevant to managing it.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this condition definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the condition definition
    :param str version: Business version of the condition definition
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this condition definition (computer friendly)
    :param str title: Name for this condition definition (human friendly)
    :param str subtitle: Subordinate title of the event definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the condition definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for condition definition (if applicable)
    :param CodeableConcept code: Identification of the condition, problem or diagnosis
    :param CodeableConcept severity: Subjective severity of condition
    :param CodeableConcept bodySite: Anatomical location, if relevant
    :param CodeableConcept stage: Stage/grade, usually assessed formally
    :param bool hasSeverity: Whether Severity is appropriate
    :param bool hasBodySite: Whether bodySite is appropriate
    :param bool hasStage: Whether stage is appropriate
    :param str definition: Formal Definition for the condition
    :param Observation observation: Observations particularly relevant to this condition
    :param Medication medication: Medications particularly relevant for this condition
    :param Precondition precondition: Observation that suggets this condition
    :param Reference team: Appropriate team for this condition
    :param Questionnaire questionnaire: Questionnaire for this condition
    :param Plan plan: Plan that is appropriate
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
        
        
        "severity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "stage": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        "observation": {"class_name": "Observation", "is_contained": True},
        
        
        "medication": {"class_name": "Medication", "is_contained": True},
        
        
        "precondition": {"class_name": "Precondition", "is_contained": True},
        
        
        "team": {"class_name": "Reference", "is_contained": False},
        
        
        "questionnaire": {"class_name": "Questionnaire", "is_contained": True},
        
        
        "plan": {"class_name": "Plan", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  subtitle:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  severity:  'CodeableConcept'  = None,  bodySite:  'CodeableConcept'  = None,  stage:  'CodeableConcept'  = None,  hasSeverity:  'bool'  = None,  hasBodySite:  'bool'  = None,  hasStage:  'bool'  = None,  definition:  list['str']  = None,  observation:  list['Observation']  = None,  medication:  list['Medication']  = None,  precondition:  list['Precondition']  = None,  team:  list['Reference']  = None,  questionnaire:  list['Questionnaire']  = None,  plan:  list['Plan']  = None, ):
        self.resourceType = resourceType or "ConditionDefinition"
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
        self.subtitle = subtitle 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.code = code 
        self.severity = severity 
        self.bodySite = bodySite 
        self.stage = stage 
        self.hasSeverity = hasSeverity 
        self.hasBodySite = hasBodySite 
        self.hasStage = hasStage 
        self.definition = definition or []
        self.observation = observation or []
        self.medication = medication or []
        self.precondition = precondition or []
        self.team = team or []
        self.questionnaire = questionnaire or []
        self.plan = plan or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConditionDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConditionDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()