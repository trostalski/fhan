"""
Generated class for Permission. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Justification(BaseModel):
    """ The asserted justification for using the data.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept basis: The regulatory grounds upon which this Permission builds
    :param Reference evidence: Justifing rational
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "basis": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "evidence": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  basis:  list['CodeableConcept']  = None,  evidence:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.basis = basis or []
        self.evidence = evidence or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Permission":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Permission":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class Resource(BaseModel):
    """ Explicit FHIR Resource references.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param Reference reference: The actual data reference
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  meaning:  'str'  = None,  reference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.meaning = meaning 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Permission":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Permission":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Data(BaseModel):
    """ A description or definition of which activities are allowed to be done on the data.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Resource resource: Explicit FHIR Resource references
    :param Coding security: Security tag code on .meta.security
    :param Period period: Timeframe encompasing data create/update
    :param Expression expression: Expression identifying the data
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "resource": {"class_name": "Resource", "is_contained": True},
        
        
        "security": {"class_name": "Coding", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "expression": {"class_name": "Expression", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  resource:  list['Resource']  = None,  security:  list['Coding']  = None,  period:  list['Period']  = None,  expression:  'Expression'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.resource = resource or []
        self.security = security or []
        self.period = period or []
        self.expression = expression 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Permission":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Permission":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Activity(BaseModel):
    """ A description or definition of which activities are allowed to be done on the data.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference actor: Authorized actor(s)
    :param CodeableConcept action: Actions controlled by this rule
    :param CodeableConcept purpose: The purpose for which the permission is given
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        
        "action": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "purpose": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  actor:  list['Reference']  = None,  action:  list['CodeableConcept']  = None,  purpose:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.actor = actor or []
        self.action = action or []
        self.purpose = purpose or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Permission":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Permission":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Rule(BaseModel):
    """ A set of rules.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: deny | permit
    :param Data data: The selection criteria to identify data that is within scope of this provision
    :param Activity activity: A description or definition of which activities are allowed to be done on the data
    :param CodeableConcept limit: What limits apply to the use of the data
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "data": {"class_name": "Data", "is_contained": True},
        
        
        "activity": {"class_name": "Activity", "is_contained": True},
        
        
        "limit": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  data:  list['Data']  = None,  activity:  list['Activity']  = None,  limit:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.data = data or []
        self.activity = activity or []
        self.limit = limit or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Permission":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Permission":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Permission(DomainResource):
    """ Permission resource holds access rules for a given data and context.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str status: active | entered-in-error | draft | rejected
    :param Reference asserter: The person or entity that asserts the permission
    :param str date: The date that permission was asserted
    :param Period validity: The period in which the permission is active
    :param Justification justification: The asserted justification for using the data
    :param str combining: deny-overrides | permit-overrides | ordered-deny-overrides | ordered-permit-overrides | deny-unless-permit | permit-unless-deny
    :param Rule rule: Constraints to the Permission
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "asserter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "validity": {"class_name": "Period", "is_contained": False},
        
        
        "justification": {"class_name": "Justification", "is_contained": True},
        
        
        
        "rule": {"class_name": "Rule", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  status:  'str'  = None,  asserter:  'Reference'  = None,  date:  list['str']  = None,  validity:  'Period'  = None,  justification:  'Justification'  = None,  combining:  'str'  = None,  rule:  list['Rule']  = None, ):
        self.resourceType = resourceType or "Permission"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status 
        self.asserter = asserter 
        self.date = date or []
        self.validity = validity 
        self.justification = justification 
        self.combining = combining 
        self.rule = rule or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Permission":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Permission":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()