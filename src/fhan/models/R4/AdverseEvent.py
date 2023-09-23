"""
Generated class for AdverseEvent. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Causality(Element):
    """ Information on the possible cause of the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept assessment: Assessment of if the entity caused the event
    :param str productRelatedness: AdverseEvent.suspectEntity.causalityProductRelatedness
    :param Reference author: AdverseEvent.suspectEntity.causalityAuthor
    :param CodeableConcept method: ProbabilityScale | Bayesian | Checklist
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    assessment: "CodeableConcept" = CodeableConcept()
    
    productRelatedness: str = None
    author: "Reference" = Reference()
    method: "CodeableConcept" = CodeableConcept()
    

  
    
    
@dataclass
class SuspectEntity(Element):
    """ Describes the entity that is suspected to have caused the adverse event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference instance: Refers to the specific entity that caused the adverse event
    :param Causality causality: Information on the possible cause of the event
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    instance: "Reference" = Reference()
    causality: list[Causality] = Causality() 
    

@dataclass
class AdverseEvent(ModelBase):
    """ Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the event
    :param str actuality: actual | potential
    :param CodeableConcept category: product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment
    :param CodeableConcept event: Type of the event itself in relation to the subject
    :param Reference subject: Subject impacted by event
    :param Reference encounter: Encounter created as part of
    :param str date: When the event occurred
    :param str detected: When the event was detected
    :param str recordedDate: When the event was recorded
    :param Reference resultingCondition: Effect on the subject due to this event
    :param Reference location: Location where adverse event occurred
    :param CodeableConcept seriousness: Seriousness of the event
    :param CodeableConcept severity: mild | moderate | severe
    :param CodeableConcept outcome: resolved | recovering | ongoing | resolvedWithSequelae | fatal | unknown
    :param Reference recorder: Who recorded the adverse event
    :param Reference contributor: Who  was involved in the adverse event or the potential adverse event
    :param SuspectEntity suspectEntity: The suspected agent causing the adverse event
    :param Reference subjectMedicalHistory: AdverseEvent.subjectMedicalHistory
    :param Reference referenceDocument: AdverseEvent.referenceDocument
    :param Reference study: AdverseEvent.study
    """

    resourceType: str = "AdverseEvent"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: "Identifier" = Identifier()
    
    actuality: str = None
    
    category: list[CodeableConcept] = CodeableConcept() 
    
    event: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    date: str = None
    
    detected: str = None
    
    recordedDate: str = None
    
    resultingCondition: list[Reference] = Reference() 
    
    location: "Reference" = Reference()
    
    seriousness: "CodeableConcept" = CodeableConcept()
    
    severity: "CodeableConcept" = CodeableConcept()
    
    outcome: "CodeableConcept" = CodeableConcept()
    
    recorder: "Reference" = Reference()
    
    contributor: list[Reference] = Reference() 
    
    suspectEntity: list[SuspectEntity] = SuspectEntity() 
    
    subjectMedicalHistory: list[Reference] = Reference() 
    
    referenceDocument: list[Reference] = Reference() 
    
    study: list[Reference] = Reference() 
    