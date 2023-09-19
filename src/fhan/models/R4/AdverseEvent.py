"""
Generated class for AdverseEvent. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement suspectEntity: The suspected agent causing the adverse event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference instance: Refers to the specific entity that caused the adverse event
    :param BackboneElement causality: Information on the possible cause of the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept assessment: Assessment of if the entity caused the event
    :param str productRelatedness: AdverseEvent.suspectEntity.causalityProductRelatedness
    :param Reference author: AdverseEvent.suspectEntity.causalityAuthor
    :param CodeableConcept method: ProbabilityScale | Bayesian | Checklist
    :param Reference subjectMedicalHistory: AdverseEvent.subjectMedicalHistory
    :param Reference referenceDocument: AdverseEvent.referenceDocument
    :param Reference study: AdverseEvent.study
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    actuality: str = None
    
    category: "CodeableConcept" = None
    
    event: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    detected: str = None
    
    recordedDate: str = None
    
    resultingCondition: "Reference" = None
    
    location: "Reference" = None
    
    seriousness: "CodeableConcept" = None
    
    severity: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    recorder: "Reference" = None
    
    contributor: "Reference" = None
    
    suspectEntity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    instance: "Reference" = None
    
    causality: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    assessment: "CodeableConcept" = None
    
    productRelatedness: str = None
    
    author: "Reference" = None
    
    method: "CodeableConcept" = None
    
    subjectMedicalHistory: "Reference" = None
    
    referenceDocument: "Reference" = None
    
    study: "Reference" = None
    