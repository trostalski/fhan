"""
Generated class for AllergyIntolerance. 
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
    """ Indicates who or what participated in the activities related to the allergy or intolerance and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who or what participated in the activities related to the allergy or intolerance
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
    def from_dict(cls, data: dict) -> "AllergyIntolerance":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AllergyIntolerance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Reaction(BaseModel):
    """ Details about each adverse reaction event linked to exposure to the identified substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: Specific substance or pharmaceutical product considered to be responsible for event
    :param CodeableReference manifestation: Clinical symptoms/signs associated with the Event
    :param str description: Description of the event as a whole
    :param str onset: Date(/time) when manifestations showed
    :param str severity: mild | moderate | severe (of event as a whole)
    :param CodeableConcept exposureRoute: How the subject was exposed to the substance
    :param Annotation note: Text about event not captured in other fields
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "substance": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "manifestation": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        
        
        "exposureRoute": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  substance:  'CodeableConcept'  = None,  manifestation:  list['CodeableReference']  = None,  description:  'str'  = None,  onset:  'str'  = None,  severity:  'str'  = None,  exposureRoute:  'CodeableConcept'  = None,  note:  list['Annotation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.substance = substance 
        self.manifestation = manifestation or []
        self.description = description 
        self.onset = onset 
        self.severity = severity 
        self.exposureRoute = exposureRoute 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AllergyIntolerance":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AllergyIntolerance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AllergyIntolerance(DomainResource):
    """ Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External ids for this item
    :param CodeableConcept clinicalStatus: active | inactive | resolved
    :param CodeableConcept verificationStatus: unconfirmed | presumed | confirmed | refuted | entered-in-error
    :param CodeableConcept type: allergy | intolerance - Underlying mechanism (if known)
    :param str category: food | medication | environment | biologic
    :param str criticality: low | high | unable-to-assess
    :param CodeableConcept code: Code that identifies the allergy or intolerance
    :param Reference patient: Who the allergy or intolerance is for
    :param Reference encounter: Encounter when the allergy or intolerance was asserted
    :param str onsetDateTime: When allergy or intolerance was identified
    :param Age onsetAge: When allergy or intolerance was identified
    :param Period onsetPeriod: When allergy or intolerance was identified
    :param Range onsetRange: When allergy or intolerance was identified
    :param str onsetString: When allergy or intolerance was identified
    :param str recordedDate: Date allergy or intolerance was first recorded
    :param Participant participant: Who or what participated in the activities related to the allergy or intolerance and how they were involved
    :param str lastOccurrence: Date(/time) of last known occurrence of a reaction
    :param Annotation note: Additional text not captured in other fields
    :param Reaction reaction: Adverse Reaction Events linked to exposure to substance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "clinicalStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "verificationStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "onsetAge": {"class_name": "Age", "is_contained": False},
        
        
        "onsetPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "onsetRange": {"class_name": "Range", "is_contained": False},
        
        
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "reaction": {"class_name": "Reaction", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  clinicalStatus:  'CodeableConcept'  = None,  verificationStatus:  'CodeableConcept'  = None,  type:  'CodeableConcept'  = None,  category:  list['str']  = None,  criticality:  'str'  = None,  code:  'CodeableConcept'  = None,  patient:  'Reference'  = None,  encounter:  'Reference'  = None,  onsetDateTime:  'str'  = None,  onsetAge:  'Age'  = None,  onsetPeriod:  'Period'  = None,  onsetRange:  'Range'  = None,  onsetString:  'str'  = None,  recordedDate:  'str'  = None,  participant:  list['Participant']  = None,  lastOccurrence:  'str'  = None,  note:  list['Annotation']  = None,  reaction:  list['Reaction']  = None, ):
        self.resourceType = resourceType or "AllergyIntolerance"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.clinicalStatus = clinicalStatus 
        self.verificationStatus = verificationStatus 
        self.type = type 
        self.category = category or []
        self.criticality = criticality 
        self.code = code 
        self.patient = patient 
        self.encounter = encounter 
        self.onsetDateTime = onsetDateTime 
        self.onsetAge = onsetAge 
        self.onsetPeriod = onsetPeriod 
        self.onsetRange = onsetRange 
        self.onsetString = onsetString 
        self.recordedDate = recordedDate 
        self.participant = participant or []
        self.lastOccurrence = lastOccurrence 
        self.note = note or []
        self.reaction = reaction or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AllergyIntolerance":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AllergyIntolerance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()