"""
Generated class for AllergyIntolerance. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Age import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Reaction(ModelBase):
    """ Details about each adverse reaction event linked to exposure to the identified substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' substance: Specific substance or pharmaceutical product considered to be responsible for event
    :param list['CodeableConcept'] manifestation: Clinical symptoms/signs associated with the Event
    :param str description: Description of the event as a whole
    :param str onset: Date(/time) when manifestations showed
    :param str severity: mild | moderate | severe (of event as a whole)
    :param 'CodeableConcept' exposureRoute: How the subject was exposed to the substance
    :param list['Annotation'] note: Text about event not captured in other fields
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  substance: 'CodeableConcept' = None,  manifestation: list['CodeableConcept'] = None,  description: str = None,  onset: str = None,  severity: str = None,  exposureRoute: 'CodeableConcept' = None,  note: list['Annotation'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.substance: 'CodeableConcept' = substance 
        self.manifestation: list['CodeableConcept'] = manifestation or []
        self.description: str = description 
        self.onset: str = onset 
        self.severity: str = severity 
        self.exposureRoute: 'CodeableConcept' = exposureRoute 
        self.note: list['Annotation'] = note or []
        

class AllergyIntolerance(DomainResource):
    """ Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External ids for this item
    :param 'CodeableConcept' clinicalStatus: active | inactive | resolved
    :param 'CodeableConcept' verificationStatus: unconfirmed | confirmed | refuted | entered-in-error
    :param str type: allergy | intolerance - Underlying mechanism (if known)
    :param str category: food | medication | environment | biologic
    :param str criticality: low | high | unable-to-assess
    :param 'CodeableConcept' code: Code that identifies the allergy or intolerance
    :param 'Reference' patient: Who the sensitivity is for
    :param 'Reference' encounter: Encounter when the allergy or intolerance was asserted
    :param str onsetDateTime: When allergy or intolerance was identified
    :param str recordedDate: Date first version of the resource instance was recorded
    :param 'Reference' recorder: Who recorded the sensitivity
    :param 'Reference' asserter: Source of the information about the allergy
    :param str lastOccurrence: Date(/time) of last known occurrence of a reaction
    :param list['Annotation'] note: Additional text not captured in other fields
    :param list['Reaction'] reaction: Adverse Reaction Events linked to exposure to substance
    """
    def __init__(self, resourceType: str = "AllergyIntolerance",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  clinicalStatus: 'CodeableConcept' = None,  verificationStatus: 'CodeableConcept' = None,  type: str = None,  category: str = None,  criticality: str = None,  code: 'CodeableConcept' = None,  patient: 'Reference' = None,  encounter: 'Reference' = None,  onsetDateTime: str = None,  recordedDate: str = None,  recorder: 'Reference' = None,  asserter: 'Reference' = None,  lastOccurrence: str = None,  note: list['Annotation'] = None,  reaction: list['Reaction'] = None, ):
        self.resourceType: str = resourceType or "AllergyIntolerance"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.clinicalStatus: 'CodeableConcept' = clinicalStatus 
        self.verificationStatus: 'CodeableConcept' = verificationStatus 
        self.type: str = type 
        self.category: str = category or []
        self.criticality: str = criticality 
        self.code: 'CodeableConcept' = code 
        self.patient: 'Reference' = patient 
        self.encounter: 'Reference' = encounter 
        self.onsetDateTime: str = onsetDateTime 
        self.recordedDate: str = recordedDate 
        self.recorder: 'Reference' = recorder 
        self.asserter: 'Reference' = asserter 
        self.lastOccurrence: str = lastOccurrence 
        self.note: list['Annotation'] = note or []
        self.reaction: list['Reaction'] = reaction or []
        