"""
Generated class for FamilyMemberHistory. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Age import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Participant(BaseModel):
    """ Indicates who or what participated in the activities related to the family member history and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who or what participated in the activities related to the family member history
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "FamilyMemberHistory":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "FamilyMemberHistory":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Condition(BaseModel):
    """ The significant Conditions (or condition) that the family member had. This is a repeating section to allow a system to represent more than one condition per resource, though there is nothing stopping multiple resources - one per condition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Condition suffered by relation
    :param CodeableConcept outcome: deceased | permanent disability | etc
    :param bool contributedToDeath: Whether the condition contributed to the cause of death
    :param Age onsetAge: When condition first manifested
    :param Range onsetRange: When condition first manifested
    :param Period onsetPeriod: When condition first manifested
    :param str onsetString: When condition first manifested
    :param Annotation note: Extra information about condition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "onsetAge": {"class_name": "Age", "is_contained": False},
        
        
        "onsetRange": {"class_name": "Range", "is_contained": False},
        
        
        "onsetPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  outcome:  'CodeableConcept'  = None,  contributedToDeath:  'bool'  = None,  onsetAge:  'Age'  = None,  onsetRange:  'Range'  = None,  onsetPeriod:  'Period'  = None,  onsetString:  'str'  = None,  note:  list['Annotation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.outcome = outcome 
        self.contributedToDeath = contributedToDeath 
        self.onsetAge = onsetAge 
        self.onsetRange = onsetRange 
        self.onsetPeriod = onsetPeriod 
        self.onsetString = onsetString 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "FamilyMemberHistory":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "FamilyMemberHistory":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Procedure(BaseModel):
    """ The significant Procedures (or procedure) that the family member had. This is a repeating section to allow a system to represent more than one procedure per resource, though there is nothing stopping multiple resources - one per procedure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Procedures performed on the related person
    :param CodeableConcept outcome: What happened following the procedure
    :param bool contributedToDeath: Whether the procedure contributed to the cause of death
    :param Age performedAge: When the procedure was performed
    :param Range performedRange: When the procedure was performed
    :param Period performedPeriod: When the procedure was performed
    :param str performedString: When the procedure was performed
    :param str performedDateTime: When the procedure was performed
    :param Annotation note: Extra information about the procedure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "performedAge": {"class_name": "Age", "is_contained": False},
        
        
        "performedRange": {"class_name": "Range", "is_contained": False},
        
        
        "performedPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  outcome:  'CodeableConcept'  = None,  contributedToDeath:  'bool'  = None,  performedAge:  'Age'  = None,  performedRange:  'Range'  = None,  performedPeriod:  'Period'  = None,  performedString:  'str'  = None,  performedDateTime:  'str'  = None,  note:  list['Annotation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.outcome = outcome 
        self.contributedToDeath = contributedToDeath 
        self.performedAge = performedAge 
        self.performedRange = performedRange 
        self.performedPeriod = performedPeriod 
        self.performedString = performedString 
        self.performedDateTime = performedDateTime 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "FamilyMemberHistory":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "FamilyMemberHistory":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class FamilyMemberHistory(DomainResource):
    """ Significant health conditions for a person related to the patient relevant in the context of care for the patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Id(s) for this record
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param str status: partial | completed | entered-in-error | health-unknown
    :param CodeableConcept dataAbsentReason: subject-unknown | withheld | unable-to-obtain | deferred
    :param Reference patient: Patient history is about
    :param str date: When history was recorded or last updated
    :param Participant participant: Who or what participated in the activities related to the family member history and how they were involved
    :param str name: The family member described
    :param CodeableConcept relationship: Relationship to the subject
    :param CodeableConcept sex: male | female | other | unknown
    :param Period bornPeriod: (approximate) date of birth
    :param str bornDate: (approximate) date of birth
    :param str bornString: (approximate) date of birth
    :param Age ageAge: (approximate) age
    :param Range ageRange: (approximate) age
    :param str ageString: (approximate) age
    :param bool estimatedAge: Age is estimated?
    :param bool deceasedBoolean: Dead? How old/when?
    :param Age deceasedAge: Dead? How old/when?
    :param Range deceasedRange: Dead? How old/when?
    :param str deceasedDate: Dead? How old/when?
    :param str deceasedString: Dead? How old/when?
    :param CodeableReference reason: Why was family member history performed?
    :param Annotation note: General note about related person
    :param Condition condition: Condition that the related person had
    :param Procedure procedure: Procedures that the related person had
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "dataAbsentReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "sex": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "bornPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "ageAge": {"class_name": "Age", "is_contained": False},
        
        
        "ageRange": {"class_name": "Range", "is_contained": False},
        
        
        
        
        
        "deceasedAge": {"class_name": "Age", "is_contained": False},
        
        
        "deceasedRange": {"class_name": "Range", "is_contained": False},
        
        
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "condition": {"class_name": "Condition", "is_contained": True},
        
        
        "procedure": {"class_name": "Procedure", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  status:  'str'  = None,  dataAbsentReason:  'CodeableConcept'  = None,  patient:  'Reference'  = None,  date:  'str'  = None,  participant:  list['Participant']  = None,  name:  'str'  = None,  relationship:  'CodeableConcept'  = None,  sex:  'CodeableConcept'  = None,  bornPeriod:  'Period'  = None,  bornDate:  'str'  = None,  bornString:  'str'  = None,  ageAge:  'Age'  = None,  ageRange:  'Range'  = None,  ageString:  'str'  = None,  estimatedAge:  'bool'  = None,  deceasedBoolean:  'bool'  = None,  deceasedAge:  'Age'  = None,  deceasedRange:  'Range'  = None,  deceasedDate:  'str'  = None,  deceasedString:  'str'  = None,  reason:  list['CodeableReference']  = None,  note:  list['Annotation']  = None,  condition:  list['Condition']  = None,  procedure:  list['Procedure']  = None, ):
        self.resourceType = resourceType or "FamilyMemberHistory"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.status = status 
        self.dataAbsentReason = dataAbsentReason 
        self.patient = patient 
        self.date = date 
        self.participant = participant or []
        self.name = name 
        self.relationship = relationship 
        self.sex = sex 
        self.bornPeriod = bornPeriod 
        self.bornDate = bornDate 
        self.bornString = bornString 
        self.ageAge = ageAge 
        self.ageRange = ageRange 
        self.ageString = ageString 
        self.estimatedAge = estimatedAge 
        self.deceasedBoolean = deceasedBoolean 
        self.deceasedAge = deceasedAge 
        self.deceasedRange = deceasedRange 
        self.deceasedDate = deceasedDate 
        self.deceasedString = deceasedString 
        self.reason = reason or []
        self.note = note or []
        self.condition = condition or []
        self.procedure = procedure or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "FamilyMemberHistory":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "FamilyMemberHistory":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()