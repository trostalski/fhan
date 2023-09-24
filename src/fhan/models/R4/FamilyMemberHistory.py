"""
Generated class for FamilyMemberHistory. 
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


    
    

class Condition(ModelBase):
    """ The significant Conditions (or condition) that the family member had. This is a repeating section to allow a system to represent more than one condition per resource, though there is nothing stopping multiple resources - one per condition.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Condition suffered by relation
    :param 'CodeableConcept' outcome: deceased | permanent disability | etc.
    :param bool contributedToDeath: Whether the condition contributed to the cause of death
    :param 'Age' onsetAge: When condition first manifested
    :param list['Annotation'] note: Extra information about condition
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  outcome: 'CodeableConcept' = None,  contributedToDeath: bool = None,  onsetAge: 'Age' = None,  note: list['Annotation'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.outcome: 'CodeableConcept' = outcome 
        self.contributedToDeath: bool = contributedToDeath 
        self.onsetAge: 'Age' = onsetAge 
        self.note: list['Annotation'] = note or []
        

class FamilyMemberHistory(DomainResource):
    """ Significant health conditions for a person related to the patient relevant in the context of care for the patient.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Id(s) for this record
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param str status: partial | completed | entered-in-error | health-unknown
    :param 'CodeableConcept' dataAbsentReason: subject-unknown | withheld | unable-to-obtain | deferred
    :param 'Reference' patient: Patient history is about
    :param str date: When history was recorded or last updated
    :param str name: The family member described
    :param 'CodeableConcept' relationship: Relationship to the subject
    :param 'CodeableConcept' sex: male | female | other | unknown
    :param 'Period' bornPeriod: (approximate) date of birth
    :param 'Age' ageAge: (approximate) age
    :param bool estimatedAge: Age is estimated?
    :param bool deceasedBoolean: Dead? How old/when?
    :param list['CodeableConcept'] reasonCode: Why was family member history performed?
    :param list['Reference'] reasonReference: Why was family member history performed?
    :param list['Annotation'] note: General note about related person
    :param list['Condition'] condition: Condition that the related person had
    """
    def __init__(self, resourceType: str = "FamilyMemberHistory",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  status: str = None,  dataAbsentReason: 'CodeableConcept' = None,  patient: 'Reference' = None,  date: str = None,  name: str = None,  relationship: 'CodeableConcept' = None,  sex: 'CodeableConcept' = None,  bornPeriod: 'Period' = None,  ageAge: 'Age' = None,  estimatedAge: bool = None,  deceasedBoolean: bool = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None,  condition: list['Condition'] = None, ):
        self.resourceType: str = resourceType or "FamilyMemberHistory"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.status: str = status 
        self.dataAbsentReason: 'CodeableConcept' = dataAbsentReason 
        self.patient: 'Reference' = patient 
        self.date: str = date 
        self.name: str = name 
        self.relationship: 'CodeableConcept' = relationship 
        self.sex: 'CodeableConcept' = sex 
        self.bornPeriod: 'Period' = bornPeriod 
        self.ageAge: 'Age' = ageAge 
        self.estimatedAge: bool = estimatedAge 
        self.deceasedBoolean: bool = deceasedBoolean 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        self.condition: list['Condition'] = condition or []
        