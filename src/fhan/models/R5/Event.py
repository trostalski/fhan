"""
Generated class for Event. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Element import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Period import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Timing import *
from fhan.models.generator_models import BaseModel

    
    

class Performer(BaseModel):
    """ Indicates who or what performed the {{title}} and how they were involved.:param CodeableConcept function: Type of performance
    :param Reference actor: Who performed {{title}}
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Event":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Event(BaseModel):
    """ Logical Model: A pattern to be followed by resources that represent the performance of some activity, possibly in accordance with a request or service definition.
    :param Identifier identifier: Business identifier for {{title}}
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param Reference researchStudy: Associated research study
    :param str status: preparation | in-progress | not-done | suspended | aborted | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: High level categorization of {{title}}
    :param CodeableConcept code: What service was done
    :param CodeableReference product: Product used/provided
    :param Reference subject: Individual service was done for/to
    :param Reference encounter: Encounter the {{title}} is part of
    :param str occurrenceDateTime: When {{title}} occurred/is occurring
    :param Period occurrencePeriod: When {{title}} occurred/is occurring
    :param Timing occurrenceTiming: When {{title}} occurred/is occurring
    :param str recorded: When {{title}} was first captured in the subject's record
    :param bool reportedBoolean: Reported rather than primary record
    :param Reference reportedReference: Reported rather than primary record
    :param Performer performer: Who performed {{title}} and what they did
    :param Reference location: Where {{title}} occurred
    :param CodeableReference reason: Why was {{title}} performed?
    :param Annotation note: Comments made about the event
    :param Reference relevantHistory: Key events in history of {{title}}
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        "researchStudy": {"class_name": "Reference", "is_contained": False},
        
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "product": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        
        "reportedReference": {"class_name": "Reference", "is_contained": False},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "relevantHistory": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  identifier:  list['Identifier']  = None,  basedOn:  list['Reference']  = None,  partOf:  list['Reference']  = None,  researchStudy:  list['Reference']  = None,  status:  'str'  = None,  statusReason:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  product:  'CodeableReference'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceTiming:  'Timing'  = None,  recorded:  'str'  = None,  reportedBoolean:  'bool'  = None,  reportedReference:  'Reference'  = None,  performer:  list['Performer']  = None,  location:  'Reference'  = None,  reason:  list['CodeableReference']  = None,  note:  list['Annotation']  = None,  relevantHistory:  list['Reference']  = None, ):
        self.resourceType = resourceType or "Event"
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.researchStudy = researchStudy or []
        self.status = status 
        self.statusReason = statusReason 
        self.category = category or []
        self.code = code 
        self.product = product 
        self.subject = subject 
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceTiming = occurrenceTiming 
        self.recorded = recorded 
        self.reportedBoolean = reportedBoolean 
        self.reportedReference = reportedReference 
        self.performer = performer or []
        self.location = location 
        self.reason = reason or []
        self.note = note or []
        self.relevantHistory = relevantHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Event":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()