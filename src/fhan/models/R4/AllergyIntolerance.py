"""
Generated class for AllergyIntolerance. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Range import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Age import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Reaction(Element):
    """ Details about each adverse reaction event linked to exposure to the identified substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: Specific substance or pharmaceutical product considered to be responsible for event
    :param CodeableConcept manifestation: Clinical symptoms/signs associated with the Event
    :param str description: Description of the event as a whole
    :param str onset: Date(/time) when manifestations showed
    :param str severity: mild | moderate | severe (of event as a whole)
    :param CodeableConcept exposureRoute: How the subject was exposed to the substance
    :param Annotation note: Text about event not captured in other fields
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    substance: "CodeableConcept" = None
    manifestation: list[CodeableConcept] = None
    
    description: str = None
    
    onset: str = None
    
    severity: str = None
    exposureRoute: "CodeableConcept" = None
    note: list[Annotation] = None
    
@dataclass
class AllergyIntolerance(ModelBase):
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
    :param CodeableConcept verificationStatus: unconfirmed | confirmed | refuted | entered-in-error
    :param str type: allergy | intolerance - Underlying mechanism (if known)
    :param str category: food | medication | environment | biologic
    :param str criticality: low | high | unable-to-assess
    :param CodeableConcept code: Code that identifies the allergy or intolerance
    :param Reference patient: Who the sensitivity is for
    :param Reference encounter: Encounter when the allergy or intolerance was asserted
    :param str onsetDateTime: When allergy or intolerance was identified
    :param str recordedDate: Date first version of the resource instance was recorded
    :param Reference recorder: Who recorded the sensitivity
    :param Reference asserter: Source of the information about the allergy
    :param str lastOccurrence: Date(/time) of last known occurrence of a reaction
    :param Annotation note: Additional text not captured in other fields
    :param Reaction reaction: Adverse Reaction Events linked to exposure to substance
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    clinicalStatus: "CodeableConcept" = None
    
    verificationStatus: "CodeableConcept" = None
    
    type: str = None
    
    category: str = None
    
    criticality: str = None
    
    code: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    onsetDateTime: str = None
    
    recordedDate: str = None
    
    recorder: "Reference" = None
    
    asserter: "Reference" = None
    
    lastOccurrence: str = None
    
    note: list["Annotation"] = None
    
    reaction: list["Reaction"] = None
    