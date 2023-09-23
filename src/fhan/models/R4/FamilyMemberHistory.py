"""
Generated class for FamilyMemberHistory. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Age import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Condition(Element):
    """ The significant Conditions (or condition) that the family member had. This is a repeating section to allow a system to represent more than one condition per resource, though there is nothing stopping multiple resources - one per condition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Condition suffered by relation
    :param CodeableConcept outcome: deceased | permanent disability | etc.
    :param bool contributedToDeath: Whether the condition contributed to the cause of death
    :param Age onsetAge: When condition first manifested
    :param Annotation note: Extra information about condition
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    outcome: "CodeableConcept" = CodeableConcept()
    
    contributedToDeath: bool = None
    onsetAge: "Age" = Age()
    note: list[Annotation] = Annotation() 
    

@dataclass
class FamilyMemberHistory(ModelBase):
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
    :param str name: The family member described
    :param CodeableConcept relationship: Relationship to the subject
    :param CodeableConcept sex: male | female | other | unknown
    :param Period bornPeriod: (approximate) date of birth
    :param Age ageAge: (approximate) age
    :param bool estimatedAge: Age is estimated?
    :param bool deceasedBoolean: Dead? How old/when?
    :param CodeableConcept reasonCode: Why was family member history performed?
    :param Reference reasonReference: Why was family member history performed?
    :param Annotation note: General note about related person
    :param Condition condition: Condition that the related person had
    """

    resourceType: str = "FamilyMemberHistory"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    status: str = None
    
    dataAbsentReason: "CodeableConcept" = CodeableConcept()
    
    patient: "Reference" = Reference()
    
    date: str = None
    
    name: str = None
    
    relationship: "CodeableConcept" = CodeableConcept()
    
    sex: "CodeableConcept" = CodeableConcept()
    
    bornPeriod: "Period" = Period()
    
    ageAge: "Age" = Age()
    
    estimatedAge: bool = None
    
    deceasedBoolean: bool = None
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    
    condition: list[Condition] = Condition() 
    