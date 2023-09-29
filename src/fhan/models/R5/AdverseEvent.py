"""
Generated class for AdverseEvent. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Participant(BaseModel):
    """ Indicates who or what participated in the adverse event and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who was involved in the adverse event or the potential adverse event
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
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Causality(BaseModel):
    """ Information on the possible cause of the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept assessmentMethod: Method of evaluating the relatedness of the suspected entity to the event
    :param CodeableConcept entityRelatedness: Result of the assessment regarding the relatedness of the suspected entity to the event
    :param Reference author: Author of the information on the possible cause of the event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "assessmentMethod": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "entityRelatedness": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  assessmentMethod:  'CodeableConcept'  = None,  entityRelatedness:  'CodeableConcept'  = None,  author:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.assessmentMethod = assessmentMethod 
        self.entityRelatedness = entityRelatedness 
        self.author = author 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class SuspectEntity(BaseModel):
    """ Describes the entity that is suspected to have caused the adverse event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept instanceCodeableConcept: Refers to the specific entity that caused the adverse event
    :param Reference instanceReference: Refers to the specific entity that caused the adverse event
    :param Causality causality: Information on the possible cause of the event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "instanceCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "instanceReference": {"class_name": "Reference", "is_contained": False},
        
        
        "causality": {"class_name": "Causality", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  instanceCodeableConcept:  'CodeableConcept'  = None,  instanceReference:  'Reference'  = None,  causality:  'Causality'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.instanceCodeableConcept = instanceCodeableConcept 
        self.instanceReference = instanceReference 
        self.causality = causality 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ContributingFactor(BaseModel):
    """ The contributing factors suspected to have increased the probability or severity of the adverse event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Item suspected to have increased the probability or severity of the adverse event
    :param CodeableConcept itemCodeableConcept: Item suspected to have increased the probability or severity of the adverse event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "itemReference": {"class_name": "Reference", "is_contained": False},
        
        
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  itemReference:  'Reference'  = None,  itemCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemReference = itemReference 
        self.itemCodeableConcept = itemCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class PreventiveAction(BaseModel):
    """ Preventive actions that contributed to avoiding the adverse event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Action that contributed to avoiding the adverse event
    :param CodeableConcept itemCodeableConcept: Action that contributed to avoiding the adverse event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "itemReference": {"class_name": "Reference", "is_contained": False},
        
        
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  itemReference:  'Reference'  = None,  itemCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemReference = itemReference 
        self.itemCodeableConcept = itemCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class MitigatingAction(BaseModel):
    """ The ameliorating action taken after the adverse event occured in order to reduce the extent of harm.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Ameliorating action taken after the adverse event occured in order to reduce the extent of harm
    :param CodeableConcept itemCodeableConcept: Ameliorating action taken after the adverse event occured in order to reduce the extent of harm
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "itemReference": {"class_name": "Reference", "is_contained": False},
        
        
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  itemReference:  'Reference'  = None,  itemCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemReference = itemReference 
        self.itemCodeableConcept = itemCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class SupportingInfo(BaseModel):
    """ Supporting information relevant to the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Subject medical history or document relevant to this adverse event
    :param CodeableConcept itemCodeableConcept: Subject medical history or document relevant to this adverse event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "itemReference": {"class_name": "Reference", "is_contained": False},
        
        
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  itemReference:  'Reference'  = None,  itemCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemReference = itemReference 
        self.itemCodeableConcept = itemCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AdverseEvent(DomainResource):
    """ An event (i.e. any change to current patient status) that may be related to unintended effects on a patient or research participant. The unintended effects may require additional monitoring, treatment, hospitalization, or may result in death. The AdverseEvent resource also extends to potential or avoided events that could have had such effects. There are two major domains where the AdverseEvent resource is expected to be used. One is in clinical care reported adverse events and the other is in reporting adverse events in clinical  research trial management.  Adverse events can be reported by healthcare providers, patients, caregivers or by medical products manufacturers.  Given the differences between these two concepts, we recommend consulting the domain specific implementation guides when implementing the AdverseEvent Resource. The implementation guides include specific extensions, value sets and constraints.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the event
    :param str status: in-progress | completed | entered-in-error | unknown
    :param str actuality: actual | potential
    :param CodeableConcept category: wrong-patient | procedure-mishap | medication-mishap | device | unsafe-physical-environment | hospital-aquired-infection | wrong-body-site
    :param CodeableConcept code: Event or incident that occurred or was averted
    :param Reference subject: Subject impacted by event
    :param Reference encounter: The Encounter associated with the start of the AdverseEvent
    :param str occurrenceDateTime: When the event occurred
    :param Period occurrencePeriod: When the event occurred
    :param Timing occurrenceTiming: When the event occurred
    :param str detected: When the event was detected
    :param str recordedDate: When the event was recorded
    :param Reference resultingEffect: Effect on the subject due to this event
    :param Reference location: Location where adverse event occurred
    :param CodeableConcept seriousness: Seriousness or gravity of the event
    :param CodeableConcept outcome: Type of outcome from the adverse event
    :param Reference recorder: Who recorded the adverse event
    :param Participant participant: Who was involved in the adverse event or the potential adverse event and what they did
    :param Reference study: Research study that the subject is enrolled in
    :param bool expectedInResearchStudy: Considered likely or probable or anticipated in the research study
    :param SuspectEntity suspectEntity: The suspected agent causing the adverse event
    :param ContributingFactor contributingFactor: Contributing factors suspected to have increased the probability or severity of the adverse event
    :param PreventiveAction preventiveAction: Preventive actions that contributed to avoiding the adverse event
    :param MitigatingAction mitigatingAction: Ameliorating actions taken after the adverse event occured in order to reduce the extent of harm
    :param SupportingInfo supportingInfo: Supporting information relevant to the event
    :param Annotation note: Comment on adverse event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        
        "resultingEffect": {"class_name": "Reference", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "seriousness": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "recorder": {"class_name": "Reference", "is_contained": False},
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        "study": {"class_name": "Reference", "is_contained": False},
        
        
        
        "suspectEntity": {"class_name": "SuspectEntity", "is_contained": True},
        
        
        "contributingFactor": {"class_name": "ContributingFactor", "is_contained": True},
        
        
        "preventiveAction": {"class_name": "PreventiveAction", "is_contained": True},
        
        
        "mitigatingAction": {"class_name": "MitigatingAction", "is_contained": True},
        
        
        "supportingInfo": {"class_name": "SupportingInfo", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  actuality:  'str'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceTiming:  'Timing'  = None,  detected:  'str'  = None,  recordedDate:  'str'  = None,  resultingEffect:  list['Reference']  = None,  location:  'Reference'  = None,  seriousness:  'CodeableConcept'  = None,  outcome:  list['CodeableConcept']  = None,  recorder:  'Reference'  = None,  participant:  list['Participant']  = None,  study:  list['Reference']  = None,  expectedInResearchStudy:  'bool'  = None,  suspectEntity:  list['SuspectEntity']  = None,  contributingFactor:  list['ContributingFactor']  = None,  preventiveAction:  list['PreventiveAction']  = None,  mitigatingAction:  list['MitigatingAction']  = None,  supportingInfo:  list['SupportingInfo']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "AdverseEvent"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.actuality = actuality 
        self.category = category or []
        self.code = code 
        self.subject = subject 
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceTiming = occurrenceTiming 
        self.detected = detected 
        self.recordedDate = recordedDate 
        self.resultingEffect = resultingEffect or []
        self.location = location 
        self.seriousness = seriousness 
        self.outcome = outcome or []
        self.recorder = recorder 
        self.participant = participant or []
        self.study = study or []
        self.expectedInResearchStudy = expectedInResearchStudy 
        self.suspectEntity = suspectEntity or []
        self.contributingFactor = contributingFactor or []
        self.preventiveAction = preventiveAction or []
        self.mitigatingAction = mitigatingAction or []
        self.supportingInfo = supportingInfo or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()