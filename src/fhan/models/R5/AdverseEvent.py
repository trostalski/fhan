"""
Generated class for AdverseEvent. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class AdverseEvent:
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
    :param str occurrencedateTime: When the event occurred
    :param Period occurrencedateTime: When the event occurred
    :param Timing occurrencedateTime: When the event occurred
    :param str detected: When the event was detected
    :param str recordedDate: When the event was recorded
    :param Reference resultingEffect: Effect on the subject due to this event
    :param Reference location: Location where adverse event occurred
    :param CodeableConcept seriousness: Seriousness or gravity of the event
    :param CodeableConcept outcome: Type of outcome from the adverse event
    :param Reference recorder: Who recorded the adverse event
    :param BackboneElement participant: Who was involved in the adverse event or the potential adverse event and what they did
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who was involved in the adverse event or the potential adverse event
    :param Reference study: Research study that the subject is enrolled in
    :param bool expectedInResearchStudy: Considered likely or probable or anticipated in the research study
    :param BackboneElement suspectEntity: The suspected agent causing the adverse event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept instanceCodeableConcept: Refers to the specific entity that caused the adverse event
    :param Reference instanceCodeableConcept: Refers to the specific entity that caused the adverse event
    :param BackboneElement causality: Information on the possible cause of the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept assessmentMethod: Method of evaluating the relatedness of the suspected entity to the event
    :param CodeableConcept entityRelatedness: Result of the assessment regarding the relatedness of the suspected entity to the event
    :param Reference author: Author of the information on the possible cause of the event
    :param BackboneElement contributingFactor: Contributing factors suspected to have increased the probability or severity of the adverse event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Item suspected to have increased the probability or severity of the adverse event
    :param CodeableConcept itemReference: Item suspected to have increased the probability or severity of the adverse event
    :param BackboneElement preventiveAction: Preventive actions that contributed to avoiding the adverse event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Action that contributed to avoiding the adverse event
    :param CodeableConcept itemReference: Action that contributed to avoiding the adverse event
    :param BackboneElement mitigatingAction: Ameliorating actions taken after the adverse event occured in order to reduce the extent of harm
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Ameliorating action taken after the adverse event occured in order to reduce the extent of harm
    :param CodeableConcept itemReference: Ameliorating action taken after the adverse event occured in order to reduce the extent of harm
    :param BackboneElement supportingInfo: Supporting information relevant to the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: Subject medical history or document relevant to this adverse event
    :param CodeableConcept itemReference: Subject medical history or document relevant to this adverse event
    :param Annotation note: Comment on adverse event
    
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
    
    status: str = None
    
    actuality: str = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    detected: str = None
    
    recordedDate: str = None
    
    resultingEffect: "Reference" = None
    
    location: "Reference" = None
    
    seriousness: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    recorder: "Reference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    study: "Reference" = None
    
    expectedInResearchStudy: bool = None
    
    suspectEntity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    instanceCodeableConcept: "CodeableConcept" = None
    
    instanceCodeableConcept: "Reference" = None
    
    causality: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    assessmentMethod: "CodeableConcept" = None
    
    entityRelatedness: "CodeableConcept" = None
    
    author: "Reference" = None
    
    contributingFactor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    preventiveAction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    mitigatingAction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    supportingInfo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    note: "Annotation" = None
    